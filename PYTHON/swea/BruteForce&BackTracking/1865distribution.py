import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\swea\\input.txt", "r")

T = int(input())

def get_best(n, percentage):
    global result
    
    if n == N:  
        result = max(result, percentage)
        return
    
    if percentage <= result:    # 1
        return
    
    for j in range(N):
        if arr[n][j] == 0 or checked[j]:    # 2
            continue
        
        # percentage *= (arr[n][j] / 100)   # 미리 곱해주면 틀립니다~
        checked[j] = 1
        get_best(n + 1, percentage * (arr[n][j] / 100))
        checked[j] = 0  

for t in range(T):
    N = int(input())    # 직원 수, 해야할 일
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    checked = [0] * N
    
    get_best(0, 1)

    print(f'#{t + 1} {result * 100:.6f}')