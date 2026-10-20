import {AbsoluteFill} from 'remotion';
import {Actor,Bus,Exterior,Vignette,useMoment,span} from '../stage';
export const Retorno=()=>{
 const {t}=useMoment('retorno');
 return <AbsoluteFill>
  <Exterior returned={t>=.75}/>
  <Bus x={-420} y={970} w={920}/>
  <Actor x={78} y={880} scale={.78} face={2} headTurn={-3+span(t,.05,.7)*12} rightArm={-8} breath={Math.sin(t*1.7)*1.2}/>
  {t>=.75&&<div style={{position:'absolute',left:815,top:940,width:210,height:210,background:'#ffd485',filter:'blur(70px)',opacity:.1}}/>}
  <Vignette/>
 </AbsoluteFill>;
};
