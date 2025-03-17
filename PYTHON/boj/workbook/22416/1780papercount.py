import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

N = int(input())

def search(y, x, n):   # 시작 좌표, 탐색 크기(?)
    pass

papers = [list(map(int, input().split())) for _ in range(N)]
# print(papers)

cnt_n1 = cnt_0 = cnt_1 = 0

# search(0, 0, N)

print(cnt_n1)
print(cnt_0)
print(cnt_1)
