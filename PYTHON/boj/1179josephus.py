N, K = map(int, input().split())

people = [x for x in range(1, N + 1)]
result = 0


##############################메모리 초과##############################
index = 0
while people:
    if len(people) == 1:
        result = people.pop()
        break
    index += (K - 1)
    if index >= len(people):
        index %= len(people)
    people.pop(index)

print(result)



    