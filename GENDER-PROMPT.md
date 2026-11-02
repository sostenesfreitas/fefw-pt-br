# Revisão de gênero do jogador (Fire Emblem: Fortune's Weave PT-BR)

O jogador (o Mediador / o Prometido) pode ser homem ou mulher. O jogo tem um código nativo que troca a palavra conforme o
gênero escolhido. Na tradução ele é escrito assim: `«forma masculina|forma feminina»`, por exemplo:

- `Você está «vivo|viva»!`
- `«O|A» Prometid«o|a» chegou.` ou `«O Prometido|A Prometida» chegou.`
- `<ICA>«Obrigado|Obrigada».` (fala do próprio jogador)
- `Prazer em «revê-lo|revê-la».`

Pasta do projeto: C:\Users\soste\Documents\fefw-pt-br. Leia BRIEF.md (glossário e estilo).

## Tarefa

Você recebe `gender\NN.json`: `{"<arquivo>\t<índice>": {"en": inglês, "pt": tradução atual, "uses"/"eues"/"eufr": a mesma
linha em espanhol/francês, onde `«m|f»` mostra os pontos em que a localização oficial troca pelo gênero do jogador}`.

Para cada linha:
1. Decida se alguma palavra se refere ao **jogador** (fala dirigida a ele, sobre ele, ou dita por ele nas escolhas
   `<ICA>/<ICB>/<NCA>/<NCB>`). As versões em espanhol/francês mostram onde a troca é necessária; use-as como guia,
   mas a decisão é sobre o português.
2. Se houver concordância de gênero com o jogador, aplique `«m|f»` em cada palavra marcada (adjetivos, particípios,
   artigos, pronomes -lo/-la, substantivos como Prometido/Mediador, Bem-vindo). Mantenha o resto da frase idêntico.
3. Se a frase já for neutra ou falar de outra pessoa (ex.: Dietrich, Theodora), deixe como está.
4. Não mexa em códigos `{{...}}`, tags `<...>`, nem no número de `\n`. Cada `«m|f»` tem exatamente uma `|`.
   Mantenha `«` e `»` (aspas angulares) só para essa troca; não use `«»` como aspas comuns.
5. Os títulos fixos do glossário viram par: Prometido → «Prometido|Prometida», Mediador → «Mediador|Mediadora»,
   Luminoso → «Luminoso|Luminosa», Arauto fica Arauto (invariável).

Escreva `gender\out\NN.json` como `{"<arquivo>\t<índice>": "PT final"}` com TODAS as ids do arquivo de entrada
(inclusive as que não mudaram). UTF-8, ensure_ascii=False, indent=1. Use nomes de arquivos temporários próprios.

Responda com: quantas linhas mudaram, quantas ficaram iguais, e 5 exemplos antes→depois.
