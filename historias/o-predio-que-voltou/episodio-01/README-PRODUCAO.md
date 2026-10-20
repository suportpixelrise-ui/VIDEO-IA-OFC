# O Prédio que Voltou — episódio 1: A cadeira vazia

Episódio vertical em animação limitada cartoon 2D, baseado nas referências aprovadas do projeto. Duração: **119,12 segundos**, 1080×1920, 30 fps. Não houve aceleração da locução para forçar 100 segundos.

Lia perdeu o contato com o irmão quando o prédio dele desapareceu. Na hora de deixar o abrigo, ela vê o prédio de volta e encontra Caio jantando. O convite da cadeira vazia compete com a última chance de evacuação. O episódio termina com A/B, sem uma escolha e sem resultado de votação.

## Arquivos de produção

- `docs/narracao.txt`: texto limpo, separado de direção.
- `docs/prompt-mestre-original.txt`: especificação recebida.
- `docs/personagens-e-geografia.md`: referência, personagens, técnica e limites.
- `docs/roteiro-de-cenas.md`: tempos reais, ações e descrições por plano.
- `docs/prompts-artes.md` e `docs/artes-manifesto.json`: prompts de produção e rastreio das artes.
- `docs/continuidade.json`: memória da história e votação ainda pendente.
- `src/timeline.json`: duração medida, legendas e eventos de sincronização.
- `src/scenes/`: onze cenas editáveis; `src/stage.tsx`: personagens articulados, recortes e elementos comuns.
- `public/assets/`: referências preservadas e artes derivadas com alpha.
- `public/audio/`: locução, efeitos e trilha separados em AAC.
- `renders/episodio-01.srt`: legendas externas.
- `renders/episodio-01-principal.mp4`: exportação principal local, com voz, efeitos, música e legendas.
- `renders/episodio-01-sem-musica.mp4`: exportação local sem música, preservando voz e efeitos.
- `renders/qa/`: quadros-chave de verificação.

Os MP4s renderizados e arquivos intermediários são mantidos localmente e ignorados no Git. O repositório contém os materiais de produção necessários para reabrir e exportar o projeto. Não houve publicação em redes sociais ou conexão de contas de serviços de mídia.

## Abrir a prévia

No computador configurado neste workspace:

```powershell
# Na raiz VIDEOS IA:
. .\video-env.ps1
Set-Location .\historias\o-predio-que-voltou\episodio-01
npm.cmd run dev -- --no-open --port=3005
```

Abra `http://localhost:3005/ACadeiraVazia`. O servidor já foi iniciado durante a produção. Em outro computador com Node compatível, execute `npm ci` antes de iniciar. Se não houver um Chrome indicado em `PUPPETEER_EXECUTABLE_PATH`, o Remotion usa seu fluxo de instalação do navegador.

## Exportar

```powershell
npx.cmd remotion render src/index.ts ACadeiraVazia renders/episodio-01-principal.mp4 --concurrency=2 --crf=20
```

Para a versão sem música, use a mesma composição com as props `{"music":false}` em um arquivo JSON, ou remuxe o vídeo já renderizado com `.work/audio/mix-sem-musica.wav`:

```powershell
ffmpeg -i renders/episodio-01-principal.mp4 -i .work/audio/mix-sem-musica.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -movflags +faststart renders/episodio-01-sem-musica.mp4
```

## Técnica, voz e som

Personagens em atlas raster derivados da folha aprovada; recortes articulados para braços, pernas e rosto. A batida no vidro, a mudança de olhar, o alcance de Caio e o movimento da cadeira são animados por frames. Fundos são desenhos estáticos, sem personagens 3D. Não é animação tradicional integral quadro a quadro.

Voz: **Microsoft Maria Desktop**, feminina, pt-BR, síntese local do Windows. É uma locução sintética editável; não é gravação de atriz nem voz neural contratada. Os blocos foram medidos no WAV real. O relógio de palavras do SAPI apresentou divergência; as marcas foram ajustadas ao intervalo audível medido de cada bloco para que as legendas não ultrapassem o áudio.

Trilha e efeitos são síntese original e determinística em `scripts/preparar_audio.py`: cama discreta em lá menor, vento, motor, passos, três batidas, atrito da cadeira, buzina e ruído curto junto à maçaneta. Música reduzida no gesto da cadeira. Nenhuma faixa ou voz paga foi adquirida.

Para trocar a narração por gravação humana, medir o novo áudio e refazer a temporização antes de exportar; as ações e as legendas dependem desses tempos.

## Estado da história

- A — Entrar no prédio e tentar buscar o irmão.
- B — Pegar o ônibus e seguir com os sobreviventes.
- Nenhuma opção foi escolhida. Não há vencedora nem contagem inventada.
- A causa dos desaparecimentos permanece sem explicação.

Consulte `docs/continuidade.json` antes de escrever o episódio seguinte. Os dois caminhos devem gerar consequências distintas.
