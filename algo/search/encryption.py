#!/usr/bin/env python
import math


def count_rows_colums(l):
    r = int(math.floor(math.sqrt(l)))
    c = int(math.ceil(math.sqrt(l)))
    if (r * c < l):
        r += 1
    return r, c


def engrid(s, r, c):
    grid = []
    for i in range(r):
        row = []
        for j in range(c):
            if (i * (c - 1) + j + i < len(s)):
                row.append(s[i * (c - 1) + j + i])
            else:
                row.append("")
        grid.append(row)
    return grid


def encrypt(g, r, c):
    enc = []
    for j in range(c):
        for i in range(r):
            if (g[i][j] != ""):
                enc.append(g[i][j])
        enc.append(" ")
    return enc


if __name__ == '__main__':
    s = raw_input().strip()
    r, c = count_rows_colums(len(s))
    g = engrid(s, r, c)
    print "".join(encrypt(g, r, c)).strip()
