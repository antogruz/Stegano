#!/usr/bin/env python3
from tests import assert_equals

def tests():
    assert_equals(0b0, low_bit(0x0))
    assert_equals(0, bits_to_byte([0, 0, 0, 0, 0, 0, 0, 0]))
    assert_equals(1, bits_to_byte([0, 0, 0, 0, 0, 0, 0, 1]))
    assert_equals(8, bits_to_byte([0, 0, 0, 0, 1, 0, 0, 0]))

def low_bit(n):
    return n & 1

def bits_to_byte(bits):
    byte = 0
    for b in bits:
        byte *= 2
        byte += b
    return byte

if __name__ == "__main__" :
    tests()
