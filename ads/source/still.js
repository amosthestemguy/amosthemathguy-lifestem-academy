const { chromium } = require('playwright'); const path=require('path');
const [ad, fmt, t, out] = process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport: fmt==='story'?{width:540,height:960}:{width:540,height:675}});
await p.goto('file://'+path.resolve(__dirname,'ad.html')+`?ad=${ad}&fmt=${fmt}`);await p.evaluate(()=>window.READY);
await p.evaluate(t=>window.render(t),+t);await p.screenshot({path:out});await b.close();})();
