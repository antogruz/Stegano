#!/usr/bin/env python3
import sys

from parser import Parser
from bits import toint, tochar, read_char

class Picture:
    def __init__(self):
        self.header = []
        self.palette = []
        self.data = []
        self.end = []

def parse(fh):
    Parser(fh).check("signature", [137, 80, 78, 71, 13,10,26,10], toint)
    picture = Picture()
    picture.header = parse_ihdr(fh)

    while len(picture.end) == 0:
        parse_chunk(fh, picture)

    return picture

def parse_ihdr(fh):
    p = Parser(fh)
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
    read_crc(p)
    return p.d

def parse_palette(fh, size):
    assert size % 3 == 0
    colors_count = int(size / 3)
    return [parse_color(fh) for i in range(colors_count)]

def parse_color(fh):
    return [read_color_component(fh) for i in range(3)]

def read_color_component(fh):
    return toint(read_char(fh))

def parse_chunk(fh, picture):
    p = Parser(fh)
    p.read_number("size", 4)
    p.read_string("type", 4)
    p.d["seek"] = fh.tell()
    type = p.d["type"]
    size = p.d["size"]
    if type == "IEND":
        picture.end.append(p.d)
    elif type == "IDAT":
        picture.data.append(p.d)
        p.skip(size)
    elif type == "PLTE":
        p.d["colors"] = parse_palette(fh, size)
        picture.palette.append(p.d)
    else:
        p.skip(size)

    read_crc(p)

def read_crc(p):
    p.skip(4)

