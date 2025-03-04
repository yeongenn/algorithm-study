T = int(input())

for t in range(T):
    N, M = map(int, input().split())    # 1 ~ N번까지, M번의 명령
    status = list(map(int, input().split()))    # 기 상태

    for m in range(M):  # M번 명령에 걸쳐
        a, b, c = map(int, input().split())     # a : 2로 고정, b : 기준 번호, c : 비교 범위

        for i in range(1, c + 1):
            left, right = b - 1 - i, b - 1 + i
            if 0 <= left < N and 0 <= right < N:   # 범위 유효할 때만
                if status[left] == status[right]:
                    status[left] = 1 if status[left] == 0 else 0
                    status[right] = status[left]
        # print(status)     # 확인용

    print(f'#{t + 1}', *status)