from collections import deque

N = int(input())

q = deque([x for x in range(1, N + 1)])

while  q:
    if N == 1:  # q 길이가 1인 경우 / 미체크시 런타임 에러
        break

    if len(q) == 1:
        break

    q.popleft()
    q.append(q.popleft())

print(*q)

