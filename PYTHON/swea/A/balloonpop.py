import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

from itertools import permutations

T = int(input())

for t in range(T):
    N = int(input())
    balloons = list(map(int, input().split()))
    
    orders = [p for p in permutations([i for i in range(N)], 4)]
    max_score = 0
        
    print(f'#{t + 1} {max_score}')