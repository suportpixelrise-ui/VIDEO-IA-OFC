# Revisão de entrega — episódio 1

## Resultado existente

- Principal: `renders/episodio-01-principal.mp4`, H.264/AAC, 1080×1920, 30 fps, aproximadamente 119,15 segundos.
- Alternativa sem música: `renders/episodio-01-sem-musica.mp4`, mantendo o mesmo vídeo, locução e efeitos.
- Legendas externas: `renders/episodio-01.srt`; 31 blocos, além das legendas queimadas na imagem.
- Fonte completa: onze cenas em Remotion, atlas de personagens, fundos, props, áudio separado, roteiro e memória da história.

## Verificações realizadas

- TypeScript e ESLint aprovados.
- Quadros-chave renderizados e conferidos visualmente; ajustes de apoio da fila, escala, enquadramento da fachada, alcance ao vidro, cadeira e leitura das alternativas.
- Abertura mostra Lia diante do lote vazio. O prédio não é exibido antes da interrupção da partida.
- Referência cartoon aprovada preservada; sem modelo 3D, fotorrealismo ou ficha de personagens inserida no vídeo.
- Mochila de Lia permanece vermelha; Caio mantém camiseta cinza; Motorista mantém camisa azul e cabelo/barba grisalhos.
- Batidas, gesto da cadeira, buzina e aproximação da mão têm eventos sincronizados na linha do tempo.
- Porta permanece fechada; ônibus segue próximo; as opções A/B não têm uma vencedora.
- Duas versões decodificadas integralmente por FFmpeg sem erros reportados.
- As duas versões preservam os mesmos 3.574 frames; o hash SHA-256 do fluxo de vídeo é idêntico. Metadados e hashes em `verificacao-video.json`.
- Reprodução integral automatizada no Chrome, em velocidade normal e com som habilitado; quadros amostrados e informações em `verificacao-playback.json`.
- Áudio sem clipping no mix fonte: pico medido abaixo de 0,81 na escala digital de 0 a 1. Trilha e efeitos ficam separados da voz para edição.

## Limites declarados

Esta é **animação limitada 2D por recortes articulados**, com poses e objetos em camadas. Os cenários são pinturas estáticas. Não é desenho integral quadro a quadro.

A voz é **Microsoft Maria Desktop**, síntese local feminina em pt-BR. A interpretação e a naturalidade não equivalem a uma gravação de atriz. A revisão técnica e a reprodução automatizada não substituem a avaliação humana da locução. Uma gravação humana pode ser substituída depois, com nova medição e sincronização.

As marcas de palavras do SAPI foram ajustadas à duração audível efetiva de cada bloco porque seu relógio apresentou divergência. As legendas usam blocos de leitura, sem destaque palavra por palavra.

Não houve acesso a serviços pagos, contratação de voz, conexão de contas de mídia, postagem em rede social ou votação real. O GitHub recebe o pacote editável; os MP4s exportados permanecem locais.

## Continuidade

Último estado: Lia na calçada, junto da porta fechada, entre Caio e o ônibus. Caio continua sentado; cadeira vazia deslocada; Motorista no ônibus próximo. A causa do fenômeno é desconhecida. A votação está pendente e nenhuma consequência vencedora foi estabelecida.
