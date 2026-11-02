# Instruções para o agente tradutor (um grupo de lotes por agente)

Você traduz lotes da localização PT-BR de Fire Emblem: Fortune's Weave (inglês → português do Brasil).
Pasta do projeto: C:\Users\soste\Documents\fefw-pt-br

1. Leia BRIEF.md inteiro (estilo, glossário, o que preservar, termos já fixados).
2. Leia pt\000a.json (nomes de pessoas, classes, lugares, capítulos, clãs, terrenos, títulos já traduzidos; o inglês
   correspondente está em batches\000a.json). Todo nome que aparecer no seu lote deve usar **exatamente** esse termo.
3. Para cada lote NNN que recebeu: leia batches\NNN.json ({"<arquivo>": {"<índice>": "English"}}) e escreva
   pt\NNN.json como objeto plano {"<arquivo>\t<índice>": "PT-BR"} (TAB real entre arquivo e índice), com TODAS as ids
   do lote e nenhuma a mais. UTF-8, ensure_ascii=False, indent=1. Não toque em outros arquivos de pt\.
4. Rode `python -I tools\check.py NNN` para cada lote; precisa terminar em "0 problems". Corrija e repita até passar.
5. Responda só com: a saída do check de cada lote e os novos termos recorrentes que você fixou (EN → PT), no máximo 15.

Regras essenciais (o validador confere):
- Códigos `{{...}}`, tags `<TH>`, `<ICA>`, `<ACB>` etc., `%d`, `%s` idênticos e na posição equivalente.
- Mesmo número de `\n` por string; linhas de tamanho parecido, nunca mais de 10% mais longas que o inglês.
- Strings que são só um ícone (U+E000–U+E2FF), só símbolos, só números ou só códigos: copiar idênticas.
- Não resumir, não juntar, não inventar. Tradução completa e natural, tom de cada personagem preservado.
- Arquivos de história (N_XXX_cNN, SE_*, SUP_*, SideStory_*, MV*, LG_*): são diálogos em ordem; leia o arquivo inteiro
  antes de traduzir para manter contexto, gênero de quem fala e consistência de tratamento.
- Arquivos de sistema (Item, Skill, Quest, SubQuest, Roster, Library, Bird, Meal, Shop, Levelup, Tutorial, Tips, Die,
  Classchange, Guide, Rule): textos de menu; manter curtos, abreviações do glossário.
- Lotes que continuam um arquivo começado em outro lote (ex.: Item em 000g e 000h): mesma terminologia dos nomes
  (Wooden Sword → Espada de Madeira em todos).
