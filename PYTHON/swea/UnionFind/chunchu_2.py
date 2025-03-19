import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

# UF ver.
def find_captain(x):        # 대장 찾기
    if captain[x] != x:
        captain[x] = find_captain(captain[x])
    return captain[x]

def alliance(x, y):
    rx = find_captain(x)
    ry = find_captain(y)
    
    allies[x].append(y)
    allies[y].append(x)
    
    # 연합군 인구 수 누적하기
    if rx < ry:     # 인덱스 작은 쪽이 대장
        captain[ry] = rx
        people[rx] = people[x] + people[y]
    else:
        captain[rx] = ry
        people[ry] = people[x] + people[y]

def war(x, y):
    cx = find_captain(x)
    cy = find_captain(y)
    
    # 각각 캡틴 구해서 captain 리스트에서 같은 캡틴으로 연결된 나라 전부 0 처리하는 방법도 O
    
    if people[cx] < people[cy]:
        for country in allies[cx]:
            alive[country] = 0
    elif people[cx] > people[cy]:
        for country in allies[cy]:
            alive[country] = 0
    else:
        for country in (allies[cx] + allies[cy]):
            alive[country] = 0
            
T = int(input())

for t in range(T):
    N = int(input())
    people = [0] + list(map(int, input().split()))      # -> 인덱스를 대장으로 하는 연합국 총 인구 수로 활용할거임
    
    captain = [x for x in range(N + 1)]
    allies = [[x] for x in range(N + 1)]
    alive = [1] * (N + 1)
    
    S = int(input())
    for _ in range(S):
        situation, x, y = input().split()
        x = ord(x) - 64
        y = ord(y) - 64
        
        if situation == 'alliance':
            alliance(x, y)
        else:           # 전쟁이야
            war(x, y)
        
    print(f'#{t + 1} {sum(alive[1::])}')