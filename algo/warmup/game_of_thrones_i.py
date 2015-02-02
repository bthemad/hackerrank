#!/usr/bin/env python
from collections import Counter


def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False


def can_be_palindrome(s):
    if (is_palindrome(s)):
        return True

    c = Counter(s)
    odd_count = 0
    for _, cnt in c.iteritems():
        if (cnt % 2 == 0):
            continue
        else:
            odd_count += 1

        if odd_count > 1:
            return False
    return True


string = raw_input()
found = can_be_palindrome(string)
if not found:
    print("NO")
else:
    print("YES")
