const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
for(const [q,out] of JSON.parse(process.argv[2])){await p.goto('file://'+__dirname+'/lf.html?'+q);await p.waitForTimeout(1500);await p.screenshot({path:out,omitBackground:true});}
await b.close();})();
