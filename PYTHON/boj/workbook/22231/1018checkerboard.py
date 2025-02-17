# M * N 체커보드

# 체커보드 검사하기
def check(i, j, g_checker, c_checker):
    count = 0
    for x in range(8):
        for y in range(8):
            if g_checker[i + x][j + y] != c_checker[x][y]:
                count += 1
#     # 리턴값은 변경 횟수
    return count


N, M = map(int, input().split())

checker = [list(input()) for _ in range(N)]
# print(checker)


w_checker = [['B'] * 8 for _ in range(8)]
# 8 * 8 체커보드
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            w_checker[i][j] = 'W'
        else:
            w_checker[i][j] = 'B'
# print(w_checker)

b_checker = list(map(list, zip(*w_checker)))[::-1]


min_result = 64
#
for i in range(N - 7):
    for j in range(M - 7):
        w_result = check(i, j, checker, w_checker)
        b_result = check(i, j, checker, b_checker)
        min_result = min(w_result, b_result, min_result)

print(min_result)