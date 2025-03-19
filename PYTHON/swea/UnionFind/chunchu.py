import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]

def alliance(x, y):
    pass

def war(x, y):      # countries[x], countries[y]
    pass

T = int(input())

for t in range(T):
    N = int(input())    # 국가 수
    people = [0] + list(map(int, input().split()))
    # print(people)
    parents = [x for x in range(N + 1)]
    countries = [[] for _ in range(N + 1)]      # 동맹국 리스트 관리
    alive = [1] * (N + 1)
    
    S = int(input())    # 동맹, 전쟁 상황 수
    for _ in range(S):
        situation, x, y = input().split()
        x = ord(x) - 64
        y = ord(y) - 64
        # print(x, y)
        
        if situation == 'alliance':
            alliance(x, y)
            pass
        else:           # war
            war(x, y)
            pass
    
    print(f'#{t + 1}', *alive)