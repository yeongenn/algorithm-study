import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

# UF 미사용 버전
def war(x, y):      # countries[x], countries[y]
    global alive
    side_1 = side_2 = 0
    
    for n in countries[x]:
        side_1 += people[n]
        
    for m in countries[y]:
        side_2 += people[m]
        
    if side_1 > side_2:
        for m in countries[y]:
            alive[m] = 0
    elif side_1 < side_2:
        for n in countries[x]:
            alive[n] = 0
    else:
        for k in (countries[x] + countries[y]):
            alive[k] = 0

T = int(input())

for t in range(T):
    N = int(input())    # 국가 수
    people = [0] + list(map(int, input().split()))
    countries = [[x] for x in range(N + 1)]      # 동맹국 리스트 관리
    alive = [1] * (N + 1)
    
    S = int(input())    # 동맹, 전쟁 상황 수
    for _ in range(S):
        situation, x, y = input().split()
        x = ord(x) - 64
        y = ord(y) - 64
        
        if situation == 'alliance':
            countries[x].append(y)
            countries[y].append(x)
        else:           # war
            war(x, y)
            
    print(f'#{t + 1} {sum(alive[1::])}')