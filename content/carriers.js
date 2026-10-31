[
  /* smsFix: a carrier's text-message opt-in. When a client stops getting the
     carrier's texts it is almost always because an earlier one went to spam or
     they replied STOP once; texting the keyword back re-opens the channel.
     Add the same field to any other carrier once we have their number.
     Optional `products`: the product lines a number is CONFIRMED for, not the
     ones it is limited to. Transamerica's reached us for FE Express and IUL and
     may well cover more; nobody has checked, and their SMS terms are not public.
     The wording downstream says "confirmed for", never "only" — we are reporting
     what we were told, not a restriction we verified. Leave the field off when a
     number is known to cover the whole carrier, as Americo's is.
     Why state a scope at all under uncertainty: the two ways to be wrong are not
     equal. Over-state the scope and an agent with another product makes one
     unnecessary phone call. Under-state it and that agent tells a real client to
     text a number that does nothing — which is the exact failure this feature
     exists to prevent. So scope stands, and the copy sends them to try it anyway. */
  {name:'Americo',smsFix:{number:'877-638-1181',word:'START'},tags:['FEX','IUL','MP','Term'],phone:'800-231-0801 &middot; New business submit@americo.com &middot; Agent services agent.services@americo.com &middot; Marketing marketing.support@americo.com',links:[['★ Americo FFL Agent Hub — all tools & brochures','https://ffl.americo.com/'],['Agent Portal','https://portal.americoagent.com/'],['Training Portal (FFL)','https://americotraining.com/'],['IUL Training','https://americoiul.com/'],['Agent Portal (login)','https://account.americoagent.com/']]},
  {name:'Mutual of Omaha',tags:['FEX','Term','IUL','Annuity'],phone:'800-775-7896 (broker new business) &middot; Producer management 800-867-6873 &middot; Producer tech support 800-228-7669 &middot; New business fax 402-997-1800',links:[['Producer Portal','https://producer.mutualofomaha.com/'],['All Products (browse)','https://producer2.mutualofomaha.com/products'],['Quote Tool','https://www3.mutualofomaha.com/mobile-quotes/#/home'],['Agent e-App','https://accounts.mutualofomaha.com/']],note:'When listing individual products, skip dental (hospital indemnity is fine)'},
  {name:'Athene',tags:['Annuity'],phone:'Sales desk 855-428-4363 (855-4-ATHENE) &middot; General 888-266-8489 (888-ANNUITY)',links:[['Producer Login (Athene Connect)','https://www.athene.com/producer/login'],['Producer Site','https://www.athene.com/producer']]},
  {name:'F&G (Fidelity & Guaranty)',tags:['IUL','Annuity'],phone:'888-513-8797 &middot; Agent hotline 800-445-6758 &middot; agentcare@fglife.com',links:[['Agent Portal','https://www.fglife.com/'],['Agent Portal (SalesLink)','https://saleslink.fglife.com/']]},
  {name:'Transamerica',smsFix:{number:'469-484-7817',word:'START',products:'FE Express and IUL'},tags:['IUL','Term','FEX'],phone:'877-234-4848 &middot; New business fax 866-834-0437',links:[['Advisor Experience (Portal + E-app)','https://secure.transamerica.com/login/sign-in/login.html'],['FFIUL Express (IUL)','https://www.transamerica.com/ffiul2-express'],['IUL Application Video','https://cdn.bfldr.com/86JM1UOD/as/thxtf3v44wmz2n66p8kjcwqn/Transamerica_IULX_Application'],['Quote Tool (TransWare)','https://mytranswarequote.transamerica.com/Wl3.html']]},
  {name:'Combined / Chubb',tags:['Supplemental'],phone:'801-658-9911',links:[['Agent Portal','https://chubb.insuranceadmin.com/']]},
  {name:'Instabrain',tags:[],phone:'800-806-9714',links:[['Agent Portal','https://portal.instabrain.io/Account/Login']]},
  {name:'National Life Group (NLG)',tags:['IUL'],phone:'800-906-3310 (pre-sale, contracting, commissions) &middot; Customer service 800-732-8939 &middot; Tech help desk 877-654-3499 &middot; agentservices@nationallife.com',links:[['Agent Login','https://www.nationallife.com/agent/auth/login'],['Agent Site','https://www.nationallife.com/'],['FlexLife Illustration — Max DB','https://www.loom.com/share/8385237c46e14910b1ff9b47f11a85bc'],['FlexLife Illustration — Max Cash','https://www.loom.com/share/b90a23619484438f84e4fa438112f3a5'],['Quote / Financial Calculators','https://www.nationallife.com/Resource-center/Financial-Calculators']]},
  {name:'American Amicable / Occidental',tags:['Term','FEX'],phone:'800-736-7311 &middot; Agent hotline: options 1,1,2 &middot; agencyservices@americanamicable.com',links:[['Agent Marketing Site','https://www.occidentallife.com/Marketing/area/A/marketing.php'],['Agent Portal','https://www.americanamicable.com/v4/AgentLogin.php'],['Agent e-App','https://www.insuranceapplication.com/cgi/webappmobile/login.aspx']]},
  {name:'Corebridge / AIG',tags:['Term','IUL','Annuity'],phone:'800-677-3311 (life producers) &middot; Annuities 888-502-2900 &middot; Policyholders 800-888-2452',links:[['Agent Portal','https://www.corebridgefinancial.com/'],['E-app','https://www.connext.corebridgefinancial.com/life/connext-portal/public/login']]},
  {name:'Foresters',tags:['FEX','Term','Whole Life'],phone:'877-622-4249 &middot; New business fax 877-329-4631',links:[['Agent Portal (ezbiz)','https://myezbiz.foresters.com/'],['Coverage Needs Calculator (client-facing)','https://www.foresters.com/en/life-insurance/life-insurance-calculator']]},
  {name:'Cigna',tags:['Supplemental','MA','ACA'],phone:'866-442-7516 (MA) &middot; 866-438-2446 (ACA)',links:[['Agent Portal (Cigna for Brokers)','https://www.cignaforbrokers.com/public/login'],['Quote / Plans','https://www.cigna.com/']]},
  {name:'Aetna',tags:['Supplemental','MA'],phone:'866-714-9301 (Medicare broker services) &middot; 866-272-6630 &middot; Producer World tech support 800-225-3375 &middot; brokersupport@aetna.com',links:[['Agent Portal','https://www.aetna.com/producer_public/login.fcc'],['Get a Quote','https://www.aetna.com/insurance-producer/working-with-aetna/get-a-quote.html']]},
  {name:'LifeX',tags:[],phone:'844-580-2474',links:[['Agent Portal','https://enrollment123.com/manage/index.cfm']]},
  {name:'Ameritas',tags:[],phone:'800-745-1112',links:[['Agent Portal','https://service.ameritas.com/service/login.asp']]}
]
