#!/bin/python
def print_int_list(l):
    print " ".join(map(str, l))


def partition(a, p):
    return ([x for x in a if x < p], p, [x for x in a if x > p])


def quickSort(a):
    if len(a) <= 1:
        return a
    left, p, right = partition(a, a[0])
    l = quickSort(left)
    r = quickSort(right)
    print_int_list(l + [p] + r)
    return l + [p] + r

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
