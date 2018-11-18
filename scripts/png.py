#!/usr/bin/env python3
import sys

from bits import *

def assert_equals(expected, actual):
    if expected != actual:
        print("Expected to get", expected, "got", actual)
        exit(-1)

class Parser:
    def __init__(self, fh):
        self.fh = fh
        self.d = {}

    def read_number(self, key, bytes_count):
        value = 0
        value = read_int(self.fh)
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


main()
