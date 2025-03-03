# 2차 월말평가 대비
# BFS - queue
# 평가에서는 import 사용 불가
import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

# from collections import deque

# ########################################### PyPy로 통과 ###########################################

T = int(input())

for t in range(T):
    I = int(input())
    crt_x, crt_y = map(int, input().split())    # 현재 위치
    dst_x, dst_y = map(int, input().split())    # 목표 위치
    min_move = 0    # 최소 이동 횟수
    
    to_visit = [(crt_x, crt_y)]     # 현재 위치에서 시작 
    # to_visit = deque([(crt_x, crt_y)])
    visited = [[0] * I for _ in range(I)]
    visited[crt_x][crt_y] = 1       # 시작 좌표 마킹
    dt = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]   # 시계 방향
    
    is_arrived = False      # flag
    while to_visit:
        if is_arrived: break
        x, y = to_visit.pop(0)
        # x, y = to_visit.popleft()
        for i, j in dt:
            nx, ny = x + i, y + j
            if 0 <= nx < I and 0 <= ny < I:
                if visited[nx][ny] == 0:
                    to_visit.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    
                if nx == dst_x and ny == dst_y: 
                    is_arrived = True
                    break       
    
    print(visited[dst_x][dst_y] - 1) 
    
# 도착했을 때 while문 내 for에서만 break -> flag로 while에서도 break