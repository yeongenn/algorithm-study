N = int(input())

coord = [list(map(int, input().split())) for _ in range(N)]
# print(coord)

paper = [[0] * 100 for _ in range(100)]

# 색종이 표시하기
for x, y in coord:
    sx, sy, ex, ey = x, y, x + 10, y + 10
    for i in range(sx, ex):
        for j in range(sy, ey):
            if paper[i][j] == 0:
                paper[i][j] = 1
                
# 둘레 구하기
m = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(100):
    for y in range(100):
        if paper[x][y] == 1:
            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j
                if 0 <= nx < 100 and 0 <= ny < 100:
                    if paper[nx][ny] == 0:
                        m += 1
                elif nx < 0 or nx >= 100 or ny < 0 or ny >= 100:
                    m += 1

print(m)