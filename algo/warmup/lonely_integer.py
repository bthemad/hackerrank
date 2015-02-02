#!/usr/bin/py
from collections import Counter


def lonelyinteger(a):
    cnts = Counter(a)
    for i, cnt in cnts.items():
        if (cnt == 1):
            return i

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
