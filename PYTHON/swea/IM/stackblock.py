import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

for t in range(T):
    N, M1, M2 = map(int, input().split())
    blocks = list(map(int, input().split()))
    
    blocks.sort(reverse=True)
    
    m = [i + 1 for i in range(M1)] + [i + 1 for i in range(M2)]
    m.sort()
    print(m)
    
    sum = 0    
    for x, y in zip(blocks, m):
        sum += (x * y)
    
    print(f'#{t + 1} {sum}')