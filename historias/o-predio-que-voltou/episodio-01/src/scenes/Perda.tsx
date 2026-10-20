import {AbsoluteFill} from 'remotion';
import {Actor,Exterior,Vignette,useMoment,span} from '../stage';
export const Perda=()=>{
 const {t}=useMoment('perda');const close=t>9.8;
 const walking=t<2.7?1-span(t,2,2.7):0;
 return <AbsoluteFill>
  <Exterior zoom={close?1.13:1}/>
  <Actor x={close?180:90+span(t,0,2.6)*65} y={close?610:930} scale={close?1.12:.67} face={t>4?1:0} headTurn={t<8?Math.sin(t*1.3)*6:3} walk={walking} gait={t*7.8} breath={Math.sin(t*1.8)*1.5}/>
  <div style={{position:'absolute',left:85,top:125,fontFamily:'Arial',fontSize:39,fontWeight:700,letterSpacing:4,color:'#fff3de',textShadow:'0 3px 9px #152232'}}>HÁ DOZE DIAS</div>
  <Vignette/>
 </AbsoluteFill>;
};
