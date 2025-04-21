import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    status = [2] + list(map(int, input().split()))
    for _ in range(M):
        I, J = map(int, input().split())    # i번째 돌 사이에 두고 마주보는 j개의 돌
        for j in range(1, J + 1):
            left_idx = I - j
            right_idx = I + j
            if left_idx > 0 and right_idx <= N and status[left_idx] == status[right_idx]:
                status[left_idx] = 1 - status[left_idx]
                status[right_idx] = status[left_idx]

    print(f'#{t + 1}', *status[1::])