# Artes derivadas — prompts e origem

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
