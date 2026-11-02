# src/USen/*.msbt.zst -> batches/NNN.json to translate: {"<file>": {"<index>": "English"}}; a file is never split.
# Batch 000 = names and short labels (people, items, skills, classes, places, chapters) that the rest looks up.
# Strings that are empty, pure control codes or numbers are skipped (build keeps the English for them).
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__)); import msbt

WORDS = 6000
NAMES = ("Person", "Item", "Skill", "Job", "Terrain", "Clan", "Spot", "Chapter", "BattleTitle", "Roster", "Legion",
         "Achievement", "Library", "Title", "Bird", "Ride", "Meal", "Shop", "Quest", "SubQuest", "whole", "Watching")
CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def wanted(s):
    t = CTRL.sub("", s).strip()
    return bool(t) and not re.fullmatch(r"[\d\s.,:%+\-/]*", t)


def main():
    by_file = {}
    for f in sorted(glob.glob("src/USen/*.msbt.zst")):
        name = os.path.basename(f)[:-len(".msbt.zst")]
        _, secs = msbt.read(f)
        d = {str(i): s for i, s in enumerate(msbt.strings(secs)) if wanted(s)}
        if d: by_file[name] = d
    names = {k: v for k, v in by_file.items() if k in NAMES}
    rest = {k: v for k, v in by_file.items() if k not in names}
    batches, cur, words = [names], {}, 0
    for k in sorted(rest):
        w = sum(len(s.split()) for s in rest[k].values())
        if cur and words + w > WORDS: batches.append(cur); cur, words = {}, 0
        cur[k] = rest[k]; words += w
    if cur: batches.append(cur)
    os.makedirs("batches", exist_ok=True)
    for n, b in enumerate(batches):
        json.dump(b, open(f"batches/{n:03d}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{n:03d}: {sum(map(len, b.values())):5d} strings, {sum(len(s.split()) for d in b.values() for s in d.values()):6d} words, {len(b)} files")


main()
