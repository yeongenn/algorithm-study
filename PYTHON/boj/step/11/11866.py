N, K = map(int, input().split())

people = [x for x in range(1, N + 1)]
result = []

index = 0   # 시작 인덱스
while people:
    index += (K - 1)
    if index >= len(people):
        index -= len(people)
        if index >= len(people):
            result.append(people.pop(0))
            break
    result.append(people.pop(index))

result.append(people.pop()) # 마지막 남은 사람 제거
print(f'<{", ".join(map(str, result))}>')

# to solve

