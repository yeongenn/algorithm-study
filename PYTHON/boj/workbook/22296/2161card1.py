from collections import deque

N = int(input())
cards = deque([n for n in range(1, N + 1)])
# print(cards)

dis = []

while len(cards) != 1:
    dis.append(cards.popleft())
    cards.append(cards.popleft())
else:
    dis.append(cards.popleft())

print(*dis)
