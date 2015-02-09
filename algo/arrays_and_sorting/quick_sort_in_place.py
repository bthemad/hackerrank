#!/usr/bin/env python
def print_int_list(l):
    print " ".join(map(str, l))


def partition(a, start, stop):
    pivot_idx = stop - 1
    swap_idx = start

    for i in range(start, stop - 1):
        if a[i] < a[pivot_idx]:
            a[i], a[swap_idx] = a[swap_idx], a[i]
            swap_idx += 1

    a[pivot_idx], a[swap_idx] = a[swap_idx], a[pivot_idx]

    print_int_list(a)
    return swap_idx


def quicksort_it(a, start, stop):
    if stop - start > 1:
        pivot_idx = partition(a, start, stop)
        quicksort_it(a, start, pivot_idx)
        quicksort_it(a, pivot_idx + 1, stop)
    else:
        return False


def quicksort(a):
    quicksort_it(a, 0, len(a))


if __name__ == '__main__':
    n = input()
    a = map(int, raw_input().strip().split(" "))
    quicksort(a)
