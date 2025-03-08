# 최대힙
import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\inflearn\\input.txt", "r")

import heapq

heap = []
while True:
    N = int(input())
    if N == -1:
        break
    elif N == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -N)    # 최대힙은 지원 X -> 음수로 넣기