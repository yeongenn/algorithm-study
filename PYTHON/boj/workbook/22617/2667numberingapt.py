import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

N = int(input())

def inside_block(r, c):
    house_cnt = 0
    q = [[r, c]]
    visited[r][c] = 1   # 시작점 마킹
    house_cnt += 1      # 시작점 카운트
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while q:
        y, x = q.pop(0)
        
        for i, j in zip(dy, dx):
            ny, nx = y + i, x + j
            if 0 <= ny < N and 0 <= nx < N and houses[ny][nx] == 1 and visited[ny][nx] == 0:
                q.append([ny, nx])
                visited[ny][nx] = 1     # 마킹 여기서 안해주면 중복 카운트 발생!
                house_cnt += 1

    return house_cnt

houses = [list(map(int, input())) for _ in range(N)]
# print(houses)
visited = [[0] * N for _ in range(N)]
count = 0   # 단지 수
in_block = []   # 단지 내 집 수


for i in range(N):
    for j in range(N):
        if not visited[i][j] and houses[i][j] != 0:
            temp = inside_block(i, j)
            in_block.append(temp)
            count += 1

# 출력            
print(count)
in_block.sort()
for num in in_block:
    print(num)
            