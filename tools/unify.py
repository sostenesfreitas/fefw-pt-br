# unify.py [--apply] : applies the term decisions of CONFLICTS.md to every pt/*.json (except files passed with --skip).
# Literal, case-sensitive replacements only; prints a count per rule so nothing changes silently.
import glob, json, re, sys

RULES = [
    ("Núcleo-Coração", "Núcleo Cardíaco"),
    ("O Princípio", "O Começo"),
    ("Bênção do Submundo", "Dádiva do Submundo"),
    ("Lordes da Chama", "Lordes das Chamas"), ("Lorde da Chama", "Lorde das Chamas"),
    ("Companhia de Comércio Vandahl", "Cia. Comercial Vandahl"),
    ("Companhia Comercial Vandahl", "Cia. Comercial Vandahl"),
    ("Companhia Vandahl", "Cia. Comercial Vandahl"),
    ("Relíquias Heroicas", "Relíquias de Herói"), ("Relíquia Heroica", "Relíquia de Herói"),
    ("Grande Colapso", "Grande Ruína"),
    ("Fio Mortal", "Gume Mortal"),
    ("Arcos Supremos", "Arcas Supremas"), ("Arco Supremo", "Arca Suprema"),
    ("% de ativação =", "Ativação % ="),
    ("Santo Cichol", "São Cichol"),
    ("Guzran Imatável", "Guzran Imortal"),
    ("Cão Louco", "Cão Raivoso"),
    ("Rei Espadachim", "Rei Bucaneiro"),
    ("Certame da Rosa", "Concurso da Rosa"),
    ("Caçadora Protetora", "Caçadora Padroeira"),
    ("sacerdote gato", "sacerdotisa gata"), ("Sacerdote gato", "Sacerdotisa gata"),
    ("corrente de proteção", "corrente protetora"),
    ("Deus Progenitor Sothis", "deusa progenitora Sothis"),
    ("10 de Elite", "10 Elites de Fódlan"),
    ("Centurio, o Corindo", "Centurio Corindo"),
    ("general-chefe", "general celestial chefe"),
    ("Grande August ", "Grande Augusto "), ("Grande August,", "Grande Augusto,"), ("Grande August.", "Grande Augusto."),
    ("Grande August!", "Grande Augusto!"), ("Grande August?", "Grande Augusto?"), ("Grande August\n", "Grande Augusto\n"),
    ("Ho ho ho", "Buá-há-há"), ("Bua há há", "Buá-há-há"), ("Buá rá rá", "Buá-há-há"),
    ("Góe Bolg", "Gáe Bolg"),
    ("Monastério de Garreg Mach", "Mosteiro de Garreg Mach"),
    ("Vento Ardente", "Vento Flamejante"),
    ("Mestre autora", "grande autora"), ("mestre autora", "grande autora"),
    ("Caça-Talentos", "Recrutador"),
    ("A Erudita dos Feitiços", "O Erudito dos Feitiços"), ("a Erudita dos Feitiços", "o Erudito dos Feitiços"),
    ("Arremesso Terreno", "Lançamento Terreno"), ("Arremesso Terrestre", "Lançamento Terreno"),
]
# Esmeralda's "Sweetie" for Dietrich in 002-004 and 011-013
SCOPED = {("002", "003", "004"): [("Fofo", "Querido")], ("011", "012", "013"): [("Meu Bem", "Querido")]}

apply = "--apply" in sys.argv
skip = {a for a in sys.argv[1:] if a.isdigit()}
counts = {}
for f in sorted(glob.glob("pt/*.json")):
    n = f[3:-5]
    if n in skip: continue
    d = json.load(open(f, encoding="utf-8")); changed = False
    rules = RULES + [r for ks, rs in SCOPED.items() if n in ks for r in rs]
    for k, v in d.items():
        nv = v
        for a, b in rules:
            c = nv.count(a)
            if c: counts[a] = counts.get(a, 0) + c; nv = nv.replace(a, b)
        if nv != v: d[k] = nv; changed = True
    if changed and apply:
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for a, c in sorted(counts.items(), key=lambda x: -x[1]): print(f"{c:4d}  {a!r}")
print("applied" if apply else "dry run")
