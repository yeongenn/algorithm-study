# # ver 1
# N, K = map(int, input().split())

# people = [x for x in range(1, N + 1)]
# result = []

# while people:
#     # 원형 큐 : 하나씩 꺼내서 조건에 맞지 않으면 다시 뒤에 push하면 된다
#     # ex) 3번째 사람 제거 : 1, 2번째 사람은 조건에 맞지 않는 거니까 queue 뒤에 다시 push하면 된다
#     for i in range(1, K + 1):
#         if i == K:
#             result.append(people.pop(0))
#         else:
#             people.append(people.pop(0))

# print(f'<{", ".join(map(str, result))}>')

"""
코드 리뷰

내가 짠 코드(ver 1)는 시간 복잡도 O(NK)
내가 젤 처음에 했던 방식(ver 2) -> idx += (K - 1)로도 가능 -> 시간 복잡도 O(N)

"""
# ver 2
N, K = map(int, input().split())

people = [x for x in range(1, N + 1)]
result = []

index = 0   # 시작 인덱스
while people:
    index += (K - 1)
    if index >= len(people):    # 인덱스 범위 넘어갈 경우 <- 여기까지는 맞게 작성
        index %= len(people)    # 넘어가는 인덱스 재설정 부분에서 삐끗함
    result.append(people.pop(index))
print(f'<{", ".join(map(str, result))}>')