#!/usr/bin/env python


def fun(a):
    if a % 3 == 0:
        return int("".join(["5"] * a))
    elif (a % 3 == 1 and a >= 10):
        return int("".join(["5"] * (a - 10) + ["3"] * 10))
    elif (a % 3 == 2 and a >= 5):
        return int("".join(["5"] * (a - 5) + ["3"] * 5))
    return -1


if __name__ == '__main__':
    t = input()
    for i in range(t):
        a = int(raw_input())
        print fun(a)
