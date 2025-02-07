# 250207 알고리즘 실습 문제
# List - 2

# # Sum
# for t in range(10):
#     TN = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]

#     sum_1 = 0
#     sum_2 = 0   # 우하향
#     sum_3 = 0   # 좌하향
#     # sum_4 = 0

#     max_s = 0

#     for i in range(100):
#         max_s = max(max_s, sum(arr[i]))
#         for j in range(100):
#             if i == j:
#                 sum_2 += arr[i][j]
#             if i + j == 99:
#                 sum_3 += arr[i][j]

#     max_s = max(max_s, sum_2, sum_3)

#     for j in range(100):
#         sum_4 = 0
#         for i in range(100):
#             sum_4 += arr[i][j]

#         max_s = max(max_s, sum_4)
#     print(f'#{t + 1} {max_s}')

#########################################################################################################

# # 파리 퇴치
# T = int(input())
# for t in range(T):
#     N, M = map(int, input().split())

#     flies = [list(map(int, input().split())) for _ in range(N)]
#     # print(flies)

#     result = 0

#     # 시작점에 대한 반복
#     # 파리채 크기만큼 반복 횟수 감소
#     for i in range(N - M + 1):
#         for j in range(N - M + 1):
#             row_sum = 0

#             # 파리채 크기만큼 반복
#             for k in range(M):
#                 # 한 줄 계산하는 코드
#                 row_sum += sum(flies[i + k][j : j + M])

#             # 파리채 한 번 치고난 다음 계산 끝
#             result = max(result, row_sum)


#     print(f'#{t + 1} {result}')

#########################################################################################################
