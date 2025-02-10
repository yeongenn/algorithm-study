li = [list(map(int, input().split())) for _ in range(9)]


max_value = 0
loc = ()
for i in range(9):
    for j in range(9):
        if li[i][j] > max_value:
            max_value = li[i][j]
            loc = (i + 1, j + 1)

print(max_value)
print(*loc)



