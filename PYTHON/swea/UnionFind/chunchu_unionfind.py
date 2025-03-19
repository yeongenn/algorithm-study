import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

for t in range(T):
    N = int(input())    # 국가 수
    people = [0] + list(map(int, input().split()))
    
    S = int(input())    # 동맹, 전쟁 상황 수
    for _ in range(S):
        situation, x, y = input().split()
        x = ord(x) - 64
        y = ord(y) - 64
        
        if situation == 'alliance':
            pass
        else:           # war
            pass
            
    print(f'#{t + 1}')