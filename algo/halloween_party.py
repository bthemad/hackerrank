def count_pieces(n):
    fkm1 = 0
    fk = 0
    for i in range(2, n + 1):
        fk = fkm1 + i / 2
        fkm1 = fk
    return fk


t = int(raw_input())
for line in range(0, t):
    i = int(raw_input())
    print count_pieces(i)
