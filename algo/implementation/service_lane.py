#!/usr/bin/env python
def get_veichle_type(a, i, j):
    return min(a[i:j + 1])


if __name__ == '__main__':
    n, t = map(int, raw_input().strip().split(" "))
    a = map(int, raw_input().strip().split(" "))
    for i in range(t):
        i, j = map(int, raw_input().strip().split(" "))
        print get_veichle_type(a, i, j)
