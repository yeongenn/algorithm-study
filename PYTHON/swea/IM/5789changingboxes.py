import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

for t in range(T):
    N, Q = map(int, input().split())
    boxes = [0] * (N + 1)
    for i in range(1, 1 + Q):
        L, R = map(int, input().split())
        boxes[L:R + 1] = [i] * (R - L + 1)

    print(f'#{t + 1}', *boxes[1::])