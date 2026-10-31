// The portal build: source/index.template.html + content/* -> index.html.
//
//   node tools/build.mjs            write index.html
//   node tools/build.mjs --check    rebuild in memory; fail unless it equals the committed index.html byte for byte
//   node tools/build.mjs --extract  the inverse: split index.html back into template + content
//
// The template holds a placeholder like @@CONTENT:academy.json@@ wherever a data
// structure's literal was. The build pastes each content file in, with one
// trailing newline removed, and escapes the two sequences that would end or
// confuse the surrounding <script> (</script and <!--). Nothing else is touched,
// so the output is exactly reproducible.
//
// --extract exists for the day someone edits index.html directly (a web upload, an
// older thread): it re-derives template + content from index.html, and refuses to
// write unless building the result reproduces index.html exactly.
import fs from 'node:fs';
import path from 'node:path';
import * as acorn from 'acorn';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

export const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const TEMPLATE = path.join(REPO, 'source', 'index.template.html');
export const CONTENT = path.join(REPO, 'content');
export const OUTPUT = path.join(REPO, 'index.html');
const MAP = JSON.parse(fs.readFileSync(path.join(REPO, 'tools', 'content-map.json'), 'utf8')).content;
const TOKEN = /@@CONTENT:([\w.-]+)@@/g;

export class BuildError extends Error {}

/** Makes a literal safe inside an inline <script>. Current content has neither sequence, so this is a no-op today. */
export function escapeForScript(text) {
  return text.replace(/<\/(script)/gi, '<\\/$1').replace(/<!--/g, '<\\!--');
}

function validate(file, text) {
  if (file.endsWith('.json')) {
    try { JSON.parse(text); } catch (e) { throw new BuildError(`content/${file} is not valid JSON: ${e.message}`); }
  } else {
    let node;
    try { node = acorn.parseExpressionAt(text, 0, { ecmaVersion: 'latest' }); } catch (e) { throw new BuildError(`content/${file} does not parse as JavaScript: ${e.message}`); }
    if (text.slice(node.end).trim() !== '') throw new BuildError(`content/${file} has text after the literal ends (offset ${node.end})`);
  }
}

export function build({ template = fs.readFileSync(TEMPLATE, 'utf8'), read = f => fs.readFileSync(path.join(CONTENT, f), 'utf8') } = {}) {
  const used = new Map();
  const out = template.replace(TOKEN, (_, file) => {
    if (!MAP.some(m => m.file === file)) throw new BuildError(`template names content/${file}, which is not in tools/content-map.json`);
    if (used.has(file)) throw new BuildError(`template names content/${file} twice`);
    let text = read(file);
    if (text.endsWith('\n')) text = text.slice(0, -1);
    validate(file, text);
    used.set(file, true);
    return escapeForScript(text);
  });
  for (const m of MAP) if (!used.has(m.file)) throw new BuildError(`content/${m.file} (${m.name}) has no placeholder in the template`);
  return out;
}

/** Finds each mapped top-level declaration's literal in index.html. Returns spans in file order. */
export function locate(html) {
  const spans = [];
  for (const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)) {
    if (/\bsrc=/.test(m[1])) continue;
    const off = m.index + m[0].indexOf('>') + 1;
    const ast = acorn.parse(m[2], { ecmaVersion: 'latest', sourceType: 'script' });
    for (const st of ast.body) {
      if (st.type !== 'VariableDeclaration') continue;
      for (const d of st.declarations) {
        const entry = MAP.find(x => x.name === d.id.name);
        if (entry && d.init) spans.push({ ...entry, start: off + d.init.start, end: off + d.init.end });
      }
    }
  }
  for (const e of MAP) {
    const n = spans.filter(s => s.name === e.name).length;
    if (n !== 1) throw new BuildError(`expected one top-level ${e.name} in index.html, found ${n}`);
  }
  return spans.sort((a, b) => a.start - b.start);
}

export function extract(html) {
  if (TOKEN.test(html)) throw new BuildError('index.html already contains a @@CONTENT@@ placeholder');
  TOKEN.lastIndex = 0;
  const files = {};
  let template = '', at = 0;
  for (const s of locate(html)) {
    const text = html.slice(s.start, s.end);
    if (s.file.endsWith('.json')) { try { JSON.parse(text); } catch { throw new BuildError(`${s.name} is mapped to a .json file but its literal is not JSON; map it to a .js file`); } }
    files[s.file] = text + '\n';
    template += html.slice(at, s.start) + `@@CONTENT:${s.file}@@`;
    at = s.end;
  }
  template += html.slice(at);
  const rebuilt = build({ template, read: f => files[f] });
  if (rebuilt !== html) throw new BuildError('extract would not round-trip; nothing written');
  return { template, files };
}

function firstDiff(a, b) {
  let i = 0; while (i < a.length && a[i] === b[i]) i++;
  const line = a.slice(0, i).split('\n').length;
  return `first difference at char ${i} (line ${line}): committed ${JSON.stringify(a.slice(i, i + 80))} vs built ${JSON.stringify(b.slice(i, i + 80))}`;
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  try {
    if (process.argv.includes('--extract')) {
      const { template, files } = extract(fs.readFileSync(OUTPUT, 'utf8'));
      fs.mkdirSync(path.dirname(TEMPLATE), { recursive: true });
      fs.mkdirSync(CONTENT, { recursive: true });
      fs.writeFileSync(TEMPLATE, template);
      for (const [f, t] of Object.entries(files)) fs.writeFileSync(path.join(CONTENT, f), t);
      console.log(`extracted ${Object.keys(files).length} content files and source/index.template.html; round trip verified`);
    } else if (process.argv.includes('--check')) {
      const committed = fs.readFileSync(OUTPUT, 'utf8');
      const built = build();
      if (built !== committed) { console.error(firstDiff(committed, built)); console.error('index.html does not match source/ + content/. If index.html was edited directly, run: node tools/build.mjs --extract'); process.exit(1); }
      console.log(`index.html: ${Buffer.byteLength(built)} bytes, ${MAP.length} content files`);
      console.log('BUILD REPRODUCES index.html');
    } else {
      // Refuse to emit a page that fails verify: write it, check it, and put the old one back if it fails.
      const built = build();
      const previous = fs.readFileSync(OUTPUT);
      fs.writeFileSync(OUTPUT, built);
      const r = spawnSync(process.execPath, [path.join(REPO, 'tools', 'verify.mjs'), '--disk'], { encoding: 'utf8' });
      if (r.status !== 0 || !/VERIFY OK/.test(r.stdout)) {
        fs.writeFileSync(OUTPUT, previous);
        process.stderr.write(r.stdout.split('\n').filter(l => l.startsWith('VERIFY FAIL')).join('\n') + '\n' + (r.stderr || ''));
        console.error('BUILD FAILED: the new index.html failed verify, so the previous one was kept');
        process.exit(1);
      }
      console.log(`wrote index.html (${Buffer.byteLength(built)} bytes) from source/ + ${MAP.length} content files; verify passed`);
    }
  } catch (e) {
    if (e instanceof BuildError) { console.error('BUILD FAILED: ' + e.message); process.exit(1); }
    throw e;
  }
}
