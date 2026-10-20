import {AbsoluteFill} from 'remotion';
import {Actor,Bus,Exterior,Vignette,useMoment,span} from '../stage';
export const Travessia=()=>{
 const {t}=useMoment('travessia');const progress=span(t,.15,4.4);
 return <AbsoluteFill>
  <Exterior returned/>
  <Bus x={-420} y={970} w={920}/>
  <Actor x={200+progress*400} y={920-progress*70} scale={.63} face={2} walk={t<4.4?1:0} gait={t*8.2} headTurn={4}/>
  <Vignette/>
 </AbsoluteFill>;
};
