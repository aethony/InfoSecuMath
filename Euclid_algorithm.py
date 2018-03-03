# coding=utf-8
import sys

class Euclid:
    """欧几里得算法中的辗转相除法和逆向迭代求线性组合，以及扩展的欧几里得算法求线性组合"""

    def __init__(self, num1, num2):
        """求出最大公约数和p、c两个list"""
        self.num1 = num1
        self.num2 = num2
        self.c = []
        self.p = []
        self.q = []

        while self.num2 != 0:
            self.c.append(self.num1)
            self.p.append(self.num2)
            x = self.num1 / self.num2
            self.q.append(x)
            r = self.num1 % self.num2
            print "{0} = {1} x {2} + {3}".format(self.num1, x, self.num2, r)
            self.num1 = self.num2
            self.num2 = r

        self.q.pop(-1)
        print "最大公约数是:  {0}\n".format(self.num1)

    def method1(self):
        """逆向迭代求线性组合"""
        print "逆向迭代："
        print "{0:<4}".format(self.num1)
        self.c.reverse()
        self.p.reverse()
        index = 1
        if len(self.c) == 1:
            index = 0
        c_x = 1
        p_x = -(self.c[index] / self.p[index])

        while len(self.c) - 1 >= index:
            print "{0:>8}{1}x({2})+{3}x({4})".format("=", self.c[index], c_x, self.p[index], p_x)
            if len(self.c) - 1 == index:
                break
            tmp = c_x
            c_x = p_x
            p_x = tmp - (self.c[index + 1] / self.p[index + 1] * p_x)
            index += 1

    def cal(self, s):
        """计算并输出扩展欧几里得算法的过程"""
        if s == "s":
            a1 = 1
            a2 = 0
        else:
            a1 = 0
            a2 = 1

        length = len(self.q)
        i = 0
        print "{0}0={1}\n{2}1={3}".format(s, a1, s, a2)
        while length - 1 >= i:
            print "{0}={1}-({2})x{3}={4}".format(s + str(i + 2), a1, a2, self.q[i], a1 - a2 * self.q[i])
            if i >= length:
                break
            tmp = a1
            a1 = a2
            a2 = tmp - a2 * self.q[i]
            i += 1

    def method2(self):
        """扩展的欧几里得算法"""
        print "sn的求解过程"
        self.cal("s")
        print "tn的求解过程"
        self.cal("t")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "仅需要两个数字！"
        sys.exit()

    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        e = Euclid(int(sys.argv[1]), int(sys.argv[2]))
        e.method1()
        e.method2()
    else:
        print "仅需要数字！"
