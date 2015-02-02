#!/usr/bin/env python
import sys


def min_diff(a, k):
    min_diff = sys.maxint
    len_s = len(a)
    start = 0
    while (start + k < len_s):
        t_min_diff = a[start + k - 1] - a[start]
        start += 1
        if (t_min_diff < min_diff):
            min_diff = t_min_diff
    return min_diff


if __name__ == '__main__':
    n = int(raw_input())
    k = int(raw_input())
    candies = [input() for _ in range(0, n)]
    candies.sort()
    print min_diff(candies, k)
