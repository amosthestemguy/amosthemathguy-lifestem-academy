const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const [q,w,h,out] of [['m=thanks',1080,1350,'thanksgiving_feed.png'],['m=thanks',1080,1920,'thanksgiving_story.png'],['m=potd',1080,1920,'potd_2026-11-26_story.png']]){
const p=await b.newPage({viewport:{width:w,height:h}});await p.goto('file://'+__dirname+'/img.html?'+q);await p.waitForTimeout(1500);await p.screenshot({path:out});await p.close();}
await b.close();})();
