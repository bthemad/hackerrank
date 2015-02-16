def frequences(a):
    c = [0] * (max(a) + 1)
    for i in a:
        c[i] += 1
    return c


def starting_points(c):
    len_c = len(c)
    for idx in range(1, len_c):
        c[idx] = c[idx - 1] + c[idx]
    return c


def count_sort(a, c):
    o = [0] * (len(a))
    for i in a:
        print c[i]
        o[c[i] - 1] = i
        c[i] -= 1
        print o
    return o


a = [4, 3, 0, 1, 5, 1, 2, 4, 2, 4]
print a
c = frequences(a)
for key, freq in enumerate(c):
    print "%d -> %d" % (key, freq)
print c
c = starting_points(c)
for key, freq in enumerate(c):
    print "%d -> %d" % (key, freq)
print c
print count_sort(a, c)
