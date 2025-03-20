import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    
    if rx == ry: return
    
    # parents[ry] = rx        # 가장 기본 코드
    
    if rx < ry:             # 근데 이렇게 적는 이유? 디버깅용 or 문제 조건에 따라 설정하느라
        parents[ry] = rx
    else:
        parents[rx] = ry

T = int(input())
for t in range(T):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())    # 실수로 받기
    min_cost = 0
    
    parents = [i for i in range(N)]     # make_set
    
    # 1. 간선들 정보를 모두 저장
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            cost = ((x_list[i] - x_list[j]) ** 2 + \
                    (y_list[i] - y_list[j]) ** 2) * tax
            edges.append((i, j, cost))      # i에서 j까지 가는데 cost만큼 비용 발생
    
    # 2. 가중치 기준으로 오름차순 정렬
    edges.sort(key=lambda x : x[2])

    # 3. 사이클 검사하면서, 앞에서부터 간선 연결
    count = 0
    for u, v, w in edges:
        if find_set(u) != find_set(v):      # 사이클 발생하지 않았을 때만 진행
            union(u, v)
            min_cost += w
            
            # 조금의 최적화
            if count == N - 1:
                break
    
    print(f'#{t + 1} {round(min_cost)}')