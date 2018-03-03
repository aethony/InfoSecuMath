#! /usr/bin/env python
# coding=utf-8

def test11(x):
    return (x * x * x + x + 1) % 11


if __name__ == "__main__":
    for i in range(1, 11):
        print test11(i)
