#!/usr/bin/env python3

import re
from bits import write_byte

def main():
    with open("files/crypto.txt", "r") as fh:
        text = fh.read()

    text = remove_first_lines(text, 2)
    text = remove_last_lines(text, 2)

    with open("ccc", "wb") as out:
        for b in swap2(read_bytes(text)):
            write_converted(out, b)

def remove_first_lines(text, n):
    return "\n".join(text.split("\n")[n:])

def remove_last_lines(text, n):
    array = text.split("\n")
    tokeep = len(array) - n
    return "\n".join(array[0:tokeep])

def read_bytes(text):
    return re.split("\s+", text)

def write_converted(out, b):
    write_byte(out, int(b, 16))

def swap2(array):
    out = []
    for i in range(int(len(array) / 2)):
        out.append(array[2 *i + 1])
        out.append(array[2 * i])

    return out


main()
