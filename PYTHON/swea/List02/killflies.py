# 파리 퇴치
T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    flies = [list(map(int, input().split())) for _ in range(N)]
    # print(flies)

    result = 0

    # 시작점에 대한 반복
    # 파리채 크기만큼 반복 횟수 감소
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            row_sum = 0

            # 파리채 크기만큼 반복
            for k in range(M):
                # 한 줄 계산하는 코드
                row_sum += sum(flies[i + k][j : j + M])

            # 파리채 한 번 치고난 다음 계산 끝
            result = max(result, row_sum)


    print(f'#{t + 1} {result}')