#!/usr/bin/env python
def get_flavour_indexes(flavours, money):
    flav_dict = {}
    for idx, f in enumerate(flavours):
        if f <= money:
            comp = money - f
            if comp in flav_dict:
                print flav_dict[comp] + 1, idx + 1
            else:
                flav_dict[f] = idx


if __name__ == '__main__':
    t = input()
    for i in range(t):
        money_amount = input()
        _ = input()
        flavours = map(int, raw_input().strip().split(" "))
        get_flavour_indexes(flavours, money_amount)
