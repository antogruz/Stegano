#!/usr/bin/env python3
import sys

from parser import Parser
import png

def main():
    file = sys.argv[1]
    with open(file, "rb") as fh:
        picture = png.parse(fh)

    for color in picture.palette[0]["colors"]:
        print(chr(int(color[0])))

main()
