# build.py: every pt/*.json ("file\tindex" -> PT) over src/USen -> out/romfs/Msg/USen/*.msbt.zst (+ the two font chains),
# then copied into the game's romfs (GAME) so the loose dump is in Portuguese. Untranslated strings keep the English.
import glob, json, os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__)); import msbt, fcpx

GAME = r"C:\Users\soste\Emuladores\PokeDinner\Jogos\fire emblem\romfs"


def main():
    pt = {}
    for f in sorted(glob.glob("pt/*.json")): pt.update(json.load(open(f, encoding="utf-8")))
    by_file = {}
    for k, v in pt.items():
        f, i = k.split("\t"); by_file.setdefault(f, {})[int(i)] = v
    out = "out/romfs/Msg/USen"; os.makedirs(out, exist_ok=True)
    done = 0
    for name, tr in by_file.items():
        h, secs = msbt.read(f"src/USen/{name}.msbt.zst"); st = msbt.strings(secs)
        for i, v in tr.items(): st[i] = v
        msbt.write(f"{out}/{name}.msbt.zst", msbt.rebuild(h, secs, st)); done += len(tr)
    fo = "out/romfs/Font"; os.makedirs(fo, exist_ok=True)
    open(f"{fo}/Cyber.bfcpx", "wb").write(fcpx.build([("__Cyber.bffnt", fcpx.FULL), ("__System.bffnt", fcpx.FULL), ("__nintendo_ext_003.bffnt", fcpx.EXT), ("__System_Ext.bffnt", fcpx.EXT2)]))
    open(f"{fo}/System_Large.bfcpx", "wb").write(fcpx.build([("__System_Large.bffnt", fcpx.FULL), ("__System.bffnt", fcpx.FULL), ("__nintendo_ext_003_Large.bffnt", fcpx.EXT), ("__System_Large_Ext.bffnt", fcpx.EXT2)]))
    print(f"{done} strings in {len(by_file)} files -> out/romfs")
    if "--install" in sys.argv:
        shutil.copytree("out/romfs", GAME, dirs_exist_ok=True); print("installed into", GAME)


main()
