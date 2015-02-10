#!/usr/bin/env python
insertion_sort_swaps = 0
quick_sort_swaps = 0


def insertion_sort(l):
    global insertion_sort_swaps

    for i in range(1, len(l)):
        j = i - 1
        elm = l[i]
        while (l[j] > elm) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1
            insertion_sort_swaps += 1
        l[j + 1] = elm
    return l


def partition(a, start, stop):
    global quick_sort_swaps

    pivot_idx = stop - 1
    swap_idx = start

    for i in range(start, stop - 1):
        if a[i] < a[pivot_idx]:
            a[i], a[swap_idx] = a[swap_idx], a[i]
            swap_idx += 1
            quick_sort_swaps += 1

    a[pivot_idx], a[swap_idx] = a[swap_idx], a[pivot_idx]
    quick_sort_swaps += 1

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
    ar = [int(i) for i in raw_input().strip().split()]
    qar = ar[:]
    iar = ar[:]
    quicksort(qar)
    insertion_sort(iar)
    print insertion_sort_swaps - quick_sort_swaps
