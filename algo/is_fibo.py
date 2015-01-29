#!/usr/bin/env python


def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_fibo(a):
    i = 0
    g = fib_generator()
    while True:
        i = g.next()
        if a == i:
            return True
        if i > a:
            return False


if __name__ == '__main__':
    t = input()
    for i in range(t):
        a = int(raw_input())
        if is_fibo(a):
            print "IsFibo"
        else:
            print "IsNotFibo"
