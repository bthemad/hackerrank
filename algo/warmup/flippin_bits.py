def flip_bits(a):
    return (~a + 2 ** 32)

t = int(raw_input())
for i in range(0, t):
    a = int(raw_input())
    print flip_bits(a)
