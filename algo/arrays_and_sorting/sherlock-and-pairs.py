#!/usr/bin/env python


def count_duplicates(a):
    c = [0] * (max(a) + 1)
    for i in a:
        c[i] += 1
    return sum(combinations(x) for x in c if x > 1)


def combinations(n):
    return n * (n - 1)


if __name__ == '__main__':
    t = input()
    for i in range(t):
        n = input()
        a = map(int, raw_input().strip().split(" "))
        print count_duplicates(a)
