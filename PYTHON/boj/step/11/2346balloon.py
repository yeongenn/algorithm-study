N = int(input())
# balloons = [x for x in range(1, N + 1)]
paper = list(map(int, input().split())) # [3, 2, 1, -3, -1]
paper = list(enumerate(paper, 1))
# print(paper)  # [(1, 3), (2, 2), (3, 1), (4, -3), (5, -1)]

index = 0   # 시작 인덱스
result = []
next = paper.pop(index)
temp = next[1]
result.append(next[0])

for _ in range(N - 1):
    if len(paper) == 1:
        result.append(paper[0][0])  # 하나만 남으면 그거 터뜨리면 될테니까
        break

    print(temp)
    if temp > 0:
        index += (temp - 1)
        if index >= len(paper):
            index %= len(paper)
    elif temp < 0:
        if temp <= index:
            index += temp
        else: index += abs(temp)
        if index >= len(paper):
            index %= len(paper)
        
    next = paper.pop(index)
    temp = next[1]
    result.append(next[0])
    
print(*result)

"""
반례

입력
10
1 -2 3 -4 5 -6 7 -8 9 -10

출력
1 2 9 3 6 5 7 8 10 4
"""