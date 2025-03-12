import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

import copy

T = int(input())

def next(idx, n):   # idx : 이전에 퀸 뒀던 자리 열 인덱스, n : 행 인덱스
    global cnt
    if n == N - 1:
        cnt += 1
        return 
                
    for j in range(N):
        if idx == j:
            continue
        
        if abs(idx - j) == 1:
            continue
        
        if not queen[j]:
            queen[j] = 1
            next(j, n + 1)
            queen[j] = 0

for t in range(T):
    N = int(input())
    # board = [[0] * N for _ in range(N)]
    queen = [0] * N
    cnt = 0
    
    for i in range(N):
        queen[i] = 1        # 마킹 
        next(i, 0)
        queen[i] = 0
                     
    print(f'#{t + 1} {cnt}')