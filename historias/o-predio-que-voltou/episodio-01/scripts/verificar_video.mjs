import {createRequire} from 'node:module';
import {createServer} from 'node:http';
import {createReadStream,statSync,mkdirSync,writeFileSync} from 'node:fs';
import path from 'node:path';
const root=process.cwd();
// QA-only browser dependency already installed in the workspace example.
const require=createRequire(path.resolve(root,'../../../shotcraft-demo/package.json'));
const puppeteer=require('puppeteer');
const video=path.join(root,'renders/episodio-01-principal.mp4');
const size=statSync(video).size;
const server=createServer((req,res)=>{
 if(req.url!='/video.mp4'){res.writeHead(404);res.end();return;}
 const m=/bytes=(\d+)-(\d*)/.exec(req.headers.range||'');
 if(m){const start=Number(m[1]),end=m[2]?Math.min(size-1,Number(m[2])):size-1;
  res.writeHead(206,{'Content-Type':'video/mp4','Accept-Ranges':'bytes','Content-Range':`bytes ${start}-${end}/${size}`,'Content-Length':end-start+1});
  createReadStream(video,{start,end}).pipe(res);
 }else{res.writeHead(200,{'Content-Type':'video/mp4','Content-Length':size,'Accept-Ranges':'bytes'});createReadStream(video).pipe(res);}
});
await new Promise(resolve=>server.listen(3011,'127.0.0.1',resolve));
const browser=await puppeteer.launch({headless:true,executablePath:process.env.PUPPETEER_EXECUTABLE_PATH,args:['--autoplay-policy=no-user-gesture-required']});
try{
 const page=await browser.newPage();await page.setViewport({width:540,height:960});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.setContent('<!doctype html><html><body style="margin:0;background:#111"><video id="v" autoplay playsinline controls style="width:540px;height:960px" src="http://127.0.0.1:3011/video.mp4"></video></body></html>');
 await page.$eval('video',async v=>{v.muted=false;v.volume=1;await v.play();});
 const points=[2,15,30,45,54,68,76,85,99,112,118];let next=0;let finished=false;
 mkdirSync(path.join(root,'renders/qa/playback'),{recursive:true});
 const sampled=[];
 while(!finished){
  const state=await page.$eval('video',v=>({time:v.currentTime,duration:v.duration,ended:v.ended,error:v.error?.message,muted:v.muted,volume:v.volume,paused:v.paused}));
  if(state.error)throw new Error(state.error);
  if(next<points.length&&state.time>=points[next]){
   await page.screenshot({path:path.join(root,`renders/qa/playback/t${points[next]}.png`)});
   sampled.push(state);console.log(`Reprodução com som: ${state.time.toFixed(1)} / ${state.duration.toFixed(1)}s`);next++;
  }
  finished=state.ended;
  if(!finished)await new Promise(resolve=>setTimeout(resolve,300));
 }
 const quality=await page.$eval('video',v=>({width:v.videoWidth,height:v.videoHeight,ended:v.ended,muted:v.muted,volume:v.volume,duration:v.duration,quality:v.getVideoPlaybackQuality().toJSON?.()||{droppedVideoFrames:v.getVideoPlaybackQuality().droppedVideoFrames,totalVideoFrames:v.getVideoPlaybackQuality().totalVideoFrames}}));
 writeFileSync(path.join(root,'docs/verificacao-playback.json'),JSON.stringify({quality,sampled,errors,method:'Reprodução integral, velocidade 1x, som habilitado; quadros amostrados. Não substitui avaliação humana da naturalidade da locução.'},null,2));
 console.log(JSON.stringify(quality));
 if(errors.length)process.exitCode=1;
}finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
