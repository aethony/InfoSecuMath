#! /usr/bin/env python
# coding=utf-8
# F2域上的多项式带余除法的实现


def division(str1, str2):
    if str2[0] == 0 or str1[0] == 0:
        print "Invalid parameter!"
        exit()
    l1 = list(str1)
    l2 = list(str2)
    quot_len = len(l1) - len(l2) - 1
    quotient = []
    remainder = []
    windowsize = len(l2)
    print len(l2)
    xor = l1[0:windowsize - 1]
    quot_len -= 1
    quotient.append('1')  # 被除数首位为1，商首位为1
    xorl = xorli(xor, l2)
    if xorl == '0':
        xorl = ''
    offset = windowsize - len(xorl)

def xorli(l1, l2):
    b1 = ''.join(l1)
    b2 = ''.join(l2)
    return str(bin(int(b1, 2) ^ int(b2, 2))[2:])


def main():
    # str1 = "100101"
    # str2 = "11"
    # division(str1, str2)
    st = ['1', '1']
    st2 = ['1', '1']
    print xorli(st, st2)


if __name__ == "__main__":
    main()
