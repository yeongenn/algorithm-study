import sys
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

from collections import deque

N, M = map(int, input().split())
loc = list(map(int, input().split()))

queue = deque([x for x in range(1, N + 1)])
# print(queue)
cnt = 0 # 2, 3번 연산 누적값

for now in loc:
    while queue[0] != now:
        now_idx = queue.index(now)
        if now_idx > len(queue) - now_idx:
            queue.rotate(1) # 오른쪽
            cnt += 1
        else:
            queue.rotate(-1)    # 왼쪽
            cnt += 1
    else:
        queue.popleft()
        continue
print(cnt)