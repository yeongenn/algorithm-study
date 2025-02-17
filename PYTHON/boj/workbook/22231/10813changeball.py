N, M = map(int, input().split())
# baskets = [0] * (N + 1)
# for i in range(1, N + 1):
#     baskets[i] = i

baskets = [x for x in range(N + 1)]     # list comprehension

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]

print(*baskets[1:])