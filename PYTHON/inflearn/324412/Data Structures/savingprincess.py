from collections import deque

N, K = map(int, input().split())

princes = deque([x for x in range(1, N + 1)])   # 1~N번 왕자
while len(princes) > 1:
    princes.rotate(-(K - 1))
    princes.popleft()
else:   # 한 명 남았으면
    print(princes.pop())