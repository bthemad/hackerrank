#!/usr/bin/env python
def cut_the_sticks(a):
    while (len(a) > 0):
        cut_length = min(a)
        print sum(1 for elm in a if elm >= cut_length)
        a = [(elm - cut_length) for elm in a if (elm - cut_length > 0)]


if __name__ == '__main__':
    n = input()
    a = map(int, raw_input().strip().split(" "))
    cut_the_sticks(a)
