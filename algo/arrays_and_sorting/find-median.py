#!/usr/bin/env python
def partition(a, start, stop):
    pivot_idx = stop - 1
    swap_idx = start

    for i in range(start, stop - 1):
        if a[i] < a[pivot_idx]:
            a[i], a[swap_idx] = a[swap_idx], a[i]
            swap_idx += 1

    a[pivot_idx], a[swap_idx] = a[swap_idx], a[pivot_idx]
    return swap_idx


def find_median_it(a, start, stop):
    median_pos = len(a) / 2
    i = 0
    while (True):
        i += 1
        pivot_idx = partition(a, start, stop)
        if pivot_idx == median_pos:
            return a[pivot_idx]
        elif pivot_idx > median_pos:
            stop = pivot_idx
        else:
            start = pivot_idx + 1
    return a[pivot_idx]


def find_median(a):
    return find_median_it(a, 0, len(a))


if __name__ == '__main__':
    n = input()
    a = map(int, raw_input().strip().split(" "))
    print find_median(a)
