# Fire Emblem: Fortune's Weave — Tradução PT-BR (fã)

Tradução não oficial de **Fire Emblem: Fortune's Weave** (Nintendo Switch 2) para português do Brasil.

- Todo o texto do jogo: menus, história das quatro rotas, apoios, histórias paralelas, itens, habilidades, missões,
  tutorial e dicas — 71.140 textos em 522 arquivos.
- Falas dirigidas ao jogador seguem o gênero escolhido no jogo («vivo|viva», «Prometido|Prometida»), usando o
  código nativo de troca de gênero do próprio jogo.
- Fontes de título ajustadas para exibir acentos (ã, õ, ç, é...).

## Download e instalação

Baixe o `.zip` em [Releases](../../releases) e veja o `LEIA-ME.txt` dentro dele.

Resumo: copie a pasta `romfs` do zip por cima da pasta `romfs` do jogo extraído (exefs + romfs), ou coloque-a como mod
LayeredFS em `user/load/04007EF01F8AE000/<nome do mod>/romfs`. Testado no emulador eden-fefw v1.07.

Este repositório não contém arquivos do jogo. Para gerar o patch você precisa do seu próprio dump.

## Estrutura

| Pasta / arquivo | Conteúdo |
|---|---|
| `pt/NNN.json` | A tradução: `{"<arquivo>\t<índice>": "texto"}` |
| `tools/msbt.py` | Leitura e escrita de MSBT (UTF-8) comprimido com zstd; converte `«m\|f»` no código de gênero |
| `tools/fcpx.py` | Gera as cadeias de fonte (`.bfcpx`) com fallback para a fonte com acentos |
| `tools/extract.py` | Extrai o texto em inglês do dump para `batches/` |
| `tools/check.py` | Valida um lote: ids, códigos `{{...}}`, tags `<...>` e quebras de linha |
| `tools/unify.py` | Padroniza termos entre lotes |
| `tools/build.py` | Gera `out/romfs` (e instala com `--install`) |
| `BRIEF.md` | Guia de estilo e glossário |

## Gerar a partir do seu dump

```
# copie romfs/Msg/USen/*.msbt.zst do jogo para src/USen e romfs/Font/*.bfcpx para src/Font
pip install zstandard
python -I tools/extract.py          # opcional: recria batches/ (texto em inglês)
python -I tools/build.py            # gera out/romfs
```

Ajuste o caminho `GAME` em `tools/build.py` para usar `--install`.

## Créditos

Tradução feita com auxílio de IA (Claude) e revisada por consistência de termos e gênero.
Fire Emblem é marca da Nintendo / Intelligent Systems. Projeto de fã, sem fins lucrativos.
