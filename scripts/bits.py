from struct import *

def read_int(fh):
    return unpack("I", fh.read(4))[0]

def read_short(fh):
    return unpack("H", fh.read(2))[0]

def write_int(fh, i):
    fh.write(pack("I", i))

def write_short(fh, s):
    fh.write(pack("H", s))

