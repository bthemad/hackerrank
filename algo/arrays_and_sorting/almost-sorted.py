#!/usr/bin/env python
def is_sorted(a):
    return all(a[i] <= a[i + 1] for i in xrange(len(a) - 1))


def is_sortable(a):
    b = a[:]
    default = (False, False, False, False)
    if len(a) == 2:
        a[0], a[1] = a[1], a[0]
        if is_sorted(a):
            return (True, "swap", 1, 2)

    i = 0
    while ((a[i] <= a[i + 1]) and (i < (len(a) - 2))):
        i += 1
    left_candidate = i
    i = left_candidate + 1
    if i == (len(a) - 1):
        right_candidate_swap = i
    else:
        while ((a[i] <= a[i + 1]) and i < (len(a) - 2)):
            i += 1
        right_candidate_swap = i + 1
    b = a[:]
    b[left_candidate], b[right_candidate_swap] = \
        b[right_candidate_swap], b[left_candidate]
    if is_sorted(b):
        return (True, "swap", left_candidate + 1, right_candidate_swap + 1)

    i = left_candidate + 1
    if i == (len(a) - 1):
        right_candidate_reverse = i
    else:
        while ((a[i] >= a[i + 1]) and i < (len(a) - 2)):
            i += 1
        right_candidate_reverse = i
    r = a[left_candidate:right_candidate_reverse + 1]
    if is_sorted(a[0:left_candidate] +
                 r[::-1] +
                 a[right_candidate_reverse + 1:]):
        return (True, "reverse",
                left_candidate + 1,
                right_candidate_reverse + 1
                )
    return default


if __name__ == '__main__':
    n = input()
    a = map(int, raw_input().strip().split(" "))
    if is_sorted(a):
        print "yes"
    else:
        sortable = is_sortable(a)
        if (sortable[0]):
            print "yes"
            print "%s %d %d" % (sortable[1:])
        else:
            print "no"
