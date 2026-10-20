import {AbsoluteFill,Sequence,useVideoConfig} from 'remotion';
import {Audio} from '@remotion/media';
import {staticFile} from 'remotion';
import {CaptionLayer} from './stage';
import {Perda} from './scenes/Perda';
import {Abrigo} from './scenes/Abrigo';
import {Partida} from './scenes/Partida';
import {Retorno} from './scenes/Retorno';
import {Travessia} from './scenes/Travessia';
import {Jantar} from './scenes/Jantar';
import {Vidro} from './scenes/Vidro';
import {Cadeira} from './scenes/Cadeira';
import {Onibus} from './scenes/Onibus';
import {Dilema} from './scenes/Dilema';
import {Escolha} from './scenes/Escolha';
export type EpisodeProps={music:boolean};
export const Episode=({music}:EpisodeProps)=>{
 const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#25363d'}}>
  <Sequence durationInFrames={551} name="01 · A perda" premountFor={fps}><Perda/></Sequence>
  <Sequence from={551} durationInFrames={465} name="02 · O abrigo" premountFor={fps}><Abrigo/></Sequence>
  <Sequence from={1016} durationInFrames={318} name="03 · A última partida" premountFor={fps}><Partida/></Sequence>
  <Sequence from={1334} durationInFrames={139} name="04 · O retorno" premountFor={fps}><Retorno/></Sequence>
  <Sequence from={1473} durationInFrames={153} name="05 · A travessia" premountFor={fps}><Travessia/></Sequence>
  <Sequence from={1626} durationInFrames={369} name="06 · O jantar" premountFor={fps}><Jantar/></Sequence>
  <Sequence from={1995} durationInFrames={195} name="07 · O vidro" premountFor={fps}><Vidro/></Sequence>
  <Sequence from={2190} durationInFrames={193} name="08 · A cadeira vazia" premountFor={fps}><Cadeira/></Sequence>
  <Sequence from={2383} durationInFrames={206} name="09 · A buzina" premountFor={fps}><Onibus/></Sequence>
  <Sequence from={2589} durationInFrames={401} name="10 · O custo da escolha" premountFor={fps}><Dilema/></Sequence>
  <Sequence from={2990} durationInFrames={584} name="11 · A decisão do público" premountFor={fps}><Escolha/></Sequence>
  <CaptionLayer/>
  <Audio src={staticFile('audio/narracao.m4a')} premountFor={fps}/>
  <Audio src={staticFile('audio/efeitos.m4a')} premountFor={fps}/>
  {music&&<Audio src={staticFile('audio/trilha.m4a')} premountFor={fps}/>}
 </AbsoluteFill>;
};
