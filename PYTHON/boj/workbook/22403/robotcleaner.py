import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

"""
로봇 청소기는 다음과 같이 작동한다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    3-1. 반시계 방향으로 90도 회전한다.
    3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3-3. 1번으로 돌아간다.
    
첫째줄 방 크기 N, M
둘째 줄 로봇 청소기 처음 좌표와 바라보는 방향 d
d: 0 - 북, 1 - 동, 2 - 남, 3 - 서
0 이면 청소되지 않은 빈칸, 1이면 벽
"""
import pprint

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# pprint.pprint(room)

# 청소 영역 수
cnt_cleaned = 0

# 현재 위치
cy, cx = r, c

while True:
    # 1
    if room[cy][cx] == 0:
        room[cy][cx] = 0
        cnt_cleaned += 1
        
        