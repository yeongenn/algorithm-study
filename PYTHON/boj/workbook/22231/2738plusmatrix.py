N, M = map(int, input().split())

m_1 = [list(map(int, input().split())) for _ in range(N)]
m_2 = [list(map(int, input().split())) for _ in range(N)]

# result_m = [[0] * N] * M    # 굳이 배열에 담을 필요 X

for i in range(N):
    for j in range(M):
        print(m_1[i][j] + m_2[i][j], end=" ")
    print()


