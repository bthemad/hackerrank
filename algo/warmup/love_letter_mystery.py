def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False


def make_palindrome(s):
    if is_palindrome(s):
        return 0
    op_count = 0
    for idx in range(0, len(s) / 2):
        diff = ord(s[-1 - idx]) - ord(s[idx])
        op_count += abs(diff)
    return op_count


t = int(raw_input())
for line in range(0, t):
    s = raw_input()
    print make_palindrome(s)
