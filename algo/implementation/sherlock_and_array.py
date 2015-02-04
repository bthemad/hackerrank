#!/usr/bin/env python


def is_balanced_array(a):
    left_sum = 0
    right_sum = sum(a)
    for i in a:
        right_sum -= i
        if (left_sum == right_sum):
            return True
        left_sum += i
    return False


if __name__ == '__main__':
    t = input()
    for i in range(t):
        n = input()
        a = map(int, raw_input().strip().split(" "))
        if is_balanced_array(a):
            print 'YES'
        else:
            print 'NO'
