from struct import *

def toint(bytes):
    return int.from_bytes(bytes, byteorder='big', signed = False)

def read_char(fh):
    return read(fh, "c", 1)

def read_int(fh):
    return read(fh, "I", 4)

def read_short(fh):
    return read(fh, "H", 2)

def read(fh, code, size):
    return unpack(">" + code, fh.read(size))[0]

def write_int(fh, i):
    fh.write(pack("I", i))

def write_short(fh, s):
    fh.write(pack("H", s))

