# Vídeos no Codex — configuração em 19/10/2026

Esta configuração foi feita sem conectar contas, criar chaves, publicar conteúdo ou contratar serviços.

## Pacotes e localização

| Pacote | Resultado |
|---|---|
| Instagram Skills | Instalado em `C:\Users\Michael\.codex\skills\instagram-skills`. Contém nove skills especializadas e o documento principal de roteamento. Modo manual/rascunho validado. |
| Remotion oficial | Já estava habilitado pelo plugin `remotion`, versão 4.0.534, com 12 skills. Mantido sem outra instalação. O repositório consultado já declara 4.0.537; isso é uma atualização futura do plugin, não uma dependência para os testes locais. |
| Video Shotcraft | Instalado em `C:\Users\Michael\.codex\skills\video-shotcraft`, com cartões, código dos demos, template, texturas, áudio e Workbench. Cópia local adaptada para Windows. |

As skills novas estarão disponíveis no próximo turno. Se não aparecerem, abra uma nova conversa ou reinicie o aplicativo. Pode pedir pelo nome da skill ou descrever a tarefa.

Versões de origem registradas:

- Instagram: versão 1.0.32; commit `6a124481d0ebe9b6d3ac1323ed2a2abc40c7e1d7`.
- Video Shotcraft: commit `43bd349a136651865ecfa6ea1cf012f6e957d304`.
- Remotion consultado: commit `039e8a2fc78b67efc228d5645367838b85818a1c`; plugin instalado mantido em 4.0.534.
- O template e o Workbench do Shotcraft usam Remotion **4.0.484**, fixado pelo próprio projeto. Versão de biblioteca e versão das skills são coisas distintas; não atualizei as dependências do template para outra versão durante a instalação.

## Ferramentas do Windows

Instalação portátil em `C:\Users\Michael\.codex-video-tools`, sem administrador:

- Node.js 24.22.0 LTS, npm 11.19.1 e npx.
- FFmpeg e ffprobe 9.0.2, build Essentials da Gyan, indicada pela página oficial do FFmpeg.
- Ambiente Python 3.12.14, com `requests`, `python-dotenv`, `PyYAML`, `uv`, `librosa` e `scipy`.
- Chrome Headless Shell do Remotion no projeto `shotcraft-demo`.
- Puppeteer instalado no exemplo para captura de páginas; pode reutilizar o Chrome Headless já baixado, sem baixar outro navegador.

Os downloads ZIP do Node e FFmpeg foram conferidos com os SHA-256 publicados pelos respectivos distribuidores. Registros em `.setup-video/tools.json` e `C:\Users\Michael\.codex-video-tools\installation.json`. O Python reaproveita o runtime fornecido pelo Codex; se o aplicativo substituir esse runtime e o ambiente deixar de abrir, será necessário recriar o ambiente Python.

As pastas das ferramentas foram acrescentadas ao PATH do usuário, preservando as entradas anteriores. Terminais já abertos não recebem a alteração automaticamente. Neste workspace, carregue:

```powershell
. .\video-env.ps1
```

O arquivo `AGENTS.md` orienta o Codex a carregar esse ambiente. Use `npm.cmd` e `npx.cmd` em PowerShell para evitar depender da política de execução dos wrappers `.ps1`. Não alterei a política de execução do Windows.

## Como usar Instagram Skills

Exemplos para enviar ao Codex:

- “Use Instagram Skills para planejar uma semana de Reels sobre inteligência artificial, em português, só com rascunhos.”
- “Use $ig-caption-writer para criar uma legenda com gancho, CTA e hashtags para este vídeo: [caminho].”
- “Use $ig-carousel-planner para planejar um carrossel de sete slides sobre [tema].”
- “Use $ig-humanizer para revisar esta legenda: [texto].”

As outras skills são `ig-hook-extractor`, `ig-hashtag-strategist`, `ig-content-planner`, `ig-repurposer`, `ig-profile-optimizer` e `ig-audience-insights`. Informe nicho, público, objetivo, exemplos de tom e mídia quando aplicável.

O pacote prepara textos e planos; a mídia deve ser fornecida ou produzida separadamente. Você publica manualmente. Publora, Apify e Pixfaro não foram configurados. Sem Apify, forneça dados e exemplos para análise; a instalação sozinha não dá acesso a métricas reais ou pesquisa autenticada. O perfil de voz e marca continua em branco para você preencher quando tiver um projeto.

## Como usar Remotion

Exemplos para enviar ao Codex:

- “Use $remotion-create para criar um Reel de 15 segundos, 1080×1920, sobre [tema], usando os arquivos desta pasta. Abra o preview.”
- “Use $remotion-captions para adicionar legendas ao vídeo.”
- “Use $remotion-render para exportar a composição aprovada em MP4.”

Para abrir o exemplo já preparado:

```powershell
. .\video-env.ps1
Set-Location .\shotcraft-demo
npm.cmd run dev -- --no-open
```

O terminal informa a URL do Studio. Para exportar o template completo:

```powershell
npm.cmd run render -- --concurrency=1
```

O template é Ink Press, em 1920×1080, 30 fps, aproximadamente 36 segundos. Novos Reels verticais precisam de composição própria e ajuste de layout.

## Como usar Video Shotcraft

Exemplos para enviar ao Codex:

- “Use $video-shotcraft para fazer um vídeo do produto em [pasta/URL]. Escolho criação autônoma. Use só recursos locais, sem serviços pagos.”
- “Use $video-shotcraft com o template Ink Press para [produto].”
- “Use o cartão spotlight-hero-card do Video Shotcraft para animar esta captura de tela.”

O pacote oferece template, criação autônoma e criação colaborativa. Nomear o modo no pedido evita uma pergunta inicial de escolha. Forneça produto, duração, formato, textos, logo e capturas ou um projeto acessível.

Galeria de movimentos: https://vincentwei1021.github.io/video-shotcraft/. Os MP4s da galeria não foram baixados; os cartões, demos, índice da biblioteca, texturas e áudio necessários à produção foram instalados.

Para abrir o Workbench ligado ao exemplo, a partir da raiz deste workspace:

```powershell
. .\video-env.ps1
node "$env:USERPROFILE\.codex\skills\video-shotcraft\workbench\scripts\open.mjs" (Join-Path $PWD 'shotcraft-demo') --no-open
```

A URL padrão é http://localhost:5198. Os ajustes locais estão documentados no `WINDOWS-SETUP.md` da skill: junctions NTFS no lugar de links Unix, normalização de caminhos, execução dos CLIs via Node e cópia de mídia via Node no lugar de `rsync`. As cópias originais dos arquivos ajustados terminam em `.upstream`. Uma reinstalação pode sobrescrever essas adaptações.

O Workbench ficou aberto em segundo plano ao final da configuração. Enquanto ele estiver ativo, basta abrir a URL. O script original protege processos em uso e pode recusar uma nova ligação na mesma porta no Windows; para ligar outro projeto sem interromper o atual, acrescente `--port 5199`.

## O que continua opcional

- Nenhuma conta, chave de API ou serviço de publicação/geração está configurado.
- Capturas exigem uma página ou projeto acessível. O teste local não exige login em site algum.
- Para novos projetos, instale suas dependências na própria pasta. As skills instaladas globalmente não substituem o `node_modules` de cada projeto.
- A exportação de projetos JianYing/CapCut CN não foi validada neste Windows; o próprio repositório informa validação principal em macOS.
- Os botões de exportação completa do Workbench não foram testados de ponta a ponta. A exportação MP4 foi validada pelo CLI do Remotion.

## Verificação realizada

- Formato YAML, nove skills especializadas, nomes únicos, importação das bibliotecas Python, parser de URL e modo manual do Instagram: aprovados.
- Ferramentas de linha de comando e `pip check`: aprovados; versões e dependências Python registradas em `.setup-video/`.
- Análise de oito segundos da faixa local `bgm-tech-house.mp3`: carregamento, estimação de tempo e detecção de batidas aprovados.
- Captura de uma página local com Puppeteer/Chrome Headless: aprovada, sem conta e sem acesso a site externo.
- Frame 150 do template: renderizado em `shotcraft-demo/out/qa/frame150.png`.
- Trecho de 15 frames: exportado em `shotcraft-demo/out/teste-instalacao.mp4`; `ffprobe` confirmou H.264, AAC, 480×270, 30 fps; FFmpeg conseguiu decodificar o arquivo. É um teste curto, não um vídeo de produção finalizado.
- Workbench: TypeScript e build Vite aprovados; servidor local iniciado e projeto de exemplo ligado. O navegador confirmou HTTP 200, interface carregada, unidades do template disponíveis e nenhum erro JavaScript. Captura em `shotcraft-demo/out/qa/workbench.png`.

O sandbox deste chat impediu a primeira tentativa de empacotamento/renderização e uma tentativa de iniciar o navegador de teste. Os testes de renderização e captura funcionaram com a execução autorizada fora do sandbox. Isso pode voltar a exigir permissão ao executar esses comandos pelo Codex; em um terminal normal do Windows, essa restrição específica do chat não se aplica.

## Fontes

- [Instagram Skills](https://github.com/sergebulaev/instagram-skills)
- [Skills oficiais do Remotion](https://github.com/remotion-dev/skills)
- [Video Shotcraft](https://github.com/Vincentwei1021/video-shotcraft)
- [Skills no Codex — documentação oficial](https://learn.chatgpt.com/docs/build-skills)
- [Node.js](https://nodejs.org/en/download) e [distribuição Windows do FFmpeg](https://www.gyan.dev/ffmpeg/builds/)
