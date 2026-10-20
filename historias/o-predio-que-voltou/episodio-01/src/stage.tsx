import React from 'react';
import {AbsoluteFill, CanvasImage, Img, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import data from './timeline.json';
import rigData from './rigs.json';

type Atlas = {file:string;width:number;height:number;parts:Record<string,number[]>};
export const rigs = rigData as unknown as Record<string,Atlas>;
export const story = data;
export const clamp = (n:number,a=0,b=1)=>Math.max(a,Math.min(b,n));
export const smooth = (n:number)=>{const t=clamp(n);return t*t*(3-2*t);};
export const span = (t:number,a:number,b:number)=>smooth((t-a)/(b-a));
export const asset = (name:string)=>staticFile(`assets/${name}`);
export const useMoment = (id:string)=>{
  const frame=useCurrentFrame();const {fps}=useVideoConfig();
  const scene=story.scenes.find(s=>s.id===id)!;
  return {frame,fps,t:frame/fps,global:scene.startSeconds+frame/fps,duration:scene.endSeconds-scene.startSeconds};
};

export const Sprite:React.FC<{atlas:string;part:string;x:number;y:number;w:number;h?:number;angle?:number;origin?:string;opacity?:number;style?:React.CSSProperties}>=({atlas,part,x,y,w,h,angle=0,origin='50% 5%',opacity=1,style})=>{
  const a=rigs[atlas];const box=a.parts[part];
  if(!box)throw new Error(`Missing sprite ${atlas}/${part}`);
  const [bx,by,bw,bh]=box;const height=h??w*bh/bw;
  return <div style={{position:'absolute',left:x,top:y,width:w,height,overflow:'hidden',rotate:`${angle}deg`,transformOrigin:origin,opacity,...style}}>
    <Img src={asset(a.file)} style={{position:'absolute',width:a.width*w/bw,height:a.height*height/bh,left:-bx*w/bw,top:-by*height/bh,maxWidth:'none'}}/>
  </div>;
};

export const Actor:React.FC<{who?:'lia'|'caio'|'motorista';x:number;y:number;scale?:number;face?:number;headTurn?:number;walk?:number;gait?:number;leftArm?:number;rightArm?:number;knock?:boolean;flip?:boolean;breath?:number;upperOnly?:boolean;lookLeft?:boolean}>=({who='lia',x,y,scale=1,face=0,headTurn=0,walk=0,gait=0,leftArm=0,rightArm=0,knock=false,flip=false,breath=0,upperOnly=false,lookLeft=false})=>{
  const swing=Math.sin(gait)*walk;
  const bounce=Math.abs(Math.sin(gait*2))*4*walk;
  return <div style={{position:'absolute',left:x,top:y,width:470,height:1000,scale:`${flip?-scale:scale} ${scale}`,transformOrigin:'0 0',translate:`0px ${-bounce}px`}}>
    {!upperOnly&&<div style={{position:'absolute',left:70,top:925,width:330,height:35,borderRadius:'50%',background:'#161b2490',filter:'blur(10px)'}}/>}
    {who==='lia'&&<Sprite atlas="lia" part="pack" x={30} y={315} w={190} h={255} angle={-5+swing*2}/>}
    {!upperOnly&&<>
      <Sprite atlas={who} part="legL" x={52} y={560} w={195} h={386} angle={swing*17} origin="70% 4%" style={{translate:`0px ${Math.max(0,-Math.sin(gait))*20*walk}px`}}/>
      <Sprite atlas={who} part="legR" x={234} y={562} w={195} h={384} angle={-swing*17} origin="24% 4%" style={{translate:`0px ${Math.max(0,Math.sin(gait))*20*walk}px`}}/>
    </>}
    <Sprite atlas={who} part="armL" x={57} y={328} w={125} h={300} angle={leftArm-swing*16} origin="67% 5%"/>
    <Sprite atlas={who} part="body" x={103} y={298+breath} w={276} h={309}/>
    {who==='lia'&&<svg width="470" height="660" style={{position:'absolute',left:0,top:0,pointerEvents:'none'}}><path d="M121 338 Q155 400 143 486" fill="none" stroke="#382a22" strokeWidth="20"/><path d="M121 338 Q155 400 143 486" fill="none" stroke="#a74140" strokeWidth="13"/></svg>}
    <Sprite atlas={who} part={knock&&who==='lia'?'knock':'armR'} x={321} y={330+breath} w={125} h={300} angle={rightArm+swing*16} origin="30% 5%"/>
    <Sprite atlas={who} part={`head${face}`} x={55} y={9+breath} w={350} h={310} angle={headTurn} origin="50% 95%" style={{scale:lookLeft?'-1 1':'1 1'}}/>
  </div>;
};

export const Background:React.FC<{name:string;cool?:boolean;zoom?:number;position?:string;style?:React.CSSProperties}>=({name,cool=false,zoom=1,position='50% 50%',style})=><AbsoluteFill style={{overflow:'hidden',background:'#304149',...style}}>
  <CanvasImage src={asset(name)} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:position,scale:zoom}}/>
  {cool&&<AbsoluteFill style={{background:'linear-gradient(180deg,#152d4c28,#1b314638 60%,#15202c44)',mixBlendMode:'multiply'}}/>}
</AbsoluteFill>;

export const Exterior:React.FC<{returned?:boolean;zoom?:number}>=({returned=false,zoom=1})=><Background name={returned?'rua-predio-vertical.png':'rua-vazia-vertical.png'} cool zoom={zoom}/>;

export const Bus:React.FC<{x?:number;y?:number;w?:number;move?:number;driver?:boolean}>=({x=-280,y=910,w=950,move=0,driver=false})=><div style={{position:'absolute',left:x+move,top:y,width:w,height:w*.6}}>
  <div style={{position:'absolute',left:w*.1,top:w*.48,width:w*.8,height:36,borderRadius:'50%',background:'#15202c66',filter:'blur(12px)'}}/>
  <Sprite atlas="onibus" part="full" x={0} y={0} w={w}/>
  {driver&&<div style={{position:'absolute',left:w*.705,top:w*.09,width:w*.15,height:w*.19,overflow:'hidden',borderRadius:16}}>
    <Actor who="motorista" x={0} y={0} scale={w/3100} upperOnly face={1}/>
    <div style={{position:'absolute',inset:0,background:'#39576f25'}}/>
  </div>}
</div>;

export const Survivor:React.FC<{person?:number;x:number;y:number;scale?:number;lean?:number}>=({person=0,x,y,scale=1,lean=0})=><Sprite atlas="extras" part={`person${person}`} x={x} y={y} w={230*scale} angle={lean} origin="50% 100%"/>;

export const Vignette:React.FC=()=> <AbsoluteFill style={{boxShadow:'inset 0 0 170px 12px #10203144',pointerEvents:'none'}}/>;

export const Door:React.FC<{x?:number;y?:number;w?:number;h?:number;handle?:boolean}>=({x=765,y=630,w=330,h=990,handle=true})=><div style={{position:'absolute',left:x,top:y,width:w,height:h,background:'#6b3e25',border:'18px solid #2f251e',boxShadow:'inset 0 0 0 10px #ab7746'}}>
  <div style={{position:'absolute',inset:'38px 30px 43%',border:'9px solid #46301f',background:'#7d4a2b'}}/>
  <div style={{position:'absolute',inset:'61% 30px 40px',border:'9px solid #46301f',background:'#754229'}}/>
  {handle&&<div style={{position:'absolute',left:30,top:'54%',width:72,height:24,borderRadius:12,background:'#b69b6d',border:'4px solid #3b3024',boxShadow:'0 5px 0 #3a2b20'}}/>}
</div>;

export const Window:React.FC<{t:number;knockTime?:number}>=({t,knockTime=0})=><>
 <div style={{position:'absolute',left:822,top:360,width:360,height:1000,border:'23px solid #28534d',background:'linear-gradient(120deg,#eab16c27,#c8e6df1a)',boxShadow:'inset 0 0 0 7px #131f26'}}/>
 <div style={{position:'absolute',left:839,top:800,width:300,height:15,background:'#28534d'}}/>
 <div style={{position:'absolute',left:913,top:425,width:10,height:170,rotate:'20deg',background:'#e5eed533'}}/>
 {[0,.31,.62].map((offset,i)=>{const pulse=1-clamp((t-knockTime-offset)/.23);return t>=knockTime+offset&&t<knockTime+offset+.23?<div key={i} style={{position:'absolute',left:790,top:932,width:40+(1-pulse)*40,height:40+(1-pulse)*40,border:'4px solid #ffe4b8',borderRadius:'50%',opacity:pulse*.55}}/>:null;})}
</>;

export const CaptionLayer:React.FC=()=>{
 const frame=useCurrentFrame(); const {fps}=useVideoConfig();const time=frame/fps;
 const c=story.captions.find(v=>time>=v.start&&time<v.end);
 return c?<div style={{position:'absolute',left:80,right:100,bottom:142,display:'flex',justifyContent:'center',pointerEvents:'none'}}><div style={{maxWidth:900,padding:'17px 27px',borderRadius:17,background:'#111c27e8',border:'2px solid #ffffff1c',fontFamily:'Arial, sans-serif',fontSize:48,fontWeight:700,lineHeight:1.23,textAlign:'center',color:'#fff7e6',textShadow:'0 2px 1px #000',whiteSpace:'pre-line'}}>{c.text}</div></div>:null;
};

export const Room:React.FC<{global:number;chair?:boolean;turn?:boolean}>=({global,chair=true,turn=false})=>{
 const pull=span(global,story.events.chair+.12,story.events.chair+1.35);
 const reach=span(global,story.events.caio_turn+.5,story.events.chair+.1);
 const turned=turn&&global>=story.events.caio_turn;
 return <>
  <Background name="jantar-vertical.png"/>
  <Actor who="caio" x={346} y={510} scale={.83} upperOnly face={turned?1:0} headTurn={turned?0:-6} rightArm={-48*reach+25*pull}/>
  {/* Restore foreground tabletop from the SAME plate: Caio remains seated behind it. */}
  <div style={{position:'absolute',inset:0,clipPath:'polygon(5% 48%,96% 48%,100% 100%,0 100%)'}}><Background name="jantar-vertical.png"/></div>
  {turn&&reach>.02&&<div style={{position:'absolute',left:346,top:510,scale:.83,transformOrigin:'0 0',width:470,height:1000}}><Sprite atlas="caio" part="armR" x={321} y={330} w={125} h={360} angle={-48*reach+25*pull} origin="30% 5%"/></div>}
  {chair&&<Sprite atlas="cadeira" part="full" x={660-100*pull} y={970+85*pull} w={335} angle={-3*pull} origin="50% 90%"/>}
  {[0,1,2].map(i=><svg key={i} width="80" height="150" style={{position:'absolute',left:272+i*24,top:895-((global*24+i*19)%90),opacity:.26*(1-((global*24+i*19)%90)/120),rotate:`${i%2?4:-4}deg`}}><path d="M35 130 C5 100 65 75 32 45 C14 28 30 15 38 5" stroke="#fff2d4" strokeWidth="6" fill="none" strokeLinecap="round"/></svg>)}
 </>;
};

export const ClosedDoorSetting:React.FC=()=> <><AbsoluteFill style={{background:'#d5b68c'}}/><svg width="1080" height="1920" style={{position:'absolute'}}><path d="M0 1490 L1080 1450 L1080 1920 L0 1920Z" fill="#a77e5f"/><path d="M0 1490 H1080 M0 1760 H1080 M200 1490 L140 1920 M760 1490 L940 1920" stroke="#6e6152" strokeWidth="5"/></svg><div style={{position:'absolute',left:0,right:0,top:420,bottom:400,background:'#78918c'}}/><Door/></>;
