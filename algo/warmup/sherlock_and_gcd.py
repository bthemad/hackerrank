#!/usr/env/bin python
from fractions import gcd


def subset_with_gcd(s):
    if (reduce(gcd, s) == 1):
        return True
    return False


if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        length = int(raw_input())
        a = map(int, raw_input().strip().split(" "))
        if (subset_with_gcd((set(a)))):
            print 'YES'
        else:
            print 'NO'
