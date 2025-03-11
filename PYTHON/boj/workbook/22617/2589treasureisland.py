import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

H, W = map(int, input().split())

def explore(y, x):
    result = 0
    q = [[y, x]]
    visited[y][x] = 1
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while q:
        y, x = q.pop(0)
        
        for i, j in zip(dy, dx):
            ny, nx = y + i, x + j
            if 0 <= ny < H and 0 <= nx < W and visited[ny][nx] == 0 and treasures[ny][nx] == "L":
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
                result = max(visited[ny][nx], result)
                
    return result

treasures = [list(input()) for _ in range(H)]   # L : 육지, W : 바다
# print(treasures)

hour = 0

for r in range(H):
    for c in range(W):
        if treasures[r][c] == "L":
            visited = [[0] * W for _ in range(H)]   # 모든 경우마다 마킹 배열 초기화 해줘야
            hour = max(hour, explore(r, c))         
            
print(hour - 1)