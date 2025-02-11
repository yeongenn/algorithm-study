T = int(input())

for t in range(T):
    # N : 돌의 수, M : 뒤집기 횟수
    N, M = map(int, input().split())

    status = list(map(int, input().split()))
    # i번째 돌 사이 두고 마주보는 j개 돌
    li = [list(map(int, input().split())) for _ in range(M)]

    # print(li)
    for i, j in li:
        for k in range(1, j + 1):
            if i - 1 - k >= 0 and i - 1 + k < N:
                if status[i - 1 - k] == status[i - 1 + k]:
                    status[i - 1 - k] = 1 if status[i - 1 - k] == 0 else 0
                    # status[i - 1 + k] = 1 if status[i - 1 + k] == 0 else 0
                    status[i - 1 + k] = status[i - 1 - k]   # 한번에 변경될테니까

    print(f'#{t + 1}', *status)