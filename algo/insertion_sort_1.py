#!/bin/python
def print_shift(a, i, elm):
    res = []
    for j in range(0, i):
        res.append(a[j])
    res.append(elm)
    for k in range(i, len(a) - 1):
        res.append(a[k])
    return res


def insertionSort(a):
    ins = a[len(a) - 1]
    for i in range(len(a) - 2, -1, -1):
        if a[i] > ins:
            print " ".join(map(str, print_shift(a, i, a[i])))
        else:
            print " ".join(map(str, print_shift(a, i + 1, ins)))
            break
    if ins < a[0]:
        print " ".join(map(str, print_shift(a, 0, ins)))


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
