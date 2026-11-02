# python -I tools/check.py NNN : validates pt/NNN.json against batches/NNN.json.
# Fails if an id is missing/extra, or if tags <...>, control codes, placeholders and the number of line breaks differ.
import json, re, sys

CODES = re.compile(r"<[^<>\n]*>|[\x00-\x08\x0b\x0c\x0e-\x1f][^\x00-\x1f]{0,8}?(?=[\s\w]|$)|\{[^}]*\}|\[[^\]]*\]|%[sd]|\$\w+")


def main(n):
    en = json.load(open(f"batches/{n}.json", encoding="utf-8"))
    pt = json.load(open(f"pt/{n}.json", encoding="utf-8"))
    ids = {i: s for d in en.values() for i, s in d.items()}  # ids are unique per file; flatten as "file\tindex"
    ids = {f"{f}\t{i}": s for f, d in en.items() for i, s in d.items()}
    bad = []
    missing = sorted(set(ids) - set(pt)); extra = sorted(set(pt) - set(ids))
    for k in missing: bad.append(f"missing {k}")
    for k in extra: bad.append(f"extra {k}")
    for k, s in ids.items():
        if k not in pt: continue
        t = pt[k]
        if not isinstance(t, str) or not t.strip(): bad.append(f"empty {k}"); continue
        if s.count("\n") != t.count("\n"): bad.append(f"line breaks {k}: {s.count(chr(10))} vs {t.count(chr(10))}")
        # player-gender switches («masc|fem» in PT, {{0e080000...}} in EN) are free: each language places its own
        if t.count("«") != t.count("»") or re.search(r"«[^»|]*»", t): bad.append(f"bad gender switch {k}")
        s, t = re.sub(r"\{\{0e0800000[0-9a-f]*\}\}", "", s), re.sub(r"«[^»]*»", "", t)
        ce, ct = sorted(CODES.findall(s)), sorted(CODES.findall(t))
        if ce != ct: bad.append(f"codes {k}: {ce} vs {ct}")
    for b in bad[:40]: print(b)
    print(f"{n}: {len(ids)} ids, {len(bad)} problems")
    sys.exit(1 if bad else 0)


main(sys.argv[1])
