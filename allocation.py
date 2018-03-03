#! /usr/bin/env python
# coding=utf-8


def main():
    l0 = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    for i in range(1, 102):
        if i % 6 == 0:
            l0.append(i)
        if i % 6 == 1:
            l1.append(i)
        if i % 6 == 2:
            l2.append(i)
        if i % 6 == 3:
            l3.append(i)
        if i % 6 == 4:
            l4.append(i)
        if i % 6 == 5:
            l5.append(i)

    print "张鹏飞+李艾鲜：" + str(l0)
    print "              " + str(l1)
    print "廖祖奇+张志威：" + str(l2)
    print "              " + str(l3)
    print "赖裕民+何  鹏：" + str(l4)
    print "              " + str(l5)


if __name__ == "__main__":
    main()
