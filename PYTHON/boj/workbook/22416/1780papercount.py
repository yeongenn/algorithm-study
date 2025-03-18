import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

N = int(input())

def search(y, x, n):   # 시작 좌표, 탐색 크기(?)
    global count
    num = papers[y][x]
    
    if n == 1:
        count[num] += 1
        return
    
    is_same = True
    for i in range(y, y + n):
        for j in range(x, x + n):
            if papers[i][j] != num:
                is_same = False
            if not is_same:
                break
    
    # 분할
    if not is_same:
        for i in range(y, y + n, n // 3):
            for j in range(x, x + n, n // 3):
                search(i, j, n // 3)
                
    else:
        count[num] += 1
    
papers = [list(map(int, input().split())) for _ in range(N)]

count = [0, 0, 0]

search(0, 0, N)

print(count[-1])
print(count[0])
print(count[1])