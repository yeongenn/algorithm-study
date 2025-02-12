li = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if li[i][j] >= max_value:   # 부호...!
            max_value = li[i][j]
            x, y = i + 1, j + 1

print(f'{max_value}')
print(x, y)