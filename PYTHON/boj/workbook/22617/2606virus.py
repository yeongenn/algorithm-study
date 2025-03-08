import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.setrecursionlimit(10 ** 6)    # recursion error 방지

N = int(input())    # 컴퓨터 수
M = int(input())    # 간선 수
cnct = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    cnct[x].append(y)
    cnct[y].append(x)
# print(cnct)

