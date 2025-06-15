import sys
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

T = int(input())

# 마지막 N개의 비트가 모두 1인지 체크

for t in range (T):
    N, M = map(int, input().split())
    result = ''
    
    bit = (1 << N) - 1
    result = 'ON' if (M & bit) == bit else 'OFF'
    
    print(f'#{t + 1} {result}')