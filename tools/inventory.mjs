// Lists every top-level array/object literal in index.html's inline scripts:
// name, size, whether it is pure data, and whether its source text is already JSON.
import fs from 'node:fs';
import * as acorn from 'acorn';
const file = process.argv.slice(2).find(a => !a.startsWith('--')) || new URL('../index.html', import.meta.url).pathname;
const html = fs.readFileSync(file, 'utf8');
const re = /<script\b([^>]*)>([\s\S]*?)<\/script>/gi;
let m, block = 0; const rows = [];
function pure(n) {
  switch (n.type) {
    case 'Literal': return !n.regex;
    case 'ArrayExpression': return n.elements.every(e => e && pure(e));
    case 'ObjectExpression': return n.properties.every(p => p.type === 'Property' && !p.computed && !p.method && p.kind === 'init' && pure(p.value));
    case 'UnaryExpression': return n.operator === '-' && n.argument.type === 'Literal' && typeof n.argument.value === 'number';
    case 'TemplateLiteral': return n.expressions.length === 0;
    default: return false;
  }
}
while ((m = re.exec(html))) {
  block++;
  if (/\bsrc=/.test(m[1])) continue;
  const off = m.index + m[0].indexOf('>') + 1;
  let ast;
  try { ast = acorn.parse(m[2], { ecmaVersion: 'latest', sourceType: 'script' }); }
  catch (e) { console.log(`block ${block}: PARSE ERROR ${e.message}`); continue; }
  for (const st of ast.body) {
    if (st.type !== 'VariableDeclaration') continue;
    for (const d of st.declarations) {
      if (!d.init || !/^(Array|Object)Expression$/.test(d.init.type)) continue;
      const src = m[2].slice(d.init.start, d.init.end);
      let json = false; try { JSON.parse(src); json = true; } catch {}
      rows.push({ block, kind: st.kind, name: d.id.name, bytes: src.length, pure: pure(d.init), json, start: off + d.init.start });
    }
  }
}
if (process.argv.includes("--json")) { console.log(JSON.stringify(rows)); process.exit(0); }
for (const r of rows) console.log([r.block, r.kind, r.name, r.bytes, r.pure ? 'pure' : 'code', r.json ? 'JSON' : '-', r.start].join('\t'));
console.log('total', rows.length, 'pure', rows.filter(r => r.pure).length, 'json', rows.filter(r => r.json).length);
