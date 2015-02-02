#!/usr/bin/env python
import math


def is_pure_square(n):
    sq = math.sqrt(n)
    return int(sq) * int(sq) == n


def count_squares(a, b):
    diff = int(math.sqrt(b) - int(math.sqrt(a)))
    if (is_pure_square(a)):
        return diff + 1
    return diff


if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        a, b = map(int, raw_input().strip().split(" "))
        print count_squares(a, b)
