import {AbsoluteFill} from 'remotion';
import {Actor,Background,Room,Vignette,useMoment,span,story} from '../stage';
export const Vidro=()=>{
 const {global}=useMoment('vidro');const k=story.events.knock;
 const raised=span(global,k-.48,k-.06)*(1-.8*span(global,k+1.6,k+2.6));
 let tap=0;
 for(const d of [0,.31,.62]){const phase=(global-k-d)/.2;if(phase>=0&&phase<1)tap+=Math.sin(phase*Math.PI)*6;}
 return <AbsoluteFill>
  <Background name="fachada-proxima.png"/>
  <div style={{position:'absolute',left:875,top:400,width:205,height:880,overflow:'hidden',clipPath:'polygon(0% 9%,100% 0%,100% 100%,0% 89%)',background:'#dfad6e'}}><div style={{position:'absolute',width:1080,height:1920,left:-178,top:-15,scale:.5,transformOrigin:'0 0'}}><Room global={global}/></div></div>
  <Actor x={185} y={595} scale={1.08} face={global>k+1.3?1:2} rightArm={-70*raised+tap} knock headTurn={3}/>
  <Vignette/>
 </AbsoluteFill>;
};
