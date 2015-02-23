#!/usr/bin/env python


def rotate_array(a, i):
    initial_length = len(a)
    a.extend(a)
    if i > initial_length:
        i = i % initial_length
    return a[(initial_length - i):(initial_length * 2 - i)]


if __name__ == '__main__':
    n, k, q = map(int, raw_input().strip().split(" "))
    a = map(int, raw_input().strip().split(" "))
    ra = rotate_array(a, k)
    for j in range(q):
        i = input()
        print ra[i]
