#!/usr/bin/env python
from bisect import bisect_left


def binary_search(a, elm):
    low_idx = 0
    high_idx = len(a) - 1
    while (low_idx <= high_idx):
        mid_idx = (low_idx + high_idx) / 2
        if elm == a[mid_idx]:
            return mid_idx
        elif elm > a[mid_idx]:
            low_idx = mid_idx + 1
        elif elm < a[mid_idx]:
            high_idx = mid_idx - 1
    return False


def pythonic_binary_search(a, elm):
    idx = bisect_left(a, elm)
    if (idx < len(a) and a[idx] == elm):
        return idx
    else:
        return False


def get_flavour_indexes(flavours, money):
    sorted_flavours = sorted(flavours)
    for f in sorted_flavours:
        if (f <= money):
            compliment = money - f
            compliment_flavours = sorted_flavours[::]
            compliment_flavours.remove(f)
            c_idx = pythonic_binary_search(compliment_flavours, compliment)
            if (c_idx is not False):
                for idx, val in enumerate(flavours):
                    if (val == f or val == compliment):
                        print idx + 1,
                print ""
                break


if __name__ == '__main__':
    t = input()
    for i in range(t):
        money_amount = input()
        _ = input()
        flavours = map(int, raw_input().strip().split(" "))
        get_flavour_indexes(flavours, money_amount)
