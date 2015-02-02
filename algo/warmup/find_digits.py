#!/usr/bin/env python


def find_digits(a):
    cnt = 0
    for d in map(int, str(a)):
        if d != 0 and a % d == 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
    t = input()
    for i in range(t):
        a = int(raw_input())
        print find_digits(a)
