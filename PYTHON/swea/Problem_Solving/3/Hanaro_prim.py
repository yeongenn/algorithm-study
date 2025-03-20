import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

import heapq

def prim(tax):
    # 우선 순위 측정할 기준 같이 주기 - (비용, 노드번호)
    pq = [(0, 0)]       # 출발점 가중치는 0
    visited = [0] * N   # 방문 여부 기록
    min_cost = 0        # 최소 비용
    
    key = [float('inf')] * N    # 최소 비용 저장 리스트
    key[0] = 0
    
    while pq:
        # cost가 가장 저렴한 후보부터 나온다
        cost, node = heapq.heappop(pq)
        
        if visited[node]: continue      # 이미 방문했으면 지나가기 -> 사이클 방지
        
        visited[node] = 1
        min_cost += cost

        for next_node in range(N):
            if visited[next_node]:
                continue
        
            # cost 계산 : ((x 좌표 차이 ** 2) + (y 좌표 차이 ** 2)) * tax
            new_cost = ((x_list[next_node] - x_list[node]) ** 2 + \
                        (y_list[next_node] - y_list[node]) ** 2) * tax
            
            # 바로 pq에 넣을 것이 아니라
            # heapq.heappush(pq, (new_cost, next_node))
            
            # 기존보다 작은 비용으로 올 경우에만 pq에 넣기
            # 기존 비용을 기록하면서 진행 - key 리스트
            if new_cost < key[next_node]:
                key[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
            
    # return min_cost
    return round(min_cost)        
        

T = int(input())
for t in range(T):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())    # 실수로 받기
    
    print(f'#{t + 1} {prim(tax)}')