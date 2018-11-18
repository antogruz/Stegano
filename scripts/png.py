#!/usr/bin/env python3
import sys

from bits import *

def assert_equals(expected, actual):
    if expected != actual:
        print("Expected to get", expected, "got", actual)

class Parser:
    def __init__(self, fh):
        self.fh = fh
        self.d = {}
        self.end = False

    def read_number(self, key, bytes_count):
        value = 0
        if bytes_count == 4:
            value = read_int(self.fh)
        if bytes_count == 2:
            value = read_short(self.fh)
        if bytes_count == 1:
            value = toint(read_char(self.fh))
        self.append(key, value)

    def read_string(self, key, bytes_count):
        value = ""
        for i in range(bytes_count):
            value += (tochar(read_char(self.fh)))
        self.append(key, value)

    def read_crc(self):
        read_int(self.fh)

    def skip(self, size):
        self.fh.read(size)

    def check(self, key, bytes, conv):
        for b in bytes:
            assert_equals(b, conv(read_char(self.fh)))

    def append(self, key, value):
        self.d[key] = value
        print(key, str(value))


def main():
    file = sys.argv[1]
    with open(file, "rb") as fh:
        parser = Parser(fh)
        parser.check("signature", [137, 80, 78, 71, 13,10,26,10], toint)
        parse_ihdr(parser)
        if int(parser.d["colortype"]) == 3:
            parse_palette(parser)

        while not parser.end:
            parse_chunk(parser)

def parse_ihdr(p):
    p.read_number("sizeIHDR", 4)
    assert p.d["sizeIHDR"] == 13

    p.check("typeIHDR", ['I', 'H', 'D', 'R'], tochar)
    p.read_number("width", 4)
    p.read_number("height", 4)
    p.read_number("bitdepth", 1)
    p.read_number("colortype", 1)
    p.read_number("compression", 1)
    p.read_number("filter", 1)
    p.read_number("interlace", 1)
    p.read_crc()

def parse_palette(p):
    p.read_number("sizePalette", 4)
    p.check("typePLTE", ["P", "L", "T", "E"], tochar)
    colors = p.d["sizePalette"] / 3
    for i in range(int(colors)):
        p.skip(3)
    p.read_crc()

def parse_chunk(p):
    p.read_number("sizeChunk", 4)
    p.read_string("typeChunk", 4)
    if p.d["typeChunk"] == "IEND":
        p.end = True
    p.skip(p.d["sizeChunk"])
    p.read_crc()

main()
