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

    def read_number(self, key, bytes_count):
        value = 0
        if bytes_count == 4:
            value = read_int(self.fh)
        if bytes_count == 2:
            value = read_short(self.fh)
        if bytes_count == 1:
            value = read_char(self.fh)
        self.append(key, value)

    def read_string(self, key, bytes_count):
        value = ""
        for i in range(bytes_count):
            value += str(read_char(self.fh))
        self.append(key, value)

    def check(self, key, bytes):
        for b in bytes:
            assert_equals(b, toint(read_char(self.fh)))

    def append(self, key, value):
        self.d[key] = value
        print(key, str(value))


def main():
    file = sys.argv[1]
    with open(file, "rb") as fh:
        parser = Parser(fh)
        parser.check("signature", [137, 80, 78, 71, 13,10,26,10])
        parse_ihdr(parser)

def parse_ihdr(p):
    p.read_number("sizeIHDR", 4)
    assert p.d["sizeIHDR"] == 13

    p.check("typeIHDR", ords(['I', 'H', 'D', 'R']))
    p.read_number("width", 4)
    p.read_number("height", 4)
    p.read_number("bitdepth", 1)
    p.read_number("colortype", 1)
    p.read_number("compression", 1)
    p.read_number("filter", 1)
    p.read_number("interlace", 1)

def ords(chars):
    return [ord(c) for c in chars]

main()
