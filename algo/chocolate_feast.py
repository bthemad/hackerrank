#!/usr/bin/env python

def get_discount_chocolate(wrappers, discount):
    if wrappers < discount:
        return 0
    else:
        new_wrappers = wrappers / discount
        return new_wrappers + get_discount_chocolate(new_wrappers + wrappers % discount , discount)


if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        n, c, m = map(int, raw_input().strip().split(" "))
        total_chocolate = n / c
        total_chocolate += get_discount_chocolate(total_chocolate, m)
        print total_chocolate
