import sys
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

for t in range(T):
    N = int(input())    # 전선 수
    wires = []
    result = 0

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(len(wires)):
            X, Y = wires[i]
            if (X < A and Y > B) or (X > A and Y < B):
                result += 1
        wires.append((A, B))
    # print(wires)

    print(f'#{t + 1} {result}')