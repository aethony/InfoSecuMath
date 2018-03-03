#! /usr/bin/env python
# coding=utf-8
import random
import math
import Euclid_algorithm

def produce_odd(start, end):
    return random.randrange(start + 1, end, 2)


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


class RSA:
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19]
    count = 0
    version = 1.0
    e = 17

    def __init__(self):
        pass

    def small_primes_test(self, num):
        for small_prime in self.small_primes:
            if num % small_prime == 0:
                print "\t\t\033[1;31;0m[-]Small primes test not passed."
                print "\t\t\033[1;31;0m[-]The number %d can be divided by \033[1;37;0m%d" % (num, small_prime)
                return False
        return True

    def getst1(self, n):
        if n % 2 == 0:
            self.count += 1
            return self.getst1(n / 2)
        else:
            return self.count, n

    def miller_rabin_test(self, n):
        index = 1
        self.count = 0
        s, t = self.getst1(n - 1)
        while index <= 5:
            b = random.randint(2, n - 2)
            print "\t\t\t{0}'s test, b is {1}".format(index, b)
            d = euclid(b, n)
            if d > 1:
                print "\t\t\t\033[1;31;0m[-]This number not pass the test!"
                return False

            j = 0
            try:
                r = math.pow(b, t) % n
            except OverflowError:
                print "\t\t\tThe number is too big.But we can use another method!"
                r = ModExp(b, t, n)
            if r == 1 or r == -1:
                pass
            else:
                while j < s:
                    j += 1
                    r = (r * r) % n
                    if r == -1:
                        break
            index += 1
        print "\t\t[+]Miller rabin test passed!The fake's passing rate is {0}".format(1 / float(math.pow(4, 5)))
        return True

    def primes_test(self, num):
        print "\t\t[*]Primes test begin."
        if self.small_primes_test(num):
            print "\t\t[+]Small primes test passed."
        else:
            return False
        if num > 361:
            print "\t\t[*]Miller rabin test begin."
            if self.miller_rabin_test(num):
                return True
            else:
                return False

        return True

    def produce_prime1(self, num, start, end):
        print "\t[+]The number of test is %d" % num
        if self.primes_test(num):
            return num
        else:
            num += 2
            if num > end:
                num = end - num + start
            return self.produce_prime1(num, start, end)

    def produce_prime(self, start, end):
        p = produce_odd(start, end)
        return self.produce_prime1(p, start, end)

    def encode(self):
        print "[*]First prime is producing" + "." * 100
        p1 = self.produce_prime(2 ** 6, 2 ** 7)
        print "\t[*]The first prime is %d" % p1
        print "[*]Second prime is producing" + "." * 100
        p2 = self.produce_prime(2 ** 14, 2 ** 15)
        print "\t[*]The second prime is %d" % p2
        n = p1 * p2 - 1



    def decode(self):
        pass


if __name__ == "__main__":
    n = RSA()
    n.encode()
