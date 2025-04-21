import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

N, K = map(int, input().split())    # N : 학생 수, K : 한 방 최대 인원 수
students = [[0, 0] for _ in range(7)]

for _ in range(N):
    S, Y = map(int, input().split())    # S : 여학생은 0, 남학생 1, Y : 학년
    students[Y][S] += 1

rooms = 0
for i in range(1, 7):
    if students[i][0] != 0:     # 여학생
        rooms += (((students[i][0] - 1) // K) + 1)

    if students[i][1] != 0:     # 남학생
        rooms += (((students[i][1] - 1) // K) + 1)
print(rooms)
