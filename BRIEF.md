# Brief de tradução — Fire Emblem: Fortune's Weave (EN → PT-BR)

RPG tático da Nintendo/Intelligent Systems (Switch 2, 2026). Mundo: **Dagda**, continente dominado pelo Império
Dagdano (capital **Dagsion**), com reinos vizinhos (Saramis, Arago, Damascar, Kunlun, Cybele). O jogador é um
**Mediator** (Mediador), corpo artificial despertado por **Fortuna** para cumprir a profecia do **Promised One**
(Prometido) contra **Balor** e as hordas do **Underworld** (Submundo). Quatro protagonistas com rotas próprias na
Parte I: **Cai**, **Dietrich**, **Theodora** (rainha de Saramis), **Leda**. Há a arena **Heroic Games** (Jogos
Heroicos), gladiadores, deuses (Solel the Sunbearer, Mars, Fortuna, Credna), templos, obeliscos.

## Fluxo

- Entrada: `batches/NNN.json` = `{ "<arquivo>": { "<índice>": "English", ... }, ... }`.
- Saída: `pt/NNN.json` = `{ "<arquivo>\t<índice>": "texto PT-BR", ... }` (chave = arquivo + TAB + índice), **todas** as
  ids do lote, nada a mais.
- `python -I tools/check.py NNN` valida (falha se faltar id ou se as marcações não baterem). Corrigir até passar.
- Nomes já traduzidos: `pt/000a.json` (pessoas, classes, lugares, capítulos, clãs, terrenos, títulos de batalha).
  Procure ali antes de traduzir um nome, para usar **exatamente** o mesmo termo. O inglês está em `batches/000a.json`.

## Preservar exatamente (o validador confere)

- Códigos `{{...}}` (hex): variáveis do jogo (nome do jogador, números, cores). Copiar idênticos, na posição
  equivalente da frase. `{{0e020001000000}}` costuma ser o nome do jogador; `{{0e010000000000}}` um número.
- Tags `<TH>`, `<ICA>`, `<ICB>`, `<ACA>`, `<ACB>`, `<NCA>`, `<EDH>` e similares no início da string: são marcação de
  cena/escolha. Copiar como estão; traduzir só o texto depois delas. Uma string que é só a tag fica só a tag.
- Quebras de linha `\n`: **mesmo número** que o original. As caixas de diálogo têm 2 linhas de ~55 caracteres;
  quebrar em ponto natural, linhas de tamanho parecido, nunca mais longas que o inglês em mais de 10%.
- `%d`, `%s`, `[...]`, `{...}`: idênticos.
- Não inventar, não resumir, não juntar frases: cada string inteira e independente.

## Estilo

- Português do Brasil natural, no registro das localizações oficiais da Nintendo (Fire Emblem Heroes em PT-BR,
  Zelda, Xenoblade). Nada de gíria regional; humor e tom de cada personagem preservados.
- Tratamento: "você" entre iguais; nobres e soldados usam "Vossa Majestade", "Majestade", "senhor(a)", "milorde",
  "milady" conforme o original (Your Majesty → Vossa Majestade; Lord/Lady X → Lorde X / Lady X; Miss Leda → Senhorita
  Leda; Father Mahdel (sacerdote) → Padre Mahdel; Prince/Queen/King → Príncipe/Rainha/Rei).
- Nomes próprios de pessoas e lugares ficam como no inglês (Cai, Dietrich, Dagsion, Saramis, Ribeira, Kunlun).
  Epítetos e títulos traduzem: the Sunbearer → o Portador do Sol; the Promised One → o Prometido; Divine Sovereign →
  Soberano Divino; Divine Emperor → Imperador Divino; Maned Demon → Demônio de Juba; the Answerer → o Respondente.
- Títulos de capítulo/missão: só a primeira letra maiúscula ("A ave branca", "Estrada para a capital"), exceto nomes
  próprios. Nomes de itens, habilidades, classes e inimigos com Iniciais Maiúsculas como no inglês.
- Interjeições: Heh → Heh; Hmph → Hmpf; Ugh → Argh; Whoa → Uau; Hahaha fica. Reticências e aspas como no original.
- Gênero: o jogador (Mediator) pode ser homem ou mulher; nas falas dirigidas a ele, preferir formas neutras
  ("você", "a pessoa", "quem…") a adjetivos marcados. Quando impossível, masculino.

## Glossário fixo

| EN | PT-BR |
|---|---|
| HP / Str / Mag / Dex / Spd / Lck / Def / Res / Mov / Rng | HP / For / Mag / Des / Vel / Sor / Def / Res / Mov / Alc |
| Hit / Avo / Crit / Atk / Cha / Bld / Con | Pre / Esq / Crít / Atq / Car / Por / Con |
| Exp / Level / Rank | Exp / Nível / Grau |
| combat art(s) | arte(s) de combate |
| skill / ability | habilidade |
| unit / ally / foe / enemy | unidade / aliado / inimigo / inimigo |
| weapon triangle / sword / lance / axe / bow / tome / staff / gauntlet | triângulo de armas / espada / lança / machado / arco / tomo / cajado / manopla |
| black magic / white magic | magia negra / magia branca |
| Underworld / Underworld Pillar / Underworld Fog | Submundo / Pilar do Submundo / Névoa do Submundo |
| Mediator / Promised One / Awakened | Mediador / Prometido / Desperto |
| Heroic Games / Qualifier / Skirmish | Jogos Heroicos / Eliminatória / Escaramuça |
| Dagdan Empire / Dagdan | Império Dagdano / dagdano |
| Commoner / Noble / God | Plebeu / Nobre / Deus |
| Gladiator / Soldier / Hunter / Diviner / Archer / Priest / Shaman / Rogue / Brigand / Pugilist | Gladiador / Soldado / Caçador / Adivinho / Arqueiro / Sacerdote / Xamã / Ladino / Bandido / Pugilista |
| Myrmidon / Swordmaster / Armored Knight / Great Knight / Bow Knight / Sniper / Bishop / Druid / Dancer / Trickster | Mirmidão / Mestre da Espada / Cavaleiro Blindado / Grande Cavaleiro / Cavaleiro Arqueiro / Franco-atirador / Bispo / Druida / Dançarino(a) / Trapaceiro |
| Ornius / Ornius Rider / Bau / Pegasus / War Elephant | Ornius / Cavaleiro de Ornius / Bau / Pégaso / Elefante de Guerra |
| Heal Spot / Warp Spot / Guard Spot / Avo Spot / Summoning Spot | Ponto de Cura / Ponto de Teleporte / Ponto de Guarda / Ponto de Esquiva / Ponto de Invocação |
| Chest / Lever / Brazier / Ballista / Onager / Fire Orb | Baú / Alavanca / Braseiro / Balista / Onagro / Orbe de Fogo |
| Part I / II / III, Chapter N, Prologue, Interlude | Parte I / II / III, Capítulo N, Prólogo, Interlúdio |
| Cai's Path (etc.) | Rota de Cai |
| Support / support conversation | Apoio / conversa de apoio |
| Roster / Library / Achievement / Legion / Clan | Elenco / Biblioteca / Conquista / Legião / Clã |
| Meal / Thermae / Theater / Arena / Obelisk | Refeição / Termas / Teatro / Arena / Obelisco |
| Scout / Ride / Bird | Explorar / Montaria / Ave |
| Save / Load / Continue / New Game / Options / Confirm / Back / Cancel | Salvar / Carregar / Continuar / Novo Jogo / Opções / Confirmar / Voltar / Cancelar |
| Press Any Button | Pressione qualquer botão |

## Termos fixados nos lotes 000a / 119 / 120 — usar igual

- Classes: Light Cavalry → Cavalaria Leve; Wing Soldier → Soldado Alado; Charioteer → Cocheiro de Guerra; Armored Ornius Rider → Cavaleiro de Ornius Blindado; Ranger / Guardian / Dreadnought / Warrior / Blacksmith → Patrulheiro / Guardião / Couraçado / Guerreiro / Ferreiro; Forest Knight / Troubadour / Dragoon → Cavaleiro da Floresta / Trovador / Dragão; Shadow Seeker / Sentinel / Battlemaster → Buscador das Sombras / Sentinela / Mestre de Batalha; Wiseman / High Savant / Bau Lord → Sábio / Alto Sábio / Lorde de Bau; Castle Knight → Cavaleiro do Castelo; Bow Adept → Adepto do Arco; War Monk → Monge de Guerra; Celestial Trooper → Soldado Celestial; Elephant Rider → Cavaleiro de Elefante.
- Monstros: Blight Louse / Atlas Bear / Sandworm / Giant / Lesser-Greater Titanus / Shade / Mummy → Piolho da Praga / Urso de Atlas / Verme da Areia / Gigante / Titanus Menor-Maior / Sombra / Múmia; Risen Dead → Morto Ressurgido; Striped Wolf → Lobo Listrado; Sea Beast → Fera Marinha; Living Armor → Armadura Viva; Necrodragon → Necrodragão; Demonic Beast → Fera Demoníaca; Flesh Pod → Casulo de Carne; Sand Boar → Javali das Areias.
- Epítetos: Brimstone Lord → Lorde do Enxofre; Bringer of War → Portador da Guerra; Baneful Knight → Cavaleiro Funesto; Progenitor God → Deus Progenitor; Sea Tyrant → Tirano dos Mares; White-Maned Demon → Demônio de Juba Branca; Pale Raven → Corvo Pálido; The Reaper → O Ceifador; Flame Lord → Lorde das Chamas; Weaver of Causality → Tecelã da Causalidade; The Phantom → O Fantasma; Balor's Shade → Sombra de Balor.
- Facções: Thundercloud Knights → Cavaleiros da Nuvem de Trovão; Silver Knights of Tellus → Cavaleiros de Prata de Tellus; Bragança Brotherhood → Irmandade de Bragança; The Har Hali → Os Har Hali; Rains of Palma → Chuvas de Palma; Forgotten Alcor → Alcor Esquecida; Order of Mithras → Ordem de Mithras; Black-Swan Pirates → Piratas do Cisne Negro; Rose Tempest → Tempestade Rósea; Ribeira Winds → Ventos de Ribeira; House Lamine → Casa Lamine; Megaira's Beacon → Farol de Megaira; Tale of the Moon → Conto da Lua; Fiery Mane → Juba Flamejante; Linaria Dewdrops → Orvalho de Linaria; Twin Jewels of Arago → Joias Gêmeas de Arago; Pale Raven's Bridal Party → Cortejo Nupcial do Corvo Pálido; "X's Army" → "Exército de X"; Alliance Forces → Forças da Aliança; Dagdan Imperial Army → Exército Imperial Dagdano.
- Gentílicos: Aragonian → aragonês; Saraminian → saraminiano; Cydonian → cidoniano; Agarthan → agarthano; Dagdan → dagdano.
- Lugares: Stronghold → Fortaleza; Hold → Reduto; Fort X → Forte X; Posthouse → Posto; Post Town → Cidade de Posta; Span → Vão; Pass → Passo; Gorge → Desfiladeiro; Canyon → Cânion; Hightown/Midtown/Lowtown → Cidade Alta/Média/Baixa; Temple Row → Rua dos Templos; Gate of the Gods → Portal dos Deuses; Underworld Gate → Portal do Submundo; "Gate II: Yin Yuan" → "Portão II: Yin Yuan"; Warp Device → Dispositivo de Teleporte; Guesthouse → Hospedaria; Inn → Estalagem; Branch Temple → Templo Filial; Crystal Palace → Palácio de Cristal; Obelisk Chamber → Câmara do Obelisco; Temple of the Diadem → Templo do Diadema; Dagda's Cauldron → Caldeirão de Dagda.
- Arena: Main Match / Semifinal / Finals / Exhibition / Preamble → Fase principal / Semifinal / Final / Exibição / Preâmbulo; "Battle vs. X" → "Batalha contra X"; "Showdown vs. X" → "Confronto contra X"; "X's Trial" → "Provação de X".
- Sistemas: Blaze / Blaze Gauge / Overblaze / Burst → Chama / Medidor de Chama / Superchama / Explosão; Celestial Wells → Poços Celestiais; Third Eye → Terceiro Olho; Divine Sand → Areia Divina; Karma Shards → Fragmentos de Carma; Renown / Relief → Renome / Alívio; Causality → Causalidade; Foresight → Presciência; Bloodmark → Marca de Sangue; Clash → Confronto; Gambit → Estratagema; Battalion → Batalhão; Squad → Esquadrão; Link / LP → Elo / PE; Staggering Blow → Golpe Atordoante; Paralogue → Paralogo; Subquest → Missão Secundária; Checkpoint → Barreira; Notable Deeds → Feitos Notáveis; War Arc / Salvation Arc → Arco da Guerra / Arco da Salvação; Follow-Up → Ataque Duplo; Dispatch Officer → Oficial de Despacho; Threat Range → Área de Perigo; Settings → Config. (rótulo curto); ON/OFF → LIGADO/DESLIGADO; Automaton → Autômato; Jester → Bobo; Crest of Flames → Brasão das Chamas.
- Abreviações extras: AS → VA; Ddg → Dsv; Mt → Pod; Pwr → Pot; Phys/Mys → Fís/Mís; Spec → Esp; Wt → Pes; Eff → Efic; Shld → Escd; Prt / Rsl ficam.
- Terreno: Ability Enhancer → Amplificador de Habilidade; Magic Flow Switch → Interruptor de Fluxo Mágico; Launch Mechanism → Mecanismo de Lançamento; Victory Token → Marco de Vitória; Score Beacon → Farol de Pontuação; Soul Plate → Placa de Almas; Orichalcum Pile → Pilha de Oricalco; Off-Limits → Área Proibida; "X Miasma" → "Miasma da/do X".
- NPCs genéricos: Innkeeper → Estalajadeiro(a); Headhunter → Recrutador(a); Stable Keeper → Cavalariço(a); Reception → Recepção; Chancellor → Chanceler; Viceroy → Vice-rei; Saint Katarina → Santa Katarina.
- Strings que são só um caractere de ícone (U+E000–U+E2FF) ou só códigos `{{…}}`: copiar idênticas.

## Termos fixados nos lotes de história (001–076) — usar igual

Heart Core → Núcleo Cardíaco; Answerer → a Respondente (feminino; habilidade "Grito do Respondente"); Crest of X → Brasão de X; Crest Stone → Pedra de Brasão; godmarks → marcas divinas; Hero's Relic → Relíquia de Herói; Grand Oracle → Grande Oráculo; Great Undoing → Grande Ruína; The Beginning (Sothis) → O Começo; progenitor god (Sothis) → deusa progenitora; demon god (Balor) → deus demônio; simulacrum → simulacro; vessel → receptáculo; the great cycle → o Grande Ciclo; Underworld War → Guerra do Submundo; Dagdan Alliance → Aliança Dagdana; Supreme Dagdan Declaration → Declaração Suprema Dagdana; Dagdan Imperial Calendar → Calendário Imperial Dagdano (meses inventados ficam); Arc(s) / Supreme Arc → Arca(s) / Arca Suprema; Gate(s) of the Gods → Portal(is) dos Deuses; underworld gate → portal do Submundo; risen dead → mortos ressurgidos; Flame Lord(s) → Lorde(s) das Chamas; Killing Edge → Gume Mortal; Divine Sovereign → Soberano Divino (Soberana Divina para Jurah); Order of the Haze → Ordem da Bruma; Founder Balor → Fundador Balor; Balor of the Ashes → Balor das Cinzas; People of the White Egg → Povo do Ovo Branco; Guardians of the Compass → Guardiões da Bússola; Sword of the Creator → Espada do Criador; Demon Sword Fragarach → Espada Demoníaca Fragarach; Shield of Dagda → Escudo de Dagda; godshield → escudo divino; Saint Cichol → São Cichol; King of Liberation → Rei da Libertação; Voice upon the Peak → Voz sobre o Pico; Dagda's Cauldron → Caldeirão de Dagda; Pirate King → Rei Pirata; Arago the Upright → Arago, o Justo; Mad King Hanno → Rei Louco Hanno; Lord of Impalement → Lorde do Empalamento; Mosa Holy State → Santo Estado de Mosa; Veil of the Void → Véu do Vazio; Strife Obelisk → Obelisco da Discórdia; Goddess of Fate → Deusa do Destino; Spell-Scholar → Erudito dos Feitiços.

Epítetos: Hell's-Eye Cai → Cai Olho do Inferno; Dietrich, the Ravishing Shadow → Dietrich, a Sombra Arrebatadora; Leda, Siren of the Six-String → Leda, Sereia das Seis Cordas; Theodora, the Breaker of Armies → Theodora, a Destruidora de Exércitos; Iron Bastion → Bastião de Ferro; Unkillable Guzran → Guzran Imortal; Mad Dog → Cão Raivoso; Swashbuckler King → Rei Bucaneiro; Mikaela Redblade → Mikaela Lâmina Rubra; Black-Lace Ninae → Ninae Renda Negra; Lady of Lilies → Dama dos Lírios; Keeper of Death and Night → Guardiã da Morte e da Noite; Windstorm Castor / Corundum Centurio → Castor Vendaval / Centurio Corindo; Aurora, Navigator's Clarion → Aurora, Clarim do Navegador; Demon Bear of Baphos → Urso Demônio de Baphos; Rose Pageant → Concurso da Rosa; Patron-Huntress → Caçadora Padroeira.

Tratamento: Sweetie → Querido (para Dietrich) / meu bem (para o jogador); Miss Leda → Senhorita Leda; boss (para Theodora) → chefa; "Sis" (Cai → Theodora) → Mana; Pop / Mom / Gramps / Great-Grandpa (Cai) → pai / mãe / vovô / bisavô; Stepmother → Madrasta; Auntie → Tia; milady → milady; cat priest (Orchel) → sacerdotisa gata; lead priest → sacerdotisa-chefe; archpriest → arquissacerdotisa; warding chain → corrente protetora; Vandahl Trading Co. → Cia. Comercial Vandahl; chariot → carro de guerra; *sigh*/*gasp* → *suspiro*, *sob* → *soluço*. vulkan, flamma, jamels, epimênio ficam.

Gênero: Talimun, Long, Zenon, Nuzzuo, Io, Peter, Benditz masculinos; Hedda, Hong Hua, Troy, Anatolia, Aurora, Orchel, Jurah, Halvin, Dante, Nydine, Lilian, Inyoni, Catania, Ninae, Mikaela, Esmeralda, Balboa (Vice-rainha), Ultand, Sha Lan femininas; Mu é menina disfarçada de menino; o Mediador (jogador) sempre em forma neutra.
