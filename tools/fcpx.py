# BFCPX (font complex = fallback chain of bffnt fonts) writer. build([(name, [(first,last),...]), ...]) -> bytes.
# Layout: hdr(0x14) + u32 1 + u32 4 + node. Node = font entry {0, hdr_size, nranges, 0x10, ranges, name\0 pad4}
# or pair {2, off_left=0x0c, off_right} whose right child is another node. Self-check rebuilds the game's own files.
import struct, sys, os

FULL = [(0x0000, 0xDFFF), (0xE240, 0xFFFF)]   # the ranges the game gives its main font
EXT = [(0xE000, 0xE1FF)]                       # nintendo_ext_003 (controller glyphs)
EXT2 = [(0xE200, 0xE23F)]                      # *_Ext fonts


def entry(name, ranges):
    n = name.encode() + b"\x00"
    n += b"\x00" * ((-len(n)) % 4)
    body = struct.pack("<IIII", 0, 8 + 8 + 8 * len(ranges), len(ranges), 0x10)
    body += b"".join(struct.pack("<II", a, b) for a, b in ranges)
    return body + n


def node(fonts):
    if len(fonts) == 1:
        return entry(*fonts[0])
    left = entry(*fonts[0])
    return struct.pack("<III", 2, 0x0C, 0x0C + len(left)) + left + node(fonts[1:])


def build(fonts):
    body = struct.pack("<II", 1, 4) + node(fonts)
    size = 0x10 + len(body)   # the game's size field excludes the 4-byte magic
    return b"FCPX\xff\xfe\x14\x00\x00\x00\x03\x09" + struct.pack("<I", size) + body


if __name__ == "__main__":  # self-check against the originals
    d = sys.argv[1]
    cases = {
        "Cyber.bfcpx": [("__Cyber.bffnt", FULL)],
        "FEFont.bfcpx": [("__FEFont.bffnt", FULL), ("__FEFont_Ext.bffnt", EXT2)],
        "Cyber_CNzh.bfcpx": [("__System_CNzh.bffnt", FULL), ("__nintendo_ext_003.bffnt", EXT), ("__System_Ext.bffnt", EXT2)],
        "System_Large.bfcpx": [("__System_Large.bffnt", FULL), ("__nintendo_ext_003_Large.bffnt", EXT), ("__System_Large_Ext.bffnt", EXT2)],
    }
    for f, fonts in cases.items():
        orig = open(os.path.join(d, f), "rb").read()
        assert build(fonts) == orig, f
    print("fcpx self-check ok")
