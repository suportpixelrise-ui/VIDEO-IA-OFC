import {AbsoluteFill} from 'remotion';
import {Room,Vignette,useMoment} from '../stage';
export const Jantar=()=>{
 const {global}=useMoment('jantar');
 return <AbsoluteFill><Room global={global}/><Vignette/></AbsoluteFill>;
};
