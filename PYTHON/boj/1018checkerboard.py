# M * N 체커보드
# N, M = map(int, input().split())

# checker = [list(input()) for _ in range(N)]
# print(checker)


blank = [['B'] * 8 for _ in range(8)]
# 8 * 8 체커보드
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            blank[i][j] = 'W'
        else:
            blank[i][j] = 'B'
print(blank)
             

# 비교
# for i in range(M - 7):
#     for j in range(N - 7):


