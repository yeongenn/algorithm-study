# 250218 역량 테스트

# 이동할 수 있는 최대 칸 수 수하기
# 4분면에서 현재 높이보다 작아야하고 그 중에서 가장 작은 높이로만 이동 가능

import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\swea\\Test\\input.txt", "r")

T = int(input())


def search(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    next_x, next_y = x, y
    min_val = arr[x][y]
    for i, j in zip(dx, dy):
        nx = x + i
        ny = y + j
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] < arr[x][y] and arr[nx][ny] < min_val:
                min_val = arr[nx][ny]
                next_x, next_y = nx, ny

    if next_x == x and next_y == y:
        return 1  # 더 이상 갈 수 없으니까 방문했다 표시만 리턴
    else:
        return 1 + search(next_x, next_y)  # distance를 누적 + 다음 좌표 찾아가야 하니까 <- swea 콜라츠 추측 문제


for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    distance = 0
    for x in range(N):
        for y in range(N):
            distance = search(x, y)
            result = max(result, distance)

    print(f"#{t + 1} {result}")
