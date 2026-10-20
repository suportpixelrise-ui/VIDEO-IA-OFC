import {AbsoluteFill} from 'remotion';
import {Actor,Bus,Exterior,Vignette,useMoment,span,story} from '../stage';
export const Onibus=()=>{
 const {t,global}=useMoment('onibus');const move=100*span(global,story.events.bus_move,story.events.bus_move+5);
 return <AbsoluteFill>
  <Exterior returned/>
  <Bus x={-280} y={930} w={1120} move={move} driver/>
  <Actor x={600} y={775} scale={.73} face={1} lookLeft={t>.3} headTurn={t>.3?-5:5} leftArm={-5}/>
  <Vignette/>
 </AbsoluteFill>;
};
