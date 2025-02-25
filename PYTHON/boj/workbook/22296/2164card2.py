from collections import deque

N = int(input())

q = deque([x for x in range(1, N + 1)])

while  q:
    if N == 1:
        break

    if len(q) == 1:
        break

    q.popleft()
    q.append(q.popleft())

print(*q)