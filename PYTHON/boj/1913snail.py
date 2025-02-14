# N = int(input())
# # M = int(input())

# mx, my = 0, 0   # M의 좌표 구해서 출력
# snail = [[0] * N for _ in range(N)]
# turn = 0    # 돌아야 하는 턴수
# k = 1   # 달팽이가 그려야하는 숫자

# sx, sy = N // 2, N // 2 # 시작 좌표

# row, col = sx, sy
# dir = -1    # 좌표 이동용

# snail[sx][sy] = k
# k += 1
# # for i in range(turn, 0, -1):    # 다 돌면 끝
# for i in range(N):
#     for j in range(turn):
#         col += dir
#         snail[row][col] = k
#         k += 1

#     turn += 1

#     for j in range(turn):
#         row += dir
#         snail[row][col] = k
#         k += 1

#     dir *= (-1)

# print(snail)