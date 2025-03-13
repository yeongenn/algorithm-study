import sys
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

def next(n):
    global cnt
    if n == N:
        cnt += 1
        return 
                
    for j in range(N):        
        if checked[j]:
            continue
        
        valid_in_diag = True
        for k in range(n):
            if abs(k - n) == abs(queens[k] - j): # 행과 열의 차이가 같으면 대각선 상
                valid_in_diag = False
                break
            
        if valid_in_diag:
            queens[n] = j    # 현재 행의 퀸 위치 마킹
            checked[j] = 1    # 체크 마킹
            next(n + 1)
            checked[j] = 0    # 해제

for t in range(T):
    N = int(input())
    checked = [0] * N   # 마킹 배열 없으니까 대각선 부분에서 문제
    queens = [99] * N   # 하나의 열에 퀸은 하나씩만 존재 가능 -> 1차원 리스트로도 가능
    cnt = 0
    
    next(0)
                     
    print(f'#{t + 1} {cnt}')