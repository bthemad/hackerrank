#!/usr/bin/py

if __name__ == '__main__':
    t = input()
    for i in range(t):
        n = int(raw_input())
        a = int(raw_input())
        b = int(raw_input())
        start = min(a, b) * (n - 1)
        end = max(a, b) * (n - 1)
        diff = abs(a - b)
        paths = set()
        if diff == 0:
            print start,
        else:
            while (start <= end):
                paths.add(start)
                start += diff
        print " ".join(map(str, sorted(paths)))
