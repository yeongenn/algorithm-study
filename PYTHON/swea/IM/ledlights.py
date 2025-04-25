import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

for t in range(T):
    N = int(input())
    pattern = list(map(int, input().split()))
    
    lights = [0] * N    # 최초 상태
    count = 0
        
    # for i, (p, l) in enumerate(zip(pattern, lights), 1):
    #     # if p == l:
    #     #     pass
    #     # else:
    #     if p != l:
    #         for j in range(i - 1, N, i):
    #             lights[j] = 1 if lights[j] == 0 else 0
    #         count += 1
    #     if lights == pattern:
    #         break

    # print(f'#{t + 1} {count}')

    for i in range(N):
        if pattern[i] != lights[i]:
            for j in range(i, N, i + 1):
                lights[j] = 1 - lights[j]   # 조명 스위치하기
            count += 1
        
        # 스위치하고 난 다음 패턴 일치하는지 확인
        if pattern == lights:
            break
    print(f'#{t + 1} {count}')