#!/bin/python
def maxXor(l, r):
    xor = l ^ l
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            xor = max(xor, i ^ j)
    return xor

_l = int(raw_input())
_r = int(raw_input())
res = maxXor(_l, _r)
print(res)
