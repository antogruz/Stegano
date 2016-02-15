#!/usr/bin/env python

import bitsHandling
import re
from struct import *

def read_int(fh):
    return unpack("I", fh.read(4))[0]

def read_short(fh):
    return unpack("H", fh.read(2))[0]

def write_int(fh, i):
    fh.write(pack("I", i))

def write_short(fh, s):
    fh.write(pack("H", s))

class PictureHeader:
    def __init__(self):
        self.size = 0

    def parse_header(self, fh):
        self.size = unpack("I", fh.read(4))[0]
        self.width = unpack("I", fh.read(4))[0]
        self.height = unpack("I", fh.read(4))[0]
        self.plans = read_short(fh)
        self.colorBits = read_short(fh)
        self.compression = read_int(fh)
        self.pictureSize = read_int(fh)
        self.hres = read_int(fh)
        self.vres = read_int(fh)
        self.colors = read_int(fh)
        self.vipColors = read_int(fh)


# Files things
    def write(self, fh):

        fh.write(pack("I", self.size))
        fh.write(pack("I", self.width))
        fh.write(pack("I", self.height))
        write_short(fh, self.plans)
        write_short(fh, self.colorBits)
        write_int(fh, self.compression)
        write_int(fh, self.pictureSize)
        write_int(fh, self.hres)
        write_int(fh, self.vres)
        write_int(fh, self.colors)
        write_int(fh, self.vipColors)



    def print_header(self):
        print "Size : " + str(self.size)
        print "Width : " + str(self.width)
        print "height : " + str(self.height)
        print "Plans : " + str(self.plans)
        print "Bits per color : " + str(self.colorBits)
        print "Compression (0 for no) : " + str(self.compression)
        print "Picture size : " + str(self.pictureSize)
        print "Horizontal resolution (px/m) : " + str(self.hres)
        print "Vertical resolution (px/m) : " + str(self.vres)
        print "Palette colors : " + str(self.colors)
        print "Palette Important colors : " + str(self.vipColors)

class PictureData:
    def __init__(self, sizePix):
        self.sizePix = sizePix
        self.bitsHandler = bitsHandling.BitsHandler()
        self.red = []
        self.green = []
        self.blue = []
        self.pixels = [self.red, self.green, self.blue]

    def parseData(self, fh):
        rgb = fh.read(3)
        while rgb:
            (red, green, blue) = unpack("<BBB", rgb)
            self.red.append(red)
            self.green.append(green)
            self.blue.append(blue)
            self.bitsHandler.addBit(int(red))
            self.bitsHandler.addBit(int(green))
            self.bitsHandler.addBit(int(blue))
            if self.sizePix > 24:
                fh.read(1)
            rgb = fh.read(3)
        self.bitsHandler.printString()

    def swapColors(self):
        tmp = self.red[:]
        self.red = self.green[:]
        self.green = self.blue[:]
        self.blue = tmp[:]

# FILES THINGS
    def write(self, fh):
        for r, g, b in zip(self.red, self.green, self.blue):
            fh.write(pack("<BBB", r, g, b))



class Bitmap:
    # Header
    def parse_file_header(self, fh):
        self.magic_number = fh.read(2)
        self.size = unpack("I", fh.read(4))[0]
        self.reserved1 = fh.read(2)
        self.reserved2 = fh.read(2)
        self.content_offset = unpack("I", fh.read(4))[0]

    def parse_picture_header(self, fh):
        self.picture = PictureHeader()
        self.picture.parse_header(fh)

    def parse_picture_data(self, fh):
        self.data = PictureData(self.picture.colorBits)
        self.data.parseData(fh)

# FILES THINGS
    def writeFileHeader(self, fh):
        fh.write(self.magic_number)
        fh.write(pack("I", self.size))
        fh.write(self.reserved1)
        fh.write(self.reserved2)
        fh.write(pack("I", self.content_offset))

    def write(self, fh):
        self.writeFileHeader(fh)
        self.picture.write(fh)
        self.data.write(fh)

# PRINT THINGS
    def print_header(self):
        print "Magic number : " + self.magic_number + "\n"
        print "File size : " + str(self.size) + "\n"
        print "Reserved 1 : " + self.reserved1 + "\n"
        print "Reserved 2 : " + self.reserved2 + "\n"
        print "Content Offset : " + str(self.content_offset) + "\n"

    def print_picture_header(self):
        self.picture.print_header()


