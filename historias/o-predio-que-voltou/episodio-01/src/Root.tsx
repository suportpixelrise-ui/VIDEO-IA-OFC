import {Composition,Folder} from 'remotion';
import {Episode} from './Episode';
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

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition id="ACadeiraVazia" component={Episode} width={1080} height={1920} fps={30} durationInFrames={3574} defaultProps={{music:true}}/>
      <Folder name="Cenas">
       <Composition id="01-Perda" component={Perda} width={1080} height={1920} fps={30} durationInFrames={551}/>
       <Composition id="02-Abrigo" component={Abrigo} width={1080} height={1920} fps={30} durationInFrames={465}/>
       <Composition id="03-Partida" component={Partida} width={1080} height={1920} fps={30} durationInFrames={318}/>
       <Composition id="04-Retorno" component={Retorno} width={1080} height={1920} fps={30} durationInFrames={139}/>
       <Composition id="05-Travessia" component={Travessia} width={1080} height={1920} fps={30} durationInFrames={153}/>
       <Composition id="06-Jantar" component={Jantar} width={1080} height={1920} fps={30} durationInFrames={369}/>
       <Composition id="07-Vidro" component={Vidro} width={1080} height={1920} fps={30} durationInFrames={195}/>
       <Composition id="08-Cadeira" component={Cadeira} width={1080} height={1920} fps={30} durationInFrames={193}/>
       <Composition id="09-Onibus" component={Onibus} width={1080} height={1920} fps={30} durationInFrames={206}/>
       <Composition id="10-Dilema" component={Dilema} width={1080} height={1920} fps={30} durationInFrames={401}/>
       <Composition id="11-Escolha" component={Escolha} width={1080} height={1920} fps={30} durationInFrames={584}/>
      </Folder>
    </>
  );
};
