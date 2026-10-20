from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'src/timeline.json').read_text(encoding='utf-8'))
docs=ROOT/'docs'
continuity={
 'serie':'O Prédio que Voltou','episodio':1,'titulo':'A cadeira vazia',
 'referencia_oficial':'../../referencias/personagens-cartoon-2d-aprovado.png',
 'fatos':['Os desaparecimentos começaram há doze dias.','O prédio de Caio sumiu à noite e deixou terra lisa.','Lia perdeu contato com o irmão e se refugiou na escola.','O abrigo está sendo evacuado no último ônibus.','O prédio reaparece no mesmo terreno.','Caio e vizinhos estão jantando; a comida está quente.','Não respondem às batidas no vidro.','Caio olha para Lia e puxa a única cadeira vazia.','O ônibus começa a andar e continua alcançável.','A porta permanece fechada; Lia não escolhe.'],
 'lia_sabe':['O prédio estava ausente e voltou.','Caio está visível e a convidou com o gesto da cadeira.','Demorar pode custar a evacuação.'],
 'misterios':['Causa dos desaparecimentos.','Onde estiveram as pessoas.','Por que não respondem às batidas.','Por que parecem esperar por Lia.','Quanto do mundo ainda existe.'],
 'estado_final':{'Lia':'Calçada junto à entrada fechada, olhando entre prédio e ônibus. Mochila vermelha presente.','Caio':'Sentado à mesa, no centro entre os vizinhos.','Motorista':'No ônibus ainda próximo.','cadeira':'Vazia, deslocada após o gesto de Caio.','porta':'Fechada.'},
 'votacao':{'estado':'ainda_nao_realizada','vencedora':None,'contagens':None,
            'A':'Entrar no prédio e tentar buscar o irmão.','B':'Pegar o ônibus e seguir com os sobreviventes.'},
 'direcoes_possiveis_nao_canonicas':{'A':'Contato com Caio e custo de perder a evacuação.','B':'Fuga com os sobreviventes, separação de Caio e informações dos passageiros.'},
 'consequencia_vencedora_estabelecida':None,
 'proibicoes_de_continuidade':['Não afirmar morte, monstros ou viagem no tempo.','Não abrir a porta no episódio 1.','Não retirar a mochila sem ação.','Não inventar votação.','Não fazer A e B convergirem imediatamente.']}
(docs/'continuidade.json').write_text(json.dumps(continuity,ensure_ascii=False,indent=2),encoding='utf-8')

characters='''# Personagens e referência

Referência obrigatória: `../../referencias/personagens-cartoon-2d-aprovado.png`, aberta e conferida na produção. Lia está à esquerda, Caio ao centro, Motorista à direita. Versões realistas ou 3D não foram usadas. Os desenhos gerados são derivados dessa folha, preservada sem alterações.

| Personagem | Identidade preservada | Atuação nesta versão |
|---|---|---|
| Lia, adulta, ~24 anos | Pele parda; olhos grandes; sobrancelhas fortes; cabelo castanho-escuro ondulado, rabo baixo e mechas soltas; jaqueta oliva, blusa bege, calça escura, tênis claros, mochila vermelha | Busca, preocupação, esperança, caminhada por articulação de recortes, braço que bate no vidro, mudança de olhar, hesitação junto à maçaneta |
| Caio, jovem adulto, ~20 anos | Pele parda; cabelo curto castanho-escuro ondulado; camiseta cinza lisa; calça azul-escura; tênis claros | Sentado; mudança de pose do rosto; alcance do braço e deslocamento da cadeira vazia |
| Motorista, adulto mais velho, ~50 anos | Rosto largo, cabelo grisalho, bigode/barba simplificados, camisa azul, calça escura, sapatos marrons | Espera e gesto de urgência; depois aparece na janela do ônibus |

Figurantes: duas pessoas na evacuação e duas à mesa, com desenho mais simples e identidades distintas dos protagonistas. Os vizinhos permanecem sem responder às batidas. Não há animação labial ligada à narradora.

## Geografia fixa

Escola e ônibus de um lado da rua; lote e prédio retornado do outro. A porta marrom fica imediatamente à esquerda da janela iluminada, como na referência do prédio. A área vazia e o prédio usam enquadramentos correspondentes. O plano próximo da fachada preserva essa relação. A ação termina com a porta fechada e o ônibus próximo.

## Técnica e limites

Animação limitada 2D: atlas de recortes raster com alpha, partes articuladas, poses de rosto, gestos e objetos em camadas, dirigidos por frames no Remotion. Cenários são pinturas estáticas; profundidade vem de composição e mudanças discretas de plano. Não se trata de animação tradicional desenhada integralmente quadro a quadro, nem geração de vídeo por IA em um único passe. A locução é sintética, gerada localmente pelo Windows; a naturalidade pode ser aprimorada com uma gravação humana futura, sem alterar o texto ou a montagem às cegas.
'''
(docs/'personagens-e-geografia.md').write_text(characters,encoding='utf-8')

rules={
 'perda':('Início dos desaparecimentos','Rua e lote vazio','Plano geral seguido de reação próxima','Lia chega procurando Caio; para diante da terra lisa.','Expectativa → preocupação','Passos curtos, varredura com cabeça/olhar, mudança de pose; câmera aproxima no corte.','Vento discreto. Sem mostrar o prédio retornado.'),
 'abrigo':('Presente','Rua e escola-abrigo','Cidade vazia e interior com colchões/mochilas','Lia acompanha os sobreviventes e ajeita a mochila.','Cansaço → resignação','Pequena mudança de braço e postura; figurantes discretos.','Ambiente baixo; voz principal.'),
 'partida':('Presente','Escola, ônibus e lote ainda vazio','Plano aberto com geografia legível','Lia dá um passo para entrar na fila; percebe luz à direita.','Resignação → atenção','Motorista gesticula; Lia para e vira a cabeça.','Motor; luz apenas no fim. Não revelar prédio antes do plano seguinte.'),
 'retorno':('Presente','Mesmo lote','Enquadramento correspondente antes/depois','O prédio reaparece; Lia reconhece a janela.','Surpresa → esperança','Corte de placas coincidentes, mudança de rosto e direção da cabeça.','Mudança discreta da cama sonora; sem portal ou explosão.'),
 'travessia':('Presente','Rua entre escola e prédio','Plano geral com deslocamento lateral','Lia atravessa para alcançar a janela.','Esperança → urgência','Braços e pernas articulados em ciclo, corpo acompanha o deslocamento; mochila sempre presa.','Passos sincronizados; ônibus fica próximo.'),
 'jantar':('Presente','Interior do térreo','Plano de mesa com Caio e dois vizinhos','Pessoas jantam normalmente; cadeira vazia visível.','Esperança do reencontro → estranhamento','Vapor animado, Caio sentado; vizinhos não reagem.','Voz e ambiente contido, sem diálogos.'),
 'vidro':('Presente','Fachada junto à janela','Lia em primeiro plano, interior à direita','Lia ergue o braço, bate três vezes e aguarda.','Esperança → dúvida','Antecipação do ombro, punho em pose e três ciclos curtos; depois baixa parcialmente o braço.','Três batidas alinhadas ao gesto; ninguém responde.'),
 'cadeira':('Presente','Mesmo interior','Plano firme da mesa e cadeira','Caio vira o rosto, alcança e desloca a cadeira vazia.','Calma familiar → convite ambíguo','Pose do rosto muda; braço alcança e acompanha a cadeira; pausa após o movimento.','Atrito da madeira destacado e música reduzida.'),
 'onibus':('Presente','Rua e ônibus ainda perto','Plano que retoma a possibilidade de fuga','Buzina chama Lia; ônibus começa a rolar devagar.','Dúvida → urgência','Lia muda a direção do olhar; deslocamento pequeno do ônibus.','Buzina e motor; não tornar a fuga impossível.'),
 'dilema':('Presente','Calçada, porta e vista do ônibus','Plano próximo da protagonista e maçaneta','Lia aproxima a mão da entrada sem abri-la e volta o olhar ao ônibus.','Desejo de reencontro → conflito','Braço avança com pausa; cabeça alterna em direção à fuga.','Voz explica custos; porta não gira, maçaneta não destranca.'),
 'escolha':('Presente','Mesmo lugar','Lia, porta fechada e duas alternativas','Apresentar A/B, sem decisão e sem resultado.','Indecisão sustentada','Respiração discreta e olhar alternado; texto simultâneo com peso igual.','Som contido; chamada apenas para comentar A ou B.')}
lines=['# Roteiro de planos e descrições de produção','',f'Duração real: {d["duration"]:.2f} s; 1080×1920; 30 fps. Os tempos seguem a locução local medida, sem acelerar a voz para caber em 100 segundos.','',
 'Regra comum a todos os planos: usar a folha `personagens-cartoon-2d-aprovado.png` como referência de identidade e estilo; cabeças grandes, corpos simplificados, olhos/sobrancelhas expressivos, contornos escuros, cores chapadas e sombras simples. Lia mantém jaqueta oliva, mochila vermelha, cabelo ondulado com rabo baixo; Caio mantém camiseta cinza e cabelo curto ondulado; Motorista mantém camisa azul, cabelo/barba grisalhos. Sem 3D, fotorealismo, violência gráfica ou texto gerado dentro da arte.','']
for i,scene in enumerate(d['scenes'],1):
    temporal,location,shot,action,emotion,motion,sound=rules[scene['id']]
    lines += [f'## {i:02d} — {scene["title"]}', '',f'- Tempo: {scene["startSeconds"]:.2f}–{scene["endSeconds"]:.2f} s ({scene["end"]-scene["start"]} frames).',f'- Momento: {temporal}. Local: {location}.',f'- Enquadramento: {shot}.',f'- Ação principal: {action}',f'- Expressão: {emotion}.',f'- Movimento: {motion}',f'- Som e restrição: {sound}', '- Atmosfera: exterior frio e legível; interior doméstico quente, conforme as referências. Tipografia adicionada na montagem.',
              f'- Prompt de animação utilizável: “Plano {i:02d}, cartoon 2D da folha aprovada. {location}. {shot}. {action} {emotion}. {motion} {sound} Preservar rosto, proporções, figurino e mochila. Sem transformação monstruosa, texto na imagem ou resolução da escolha.”','']
(docs/'roteiro-de-cenas.md').write_text('\n'.join(lines),encoding='utf-8')

prompts='''# Artes derivadas — prompts e origem

Modo usado: ferramenta integrada **image_gen**, com referências locais anexadas. Nenhuma API paga externa ou chave foi configurada. Os PNGs finais estão em `public/assets/`; o manifesto relaciona os nomes aos arquivos de geração originais. As artes de referência aprovadas permanecem em `../../referencias/`.

## Prompts de produção finais

- **lia-rig.png** — Atlas transparente 3×4 de Lia da coluna esquerda da folha aprovada. Três cabeças: busca, preocupação, surpresa/esperança; tronco oliva/bege com cintura escura; mochila vermelha; punho de bater; braços e pernas separados. Preservar face, cabelo ondulado/rabo baixo, roupas e tênis. Peças opacas, alpha no fundo, sem texto, sem personagem montado.
- **caio-rig.png** — Atlas transparente 3×4 de Caio da coluna central. Três poses calmas de cabeça/olhar, tronco de camiseta cinza lisa, braços/mãos, pernas/calçados. Não monstruoso; preservar identidade e proporções; peças separadas com margens, fundo alpha.
- **motorista-rig.png** — Atlas transparente 3×4 do homem mais velho da coluna direita. Cabeças cansada/urgente/frontal, camisa azul e cintura, braços/gesto de espera, pernas/sapatos. Preservar cabelo e barba grisalhos, rosto largo e desenho cartoon. Sem texto.
- **rua-vazia-vertical.png** — Adaptar a rua aprovada para 9:16: escola creme com portão verde à esquerda, terra lisa vazia à direita, rua ao centro, postes e casas brasileiras contemporâneas. Entardecer frio legível, poucos sinais de abandono recente. Sem pessoas, ônibus, prédio no lote, portal ou título.
- **rua-predio-vertical.png** — Editar somente o lote da placa vertical anterior, restaurando o prédio cinza-azulado da referência, porta marrom à esquerda da janela quente do térreo. Manter câmera, escola, rua, céu, árvores e perspectiva. Sem pessoas ou fenômeno adicional.
- **jantar-vertical.png** — Adaptar a sala aprovada para 9:16, com janela e porta, paredes bege/verde, luminária laranja e mesa de madeira. Dois vizinhos distintos nas pontas, lugar central traseiro reservado ao Caio animado; lugar frontal sem cadeira para receber o objeto animado. Comida sem vapor pintado, para animar em edição. Sem protagonistas embutidos ou texto.
- **cadeira.png** — Uma única cadeira vazia de madeira, igual às da sala, em três-quartos, com quatro pernas e encosto retangular, contornos escuros e cores chapadas. Sem sala, mesa, pessoas, palavras ou sombra de chão; fundo alpha.
- **onibus.png** — Retirar fundo e sombra do ônibus aprovado, preservando veículo amarelo, faixa verde desaturada, rodas, bancos, vidros, porta e ângulo. Não criar logotipo, letras ou motorista. Fundo alpha, ônibus completo.
- **sobreviventes.png** — Atlas de dois adultos secundários diferentes dos protagonistas: mulher de cabelo preto curto, casaco azul e bolsa de lona; homem de cabeça raspada, blusa lilás e cobertor. Roupas discretas, corpo inteiro, mesma linguagem gráfica, fundo alpha, sem cenário ou texto.
- **fachada-proxima.png** — Plano vertical próximo da fachada do prédio retornado. Paredes continuam além do topo/lado do quadro e encontram a calçada; porta marrom fechada imediatamente à esquerda da janela quente; escola visível à esquerda ao fundo. Placa final vazia, sem pessoas. A correção final removeu integralmente a mulher que surgiu na primeira variação, reconstruindo o cenário e preservando todo o restante.

Os atlas são consumidos por recortes CSS no Remotion. O script de preparação lê o canal alpha para localizar as peças e grava metadados; ele não redesenha nem altera os pixels das artes.
'''
(docs/'prompts-artes.md').write_text(prompts,encoding='utf-8')
print('Personagens, geografia, roteiro de 11 cenas, prompts e continuidade documentados.')
