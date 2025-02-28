T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    current = list(map(int, input().split()))   # 현재 상태 - 1 : 깃발 on, 0 : 깃발 다운
    # print(current)  # 확인용

    for i in range(M):  # M번 명령동안~
        a, b, c = map(int, input().split())

        # 기 바꿔야하는 마지막 사람 번호
        people = 0
        if b + c > N + 1:
            people = b + N - c - 1
        else:
            people = b + c - 1

        for j in range(b - 1, people):
            if current[j] == 0:
                current[j] = 1
            else:
                current[j] = 0
    result = current
    print(f'#{t + 1}', *result)