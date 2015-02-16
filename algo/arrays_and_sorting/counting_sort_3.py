#!/usr/bin/env python
def print_int_list(l):
    print " ".join(map(str, l))


def frequences(a):
    c = [0] * (max(a) + 1)
    for i in a:
        c[i] += 1
    return c


def starting_points(c):
    len_c = len(c)
    for idx in range(1, len_c):
        c[idx] = c[idx - 1] + c[idx]
    return c


if __name__ == '__main__':
    n = input()
    a = []
    for i in range(n):
        j, _ = raw_input().strip().split(" ")
        a.append(int(j))
    c = starting_points(frequences(a))
    print_int_list(c)
