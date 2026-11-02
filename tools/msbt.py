# MSBT (UTF-8, little-endian, v3) read/write for Fortune's Weave: Msg/<lang>/*.msbt.zst.
# read(path) -> (header_bytes, [(tag, body_bytes)...]); strings(sections) -> list[str]; rebuild(sections, strings) -> bytes.
import struct, zstandard

ENC = "utf-8"


def read(path):
    d = zstandard.ZstdDecompressor().decompress(open(path, "rb").read(), max_output_size=500_000_000)
    assert d[:8] == b"MsgStdBn" and d[8:10] == b"\xff\xfe" and d[0x0C] == 0, path
    nsec = struct.unpack("<H", d[0x0E:0x10])[0]
    secs, off = [], 0x20
    for _ in range(nsec):
        tag = d[off:off + 4]
        size = struct.unpack("<I", d[off + 4:off + 8])[0]
        secs.append((tag, d[off + 0x10:off + 0x10 + size]))
        off = (off + 0x10 + size + 15) & ~15
    return d[:0x20], secs


import re
TAG = re.compile(r"\{\{([0-9a-f]+)\}\}")


def decode(s):
    # control codes (0x0E group:u16 type:u16 len:u16 args / 0x0F group:u16 type:u16) become {{hex}} so they survive JSON
    out, i = [], 0
    while i < len(s):
        b = s[i]
        if b == 0x0E and i + 7 <= len(s):
            ln = struct.unpack("<H", s[i + 5:i + 7])[0]; j = i + 7 + ln
            out.append("{{" + s[i:j].hex() + "}}"); i = j
        elif b == 0x0F and i + 5 <= len(s):
            out.append("{{" + s[i:i + 5].hex() + "}}"); i += 5
        else:
            j = i + 1
            while j < len(s) and s[j] not in (0x0E, 0x0F): j += 1
            out.append(s[i:j].decode(ENC, "surrogateescape")); i = j
    return "".join(out)


GENDER = re.compile(r"«([^|«»]*)\|([^|«»]*)»")


def gender_code(m, f):
    # player-gender switch: 0E, group 8, type 0, arg len, then (u16 len + utf8) for masculine and feminine
    args = b"".join(struct.pack("<H", len(x)) + x for x in (m.encode(ENC), f.encode(ENC)))
    return "{{" + (b"\x0e" + struct.pack("<HHH", 8, 0, len(args)) + args).hex() + "}}"


def _enc(t):
    t = GENDER.sub(lambda g: gender_code(g.group(1), g.group(2)), t)
    out, pos = [], 0
    for m in TAG.finditer(t):
        out.append(t[pos:m.start()].encode(ENC, "surrogateescape")); out.append(bytes.fromhex(m.group(1))); pos = m.end()
    out.append(t[pos:].encode(ENC, "surrogateescape"))
    return b"".join(out)


def strings(secs):
    body = dict(secs)[b"TXT2"]
    n = struct.unpack("<I", body[:4])[0]
    offs = struct.unpack(f"<{n}I", body[4:4 + 4 * n])
    out = []
    for i in range(n):
        s = body[offs[i]:offs[i + 1] if i + 1 < n else len(body)]
        out.append(decode(s[:-1] if s.endswith(b"\x00") else s))
    return out


def rebuild(header, secs, strs):
    n = len(strs)
    enc = [_enc(s) + b"\x00" for s in strs]
    offs, pos = [], 4 + 4 * n
    for e in enc:
        offs.append(pos); pos += len(e)
    txt2 = struct.pack("<I", n) + struct.pack(f"<{n}I", *offs) + b"".join(enc)
    out = bytearray(header)
    for tag, body in secs:
        if tag == b"TXT2":
            body = txt2
        out += tag + struct.pack("<I", len(body)) + b"\x00" * 8 + body
        pad = (-len(out)) % 16
        out += b"\xab" * pad
    struct.pack_into("<I", out, 0x12, len(out))
    return bytes(out)


def write(path, data):
    open(path, "wb").write(zstandard.ZstdCompressor(level=19).compress(data))


if __name__ == "__main__":  # self-check: decode -> rebuild must be byte-identical
    import sys
    h, secs = read(sys.argv[1])
    strs = strings(secs)
    orig = zstandard.ZstdDecompressor().decompress(open(sys.argv[1], "rb").read(), max_output_size=500_000_000)
    assert rebuild(h, secs, strs) == orig, "roundtrip mismatch"
    print(len(strs), "strings, roundtrip ok")
