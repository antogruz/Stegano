from struct import *

class BitsHandler:
    def __init__(self):
        self.bytes = ""
        self.bits = []

    def packByte(self):
        val = 0
        for i in range(8):
            val *= 2
            val += self.bits[i] & 1
        self.bytes += pack("B", val)
        self.bits = []

    def addBit(self, bit):
        if len(self.bits) >= 8:
            raise Exception("More than 8 bits !")
        self.bits.append(bit & 1)

        if len(self.bits) == 8:
            self.packByte()

    def printString(self):
        print self.bytes
