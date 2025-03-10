import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

import heapq

T = int(input())

def sum_of_ancestors(idx):
    if idx <= 2:
        return heap[0]
    else: 
        return heap[(idx - 1) // 2] + sum_of_ancestors((idx - 1) // 2)

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    
    heap = []
    while arr:
        k = arr.pop(0)
        heapq.heappush(heap, k)
    
    n = len(heap) - 1    # 마지막 노드
    
    result = sum_of_ancestors(n)

    print(f'#{t + 1} {result}')