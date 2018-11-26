#!/usr/bin/env python3
import sys
import string

import png
from bits import toint, read_char, write_byte
from tobits import bits_to_byte, low_bit

def main():
    file = sys.argv[1]
    with open(file, "rb") as fh:
        picture = png.parse(fh)

    with open(file, "rb") as fh, open("lsb", "wb") as out:
        fh.seek(picture.data[0]["seek"])
        write_lsb(fh, out, picture.data[0]["size"])

def write_lsb(fh, out, size):
    bits = []
    for i in range(size):
        byte = toint(read_char(fh))
        bits.append(low_bit(byte))
        if len(bits) == 8:
            write_byte(out, bits_to_byte(bits))
            bits = []




main()
