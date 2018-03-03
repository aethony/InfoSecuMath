#! /usr/bin/env python
# coding=utf-8

import random
import math

count = 0


def ModExp(n, k, m):
    """This method is use to calculate the big Modular Exponentiation"""
    a = list(bin(k))[2:]
    a.reverse()
    s = 1
    for i in a:
        if i == '1':
            s = (s * n) % m
        n = (n * n) % m
    return s


def euclid(a, b):
    """(a,b)"""
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def getst1(n):
    """This method is used to get s and t."""
    global count
    if n % 2 == 0:
        count += 1
        return getst1(n / 2)
    else:
        return count, n


def miller_rabin_test(n, k):
    """miller_rabin_test is miller rabin test"""
    i = 1
    if n < 3 or k < 1 or n % 2 == 0:
        print "Oops, number or k is invalid!"
        exit()
    global count
    count = 0
    s, t = getst1(n - 1)
    while i <= k:
        b = random.randint(2, n - 2)
        print "{0}'s test, b is {1}".format(i, b)
        d = euclid(b, n)
        if d > 1:
            print "This number not pass the test!"
            exit()

        j = 0
        try:
            r = math.pow(b, t) % n
        except OverflowError:
            print "The number is too big.But we can use another method!"
            r = ModExp(b, t, n)
        if r == 1 or r == -1:
            pass
        else:
            while j < s:
                j += 1
                r = (r * r) % n
                if r == -1:
                    break
        i += 1
    print "Congratulation!!The fake's passing rate is {0}".format(1 / float(math.pow(4, k)))


if __name__ == "__main__":
    miller_rabin_test(71, 9)
    # print ModExp(15, 5, 113)
