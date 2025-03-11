import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.setrecursionlimit(10 ** 6)    # recursion error 방지

N = int(input())    # 컴퓨터 수
M = int(input())    # 간선 수
cnct = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    cnct[x][y] = 1
    cnct[y][x] = 1      # 양방향
# print(cnct)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j: continue
            if cnct[i][k] and cnct[k][j]:
                cnct[i][j] = 1
                
count = sum(cnct[1])
print(count)