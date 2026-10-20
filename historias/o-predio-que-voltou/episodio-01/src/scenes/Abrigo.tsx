import {AbsoluteFill} from 'remotion';
import {Actor,Background,Exterior,Survivor,Vignette,useMoment,span} from '../stage';
export const Abrigo=()=>{
 const {t}=useMoment('abrigo');
 return <AbsoluteFill>
  {t<3.8?<><Exterior zoom={1.12}/><Actor x={-80} y={1100} scale={.44} face={1}/></>:<>
   <Background name="cenario-escola-abrigo.png" position="56% 50%"/>
   <Survivor person={0} x={40} y={780} scale={.7} lean={Math.sin(t)*.7}/>
   <Survivor person={1} x={800} y={890} scale={.55}/>
   <Actor x={300} y={655} scale={.9} face={1} headTurn={-5+Math.sin(t*.7)*2} leftArm={-24*(span(t,5,6)-span(t,8,9))} breath={Math.sin(t*1.8)*2}/>
   <div style={{position:'absolute',left:82,top:125,fontFamily:'Arial',fontSize:38,letterSpacing:4,fontWeight:700,color:'#f8e8c4'}}>O ABRIGO · HOJE</div>
  </>}
  <Vignette/>
 </AbsoluteFill>;
};
