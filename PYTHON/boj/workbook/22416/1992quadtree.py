import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

def func(N, arr, sx, sy):
    cnt_0 = 0
    for i in range(sx, sx + N):
        for j in range(sy, sy + N):
            if arr[i][j] == '0':
                cnt_0 += 1
    if cnt_0 == N * N:
        print(0, end="")
        return
    elif cnt_0 == 0:
        print(1, end="")
        return
    else:
        print("(", end="")
        half = N // 2
        for r in range(0, N, half):
            for c in range(0, N, half):
                func(half, arr, sx + r, sy + c) # 현재 좌표에서 거리 계산해야
        print(")", end="")
    
N = int(input())

q_tree = [list(input()) for _ in range(N)]
# print(q_tree)

func(N, q_tree, 0, 0)

# 4분면으로 쪼개는 작업을 반복 -> 제일 작은 단위로 쪼갤 때까지 -> 제일 작은 단위에서 얻을 수 있는 값은 0 or 1 -> 재귀
# 반복해야 하는 작업 : 쪼갠 사분면을 하나씩 탐색하기 + 원하는 결과를 얻을 때까지 쪼개기
# 제일 고민했던 부분 : 처음에 주어진 배열을 쪼개서 새로운 배열을 만들어야 하나?
#   -> 굳이 그렇게 하지 않아도 인덱스 재설정 통해서도 가능하겠다고 생각

# 오답 상황 리뷰 : 재귀 호출할 때 넘겨줄 인덱스를 현재 좌표 기준으로 계산해야하는데 냅다 바로 넘기는 바람에 
#                최초 배열에서 1사분면만 계속 탐색함ㅎㅋ