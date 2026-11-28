const { chromium } = require('playwright'); const path=require('path');
const jobs = JSON.parse(process.argv[2]);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:540,height:960},deviceScaleFactor:2});
for (const j of jobs){ const q=new URLSearchParams(j.q).toString();
 await p.goto('file://'+path.resolve(__dirname,'card.html')+'?'+q); await p.evaluate(()=>window.READY);
 await p.screenshot({path:j.out}); console.log('card',j.out);}
await b.close();})();
