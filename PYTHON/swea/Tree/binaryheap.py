import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

import heapq

T = int(input())

def sum_of_ancestors(idx):  # 힙 idx번째 노드의 조상 노드 합
    if idx <= 2:        # 1, 2번째 노드의 조상 노드는 트리의 최상위 노드 -> 0번째 노드
        return heap[0]
    else: 
        # idx 노드의 바로 위 조상 노드((idx - 1) // 2) 와 그 조상 노드의 조상 노드들의 합
        # 결국 누적 합 -> 1차원 리스트로 관리 가능?
        return heap[(idx - 1) // 2] + sum_of_ancestors((idx - 1) // 2)

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    
    # 힙 생성하기 - 최소힙
    heap = []
    while arr:
        k = arr.pop(0)
        heapq.heappush(heap, k)
    
    n = len(heap) - 1    # 마지막 노드
    
    result = sum_of_ancestors(n)

    print(f'#{t + 1} {result}')