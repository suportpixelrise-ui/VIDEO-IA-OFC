import {bundle} from '@remotion/bundler';
import {openBrowser,renderStill,selectComposition} from '@remotion/renderer';
import path from 'node:path';
import {mkdirSync,writeFileSync} from 'node:fs';
const root=process.cwd();
const frames=process.argv[2]?process.argv[2].split(',').map(Number):[150,420,780,1170,1380,1530,1740,2040,2250,2290,2335,2490,2730,3210];
mkdirSync(path.join(root,'renders/qa'),{recursive:true});
const serveUrl=await bundle({entryPoint:path.join(root,'src/index.ts'),outDir:path.join(root,'.work/bundle')});
const browser=await openBrowser('chrome',{browserExecutable:process.env.PUPPETEER_EXECUTABLE_PATH});
try{
 const composition=await selectComposition({serveUrl,id:'ACadeiraVazia',puppeteerInstance:browser});
 for(const frame of frames){
  await renderStill({serveUrl,composition,frame,scale:.5,imageFormat:'png',output:path.join(root,`renders/qa/f${frame}.png`),puppeteerInstance:browser});
  console.log(`QA frame ${frame} / ${(frame/30).toFixed(2)}s`);
 }
 writeFileSync(path.join(root,'docs/verificacao-render-qa.json'),JSON.stringify({composition,frames,scale:.5},null,2));
}finally{await browser.close({silent:true});}
