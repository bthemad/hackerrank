#!/usr/bin/env python
def print_int_list(l):
    print " ".join(map(str, l))


def counting(a):
    c = [0] * 100
    for i in a:
        c[i] += 1
    return c


def print_counter(c):
    for i, j in enumerate(c):
        if j > 0:
            s = "%i " % i * j
            print s.strip(),


if __name__ == '__main__':
    n = input()
    a = [int(i) for i in raw_input().strip().split()]
    c = counting(a)
    print_counter(c)
