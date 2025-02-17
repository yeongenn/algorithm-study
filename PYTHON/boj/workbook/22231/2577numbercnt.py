A, B, C = [int(input()) for _ in range(3)]

M = str(A * B * C)
dat = [0] * 10
for m in M:
    dat[int(m)] += 1

for n in dat:
    print(n)