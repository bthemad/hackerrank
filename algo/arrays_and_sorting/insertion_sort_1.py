#!/bin/python
def insertionSort(l):
    elm = l[len(l) - 1]
    j = len(l) - 2
    while (l[j] > elm) and (j >= 0):
        l[j + 1] = l[j]
        j -= 1
        print " ".join(map(str, l))
    l[j + 1] = elm
    print " ".join(map(str, l))
    return l


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
