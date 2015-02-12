#!/usr/bin/env python
def print_int_list(l):
    print " ".join(map(str, l))


def count(a):
    len_a = len(a)
    c = [len_a] * 100
    for i in a:
        c[0:i] = map(lambda x: x - 1, c[0:i])
    return c


if __name__ == '__main__':
    n = input()
    a = []
    for i in range(n):
        j, _ = raw_input().strip().split(" ")
        a.append(int(j))
    c = count(a)
    print_int_list(c)
