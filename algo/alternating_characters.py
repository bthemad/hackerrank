#!/usr/bin/env python
def number_of_deletions(s):
    if (len(s) == 0):
        return 0

    deletions = 0
    prev_letter = s[0]
    for letter in s[1:]:
        if letter == prev_letter:
            deletions += 1
        prev_letter = letter

    return deletions

t = int(raw_input())
for i in range(0, t):
    s = raw_input()
    print number_of_deletions(s)
