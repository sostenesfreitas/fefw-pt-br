# Glyph coverage of the game's BFFNT fonts (zstd): which test characters each font can draw.
import glob, os, struct, sys, zstandard

TEST = "jJ:;!?ãõçÃÕÇéêáàíóúÉÊÁÍÓÚüñ"


def codepoints(d):
    assert d[:4] == b"FFNT", d[:4]
    bom = d[4:6]; E = "<" if bom == b"\xff\xfe" else ">"
    hdr = struct.unpack(E + "H", d[6:8])[0]
    nsec = struct.unpack(E + "H", d[0x10:0x12])[0]
    off = hdr; cps = set()
    for _ in range(nsec):
        tag = d[off:off+4]; size = struct.unpack(E + "I", d[off+4:off+8])[0]
        if tag == b"CMAP":
            b = d[off+8:off+size]
            first, last, typ = struct.unpack(E + "IIH", b[:10])
            if typ == 0:  # direct
                base = struct.unpack(E + "H", b[10:12])[0]
                if base != 0xFFFF: cps.update(range(first, last + 1))
            elif typ == 1:  # table
                arr = struct.unpack(E + f"{last-first+1}H", b[12:12 + 2*(last-first+1)])
                cps.update(first + i for i, g in enumerate(arr) if g != 0xFFFF)
            elif typ == 2:  # scan
                n = struct.unpack(E + "H", b[12:14])[0]
                for i in range(n):
                    cp, g = struct.unpack(E + "IH", b[16 + 8*i:22 + 8*i])
                    if g != 0xFFFF: cps.add(cp)
        off += size
    return cps


for f in sorted(glob.glob(os.path.join(sys.argv[1], "*.bffnt.zst"))) if __name__ == "__main__" else []:
    d = zstandard.ZstdDecompressor().decompress(open(f, "rb").read(), max_output_size=300_000_000)
    try:
        cps = codepoints(d)
    except Exception as e:
        print(os.path.basename(f).ljust(36), "ERR", e); continue
    missing = "".join(c for c in TEST if ord(c) not in cps)
    print(os.path.basename(f).ljust(36), f"{len(cps):6d} glyphs  missing: {missing or '-'}")
