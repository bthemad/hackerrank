#!/usr/bin/env python
def print_map(a):
    for l in a:
        print "".join(map(str, l))


def is_cavity(mmap, i, j):
    elm = mmap[i][j]
    if (elm > mmap[i + 1][j]
            and elm > mmap[i - 1][j]
            and elm > mmap[i][j + 1]
            and elm > mmap[i][j - 1]):
        return True
    return False


def cavity_map(a):
    map_len = len(a[0])
    cavities = []
    for i in range(1, map_len - 1):
        for j in range(1, map_len - 1):
            if(is_cavity(a, i, j)):
                cavities.append((i, j))
    for (i, j) in cavities:
        a[i][j] = 'X'
    return a


if __name__ == '__main__':
    n = input()
    mmap = []
    for i in range(n):
        line = map(int, list(raw_input().strip()))
        mmap.append(line)
    c = cavity_map(mmap)
    print_map(c)
