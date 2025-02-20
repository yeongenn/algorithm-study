N, K = map(int, input().split())

people = [x for x in range(1, N + 1)]
result = []

index = 0   # 시작 인덱스
while people:
    index += (K - 1)
    if index >= len(people):    # 인덱스 범위 초과 시
        index %= len(people)    # 인덱스 재설정
    result.append(people.pop(index))
print(f'<{", ".join(map(str, result))}>')