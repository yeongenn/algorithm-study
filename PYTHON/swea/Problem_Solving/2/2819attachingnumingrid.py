import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())    

for t in range(T):
    grid = [list(input().split()) for _ in range(4)]
    print(grid)
    
    print(f'#{t + 1}')