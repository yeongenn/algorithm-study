N = int(input())

# 도화지 크기 100 * 100
# 색종이 크기 10 * 10

white = [[0] * 100 for _ in range(100)]
result = 0

for i in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if white[i][j] == 0:
                white[i][j] = 1
                result += 1

print(result)
