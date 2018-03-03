#! /usr/bin/env python
# coding=utf-8

num = [0, 1, 1, 2, 8, 18, 59, 155, 460, 1276, 3672, 10357, 29533]

for n in num:
    print "{0:>20}".format(bin(n))