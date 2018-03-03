#! /usr/bin/env python
# coding=utf-8

xor_li = [0x53, 0x87, 0xf2, 0xa4, 0xe2, 0xb7]
infile = file("CM_2.exe", "rb")
outfile = file("out.exe", "wb")

def main():
    while True:
        infile.read(1)