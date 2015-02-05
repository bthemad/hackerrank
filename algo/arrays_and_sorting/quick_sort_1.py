#!/bin/python
def partition(a):
    p = a[0]
    a = a[1:]
    return [x for x in a if x < p] + [p] + [x for x in a if x >= p]

m = input()
a = [int(i) for i in raw_input().strip().split()]
print " ".join(map(str, partition(a)))
