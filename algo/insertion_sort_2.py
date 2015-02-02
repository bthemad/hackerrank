#!/bin/python
def insertionSort(l):
    for i in range(1, len(l)):
        j = i - 1
        elm = l[i]
        while (l[j] > elm) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1
            print elm, l
        l[j + 1] = elm
        print " ".join(map(str, l))
    return l


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
