from bits import *
from tests import assert_equals

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

    def read_string(self, key, bytes_count, verbose=True):
        value = ""
        for i in range(bytes_count):
            value += (tochar(read_char(self.fh)))
        self.append(key, value, verbose)

    def skip(self, size):
        self.fh.read(size)

    def check(self, key, bytes, conv):
        for b in bytes:
            assert_equals(b, conv(read_char(self.fh)))

    def append(self, key, value, verbose=True):
        self.d[key] = value
        if (verbose):
            print(key, str(value))


