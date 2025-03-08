import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.setrecursionlimit(10 ** 6)    # recursion error 방지

def island(y, x):
    visited[y][x] = 1   # 방문 처리
    dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    for i, j in zip(dy, dx):
        ny, nx = y + i, x + j
        if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx] and graph[ny][nx]: # 범위 내이고 마킹 안했고 땅일 경우에
            island(ny, nx) 

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0: break
    
    graph = [list(map(int, input().split())) for _ in range(H)]   # 0 : 바다, 1 : 땅
    visited = [[0] * W for _ in range(H)]   # 방문 체크용
    # print(map)

    island_cnt = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1 and visited[i][j] == 0:   # 방문한 적 없고 땅일 때만
                island(i, j)
                island_cnt += 1
                
    print(island_cnt)