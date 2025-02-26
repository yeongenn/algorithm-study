import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

def color_paper(n, sx, sy):
    global white, blue
    
    w_cnt, b_cnt = 0, 0
    
    for i in range(sx, sx + n):
        for j in range(sy, sy + n):
            if paper[i][j] == 0:
                w_cnt += 1
            else:
                b_cnt += 1
    
    if w_cnt == n * n:
        white += 1
        return
    elif b_cnt == n * n:
        blue += 1
        return
    else:
        half = n // 2
        for i in range(0, n, half):
            for j in range(0, n, half):
                color_paper(half, sx + i, sy + j)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)] # 0 : 하얀색, 1 : 파란색
# print(paper)

white = 0
blue = 0

color_paper(N, 0, 0)

print(white)
print(blue)

# 1992 quadtree문제랑 동일
# 인덱스는 여전히 어려움ㅜㅜ