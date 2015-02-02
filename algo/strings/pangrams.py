#!/usr/bin/env python
import string


pangram = False
alphabet = list(string.ascii_lowercase)
s = raw_input().strip()
for letter in s:
    if letter != " " and letter.lower() in alphabet:
        alphabet.remove(letter.lower())
    if len(alphabet) == 0:
        pangram = True
        break

if pangram:
    print 'pangram'
else:
    print 'not pangram'
