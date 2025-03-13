import sys
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

for t in range(T):
    A, B, C = map(int, input().split())
    result = 0      # 최소 사탕 개수
    while A != 0 and B != 0 and C != 0:
        
        if A < B < C:
            break
        else: 
            while B >= C:
                B -= 1
                result += 1
            
            while A >= B:
                A -= 1
                result += 1

    else:
        result = -1
    
    print(f'#{t + 1} {result}')