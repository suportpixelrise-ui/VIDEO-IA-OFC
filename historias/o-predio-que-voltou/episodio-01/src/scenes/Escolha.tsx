import {AbsoluteFill} from 'remotion';
import {Actor,Background,Bus,Vignette,useMoment,span} from '../stage';
export const Escolha=()=>{
 const {t}=useMoment('escolha');const opacity=span(t,.1,.8);
 const left=Math.floor(t/3)%2===1;
 return <AbsoluteFill>
  <Background name="fachada-proxima.png"/>
  <div style={{position:'absolute',left:0,top:0,width:345,height:1920,overflow:'hidden'}}><Bus x={-355} y={1020} w={650} move={55+Math.min(25,t)} driver/></div>
  <Actor x={150} y={570} scale={.9} face={1} lookLeft={left} rightArm={-42} headTurn={left?-3:3} breath={Math.sin(t*1.5)*1.5}/>
  <Vignette/>
  <div style={{position:'absolute',left:74,right:94,top:1185,opacity,fontFamily:'Arial, sans-serif',color:'#fff4dc'}}>
   <div style={{fontSize:54,fontWeight:700,textAlign:'center',marginBottom:28,textShadow:'0 3px 8px #13222c'}}>O que Lia deve fazer?</div>
   <div style={{background:'#162b37f2',border:'3px solid #f5d299',borderRadius:22,padding:'26px 24px',display:'flex',gap:22,alignItems:'center',marginBottom:22}}><b style={{fontSize:66,lineHeight:1,color:'#f5d299'}}>A</b><span style={{fontSize:45,fontWeight:700}}>ENTRAR NO PRÉDIO</span></div>
   <div style={{background:'#162b37f2',border:'3px solid #f5d299',borderRadius:22,padding:'26px 24px',display:'flex',gap:22,alignItems:'center'}}><b style={{fontSize:66,lineHeight:1,color:'#f5d299'}}>B</b><span style={{fontSize:45,fontWeight:700}}>PEGAR O ÔNIBUS</span></div>
  </div>
 </AbsoluteFill>;
};
