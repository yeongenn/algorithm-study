import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
        
    can_create = False
    for s in sample:
        if len(passcode) == 0:
            can_create = True
            break
        
        if s == passcode[0]:
            passcode.pop(0)
    
    print(f'#{t + 1} {int(can_create)}')