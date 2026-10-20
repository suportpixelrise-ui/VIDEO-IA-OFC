import {AbsoluteFill} from 'remotion';
import {Actor,Bus,Exterior,Survivor,Vignette,useMoment,span} from '../stage';
export const Partida=()=>{
 const {t,duration}=useMoment('partida');const step=span(t,.3,2.3);
 return <AbsoluteFill>
  <Exterior/>
  <Bus x={-350} y={920} w={1050}/>
  <Actor who="motorista" x={-10} y={1010} scale={.51} face={0} rightArm={-24}/>
  <Survivor person={0} x={252} y={1160} scale={.64}/>
  <Survivor person={1} x={400} y={1190} scale={.62}/>
  <Actor x={500+40*step} y={940} scale={.61} face={t>duration-1.4?2:1} headTurn={t>duration-1.4?8:-2} walk={t<2.3?.75:0} gait={t*7.8}/>
  {t>duration-.7&&<AbsoluteFill style={{background:'linear-gradient(90deg,transparent 55%,#ffc96d21)'}}/>}
  <Vignette/>
 </AbsoluteFill>;
};
