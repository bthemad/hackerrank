#!/usr/bin/env python
def print_int_list(l):
    print " ".join(map(str, l))


def counting(a):
    c = [0] * 100
    for i in a:
        c[i] += 1
    return c


if __name__ == '__main__':
    n = input()
    a = [int(i) for i in raw_input().strip().split()]
    print_int_list(counting(a))
