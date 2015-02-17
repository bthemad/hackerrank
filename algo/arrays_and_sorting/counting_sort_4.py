def frequences(a):
    c = [0] * (max(a) + 1)
    for i in a:
        c[i] += 1
    return c


def starting_points(c):
    len_c = len(c)
    c.insert(0, 0)
    for idx in range(1, len_c):
        c[idx] = c[idx - 1] + c[idx]
    return c


def count_sort(a, b, c):
    length = len(a)
    o = [0] * (len(a))
    for idx, key in enumerate(a):
        if idx >= length / 2:
            o[c[key]] = b[idx]
        else:
            o[c[key]] = "-"
        c[key] += 1
    return o


if __name__ == '__main__':
    n = input()
    keys = []
    strings = []
    for i in range(n):
        k, s = raw_input().strip().split(" ")
        keys.append(int(k))
        strings.append(s)
    original_keys = keys[:]
    keys = starting_points(frequences(keys))
    result = count_sort(original_keys, strings, keys)
    print " ".join(map(str, result))
