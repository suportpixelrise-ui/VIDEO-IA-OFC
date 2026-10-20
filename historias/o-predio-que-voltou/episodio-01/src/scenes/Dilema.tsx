import {AbsoluteFill} from 'remotion';
import {Actor,Background,Bus,Vignette,useMoment,span,story} from '../stage';
export const Dilema=()=>{
 const {t,global}=useMoment('dilema');const reach=span(global,story.events.hand,story.events.hand+1.8);
 return <AbsoluteFill>
  <Background name="fachada-proxima.png"/>
  <div style={{position:'absolute',left:0,top:0,width:345,height:1920,overflow:'hidden'}}><Bus x={-375} y={1020} w={650} move={35+Math.min(40,t*2)} driver/></div>
  <Actor x={150} y={570} scale={.9} face={1} lookLeft={t>7.2&&t<10.4} rightArm={-42*reach} headTurn={t>7.2&&t<10.4?-4:2} breath={Math.sin(t*1.5)*1.5}/>
  <Vignette/>
 </AbsoluteFill>;
};
