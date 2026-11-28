const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const [m,w,h] of [['s',1080,220],['l',1080,100]]){const p=await b.newPage({viewport:{width:w,height:h}});await p.goto('file://'+__dirname+'/ban.html?m='+m);await p.waitForTimeout(1200);await p.screenshot({path:'ban_'+m+'.png',omitBackground:true});await p.close();}
await b.close();})();
