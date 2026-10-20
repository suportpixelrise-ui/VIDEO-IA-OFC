import {AbsoluteFill} from 'remotion';
import {Room,Vignette,useMoment} from '../stage';
export const Cadeira=()=>{
 const {global}=useMoment('cadeira');
 return <AbsoluteFill><Room global={global} turn/><Vignette/></AbsoluteFill>;
};
