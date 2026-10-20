"""Offline: measure the actual voice, align subtitles, synthesize original score/SFX."""
from pathlib import Path
import json
import math
import re
import subprocess
import wave
import numpy as np
from scipy import signal

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT/'.work/audio'
WORK.mkdir(parents=True, exist_ok=True)
SR = 48000
FPS = 30
segments = json.loads((ROOT/'docs/segmentos-locucao.json').read_text(encoding='utf-8'))
word_blocks = json.loads((ROOT/'docs/palavras-locucao-local.json').read_text(encoding='utf-8-sig'))
parts = [np.zeros(int(.8*SR),dtype=np.float32)]
cursor = .8
captions = []
timed = []

def load_wav(path):
    with wave.open(str(path),'rb') as w:
        rate, channels = w.getframerate(), w.getnchannels()
        a=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').astype(np.float32)/32768
        if channels>1: a=a.reshape(-1,channels).mean(axis=1)
    divisor=math.gcd(SR,rate)
    return signal.resample_poly(a,SR//divisor,rate//divisor).astype(np.float32)

for item, word_block in zip(segments,word_blocks):
    audio=load_wav(ROOT/'public/audio/locucao'/f'{item["id"]}.wav')
    duration=len(audio)/SR
    words=word_block['words']
    # Windows SAPI's event clock can drift past the emitted WAV. Fit its
    # monotonic offsets to the actual audible extent, never into the next block.
    window=round(.02*SR)
    energy=np.array([np.sqrt(np.mean(audio[k:k+window]**2)) for k in range(0,len(audio),window)])
    active=np.flatnonzero(energy>max(.002,float(energy.max())*.035))
    audible_start=float(active[0]*.02) if len(active) else .1
    audible_end=min(duration,float((active[-1]+1)*.02)) if len(active) else duration-.1
    first_reported=words[0]['Start']; last_reported=words[-1]['Start']
    last_word_start=max(audible_start+.2,audible_end-.32)
    for word in words:
        ratio=(word['Start']-first_reported)/max(.01,last_reported-first_reported)
        word['Start']=audible_start+ratio*(last_word_start-audible_start)
    timed.append({**item,'start':cursor,'end':cursor+duration,'duration':duration,
                  'words':[{'text':w['Text'],'start':cursor+w['Start']} for w in words]})
    # Use original spelling/punctuation, and the synthesizer's real word offsets.
    current=[]
    for i,w in enumerate(words):
        start=int(w.get('Char',0)); count=int(w.get('Count',len(w['Text'])))
        token=item['text'][start:start+count] if count else w['Text']
        if not token.strip(): token=w['Text']
        # Capture punctuation immediately following the spoken word.
        following=item['text'][start+count:]
        suffix=re.match(r'^[.,!?…:;]+',following)
        if suffix: token+=suffix.group(0)
        current.append((token,cursor+w['Start']))
        next_length=len(' '.join(x[0] for x in current))+(len(words[i+1]['Text'])+1 if i+1<len(words) else 0)
        trailing=current[-1][0].lower().strip('.,!?…:;')
        connector=trailing in {'o','a','os','as','do','da','de','no','na','em','e','com','para','um','uma','se','ao'}
        punctuation=token.endswith(('.', '!', '?')) and len(current)>=3
        clause=token.endswith((',', ';')) and len(' '.join(x[0] for x in current))>=22
        if ((next_length>49 and not connector) or punctuation or clause or i==len(words)-1):
            end=cursor+(words[i+1]['Start']-.04 if i+1<len(words) else min(duration-.03,audible_end+.15))
            captions.append({'start':current[0][1],'end':min(cursor+duration,max(current[0][1]+.25,end)),'text':' '.join(x[0] for x in current)})
            current=[]
    parts.append(audio)
    pause=item['pause_after']
    parts.append(np.zeros(round(pause*SR),dtype=np.float32))
    cursor+=duration+pause
parts.append(np.zeros(3*SR,dtype=np.float32))
voice=np.concatenate(parts)
voice=signal.sosfilt(signal.butter(2,75,'highpass',fs=SR,output='sos'),voice).astype(np.float32)
voice*=.79/max(.01,float(np.max(np.abs(voice))))
length=len(voice)
total=length/SR

def word_time(block, word):
    return next((x['start'] for x in timed[block]['words'] if x['text'].lower().strip('.,!?…:;')==word),timed[block]['start'])

events={'reveal':timed[5]['start'], 'crossing':timed[6]['start'],
        'dinner':timed[7]['start'], 'knock':word_time(8,'bate'),
        'caio_turn':word_time(10,'olha'), 'chair':word_time(10,'puxa'),
        'horn':timed[11]['start']+.15,'bus_move':word_time(11,'ônibus')+.5,
        'hand':timed[12]['start']+1, 'choice':timed[14]['start']}

rng=np.random.default_rng(20261020)
t=np.arange(length,dtype=np.float32)/SR
# Original restrained score: soft A-minor suspended chord, very slow modulation.
music=np.zeros(length,dtype=np.float32)
for freq,gain,phase in [(220,.011,.3),(261.6256,.006,1.1),(329.6276,.008,2.2),(440,.003,.8)]:
    music += gain*np.sin(2*np.pi*freq*t+phase)*(0.6+0.4*np.sin(2*np.pi*.07*t+phase))
fade=np.minimum(1,t/3)*np.minimum(1,(total-t)/3)
duck=1-.9*np.exp(-((t-events['chair'])/1.5)**2)
music*=fade*duck
sfx=np.zeros(length,dtype=np.float32)

def put(sound,when,gain=1):
    first=max(0,round(when*SR)); end=min(length,first+len(sound))
    if end>first: sfx[first:end]+=sound[:end-first]*gain

def noise(sec,lo,hi):
    a=rng.normal(0,1,round(sec*SR)).astype(np.float32)
    a=signal.sosfilt(signal.butter(2,[lo,hi],'bandpass',fs=SR,output='sos'),a)
    return (a/(max(.01,float(np.max(np.abs(a)))))).astype(np.float32)

wind=noise(total,160,1800)*(.007+.006*np.sin(t*.37)**2)
wind[:round(timed[2]['start']*SR)]*=1.5
sfx+=wind
engine_start=timed[4]['start']
engine_time=np.maximum(0,t-engine_start)
engine=(np.sin(2*np.pi*83*t)+.35*np.sin(2*np.pi*166*t))*.012
engine*=(t>engine_start)*np.minimum(1,engine_time/2)
engine*=1-.8*np.exp(-((t-events['dinner'])/9)**2)
sfx+=engine
for beat in range(3):
    nt=np.arange(round(.16*SR))/SR
    knock=(np.sin(2*np.pi*1050*nt)*np.exp(-nt*43)+.3*noise(.16,500,3400)*np.exp(-nt*45))*.14
    put(knock,events['knock']+beat*.31)
scrape=noise(1.3,220,3600)*np.sin(np.linspace(0,np.pi,round(1.3*SR)))**1.6*.09
put(scrape,events['chair']+.15)
ht=np.arange(round(.62*SR))/SR
horn=(np.sin(2*np.pi*174.61*ht)+.65*np.sin(2*np.pi*220*ht))*.072
horn*=np.minimum(1,ht/.04)*np.minimum(1,(.62-ht)/.12)
put(horn,events['horn'])
for when in np.arange(events['crossing']+.35,timed[7]['start']-.1,.42):
    ft=np.arange(round(.14*SR))/SR
    foot=(noise(.14,100,1900)*np.exp(-ft*28)+.25*np.sin(2*np.pi*155*ft)*np.exp(-ft*38))*.065
    put(foot,when)
put(noise(.22,900,4700)*np.sin(np.linspace(0,np.pi,round(.22*SR)))*.017,events['hand']+1.0)

def save(path,a):
    with wave.open(str(path),'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(a,-.98,.98)*32767).astype('<i2').tobytes())

for name,a in [('narracao',voice),('efeitos',sfx),('trilha',music),('mix-principal',voice+sfx+music),('mix-sem-musica',voice+sfx)]:
    save(WORK/f'{name}.wav',a)
    if name in ['narracao','efeitos','trilha']:
        subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(WORK/f'{name}.wav'),'-c:a','aac','-b:a','128k',str(ROOT/'public/audio'/f'{name}.m4a')],check=True)

scenes=[
 ('perda',0,2,'A perda','Lia procura o irmão e encontra terra lisa.'),
 ('abrigo',2,4,'Sobreviver','Outros vazios; abrigo em uma escola. Lia ajeita a mochila.'),
 ('partida',4,5,'A última partida','Motorista e sobreviventes aguardam. Lia entra na fila. Lote ainda vazio.'),
 ('retorno',5,6,'O retorno','Luz do outro lado da rua. Corte coincidente: o prédio reaparece. Lia reage.'),
 ('travessia',6,7,'A travessia','Lia atravessa com ciclo de pernas e braços, mochila presa.'),
 ('jantar',7,8,'O jantar','Caio sentado entre vizinhos; vapor discreto sobre a comida.'),
 ('vidro',8,10,'Ninguém responde','Lia levanta o braço e bate três vezes. Vizinhos não reagem.'),
 ('cadeira',10,11,'A cadeira vazia','Caio vira o rosto, alcança e desloca a cadeira vazia. Pausa.'),
 ('onibus',11,12,'A buzina','Motorista chama; ônibus avança pouco, ainda alcançável.'),
 ('dilema',12,14,'O custo','Lia alterna o olhar entre a porta fechada e o ônibus; mão hesita junto da maçaneta.'),
 ('escolha',14,18,'A decisão do público','As duas alternativas têm o mesmo peso; termina antes de Lia escolher.')]
scene_data=[]
for name,a,b,title,action in scenes:
    start=0 if a==0 else timed[a]['start']
    end=timed[b]['start'] if b<len(timed) else total
    scene_data.append({'id':name,'title':title,'start':round(start*FPS),'end':round(end*FPS),
                       'startSeconds':start,'endSeconds':end,'action':action})
metadata={'fps':FPS,'duration':total,'durationInFrames':math.ceil(total*FPS),
          'voice':'Microsoft Maria Desktop (Windows, pt-BR, feminina, síntese local)',
          'segments':timed,'captions':captions,'events':events,'scenes':scene_data}
(ROOT/'src/timeline.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'docs/temporizacao-real.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
def stamp(value):
    ms=round(value*1000); h,ms=divmod(ms,3600000); m,ms=divmod(ms,60000); s,ms=divmod(ms,1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'
lines=[]
for i,c in enumerate(captions,1):
    words=c['text'].split(); best=min(range(1,len(words)),key=lambda n:abs(len(' '.join(words[:n]))-len(' '.join(words[n:])))) if len(words)>1 else 1
    text=c['text'] if len(c['text'])<=29 else ' '.join(words[:best])+'\n'+' '.join(words[best:])
    lines.append(f'{i}\n{stamp(c["start"])} --> {stamp(c["end"])}\n{text}\n')
(ROOT/'renders/episodio-01.srt').write_text('\n'.join(lines),encoding='utf-8')
report={'duration':total,'frames':metadata['durationInFrames'],'voice_peak':float(np.max(np.abs(voice))),
        'main_peak':float(np.max(np.abs(voice+sfx+music))),'sample_rate':SR,'captions':len(captions),
        'events':events}
(ROOT/'docs/verificacao-audio.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
