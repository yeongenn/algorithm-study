import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

def next_room(y, x):
    cnt = 1
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i, j in zip(dy, dx):
        ny, nx = y + i, x + j
        if 0 <= ny < N and 0 <= nx < N and rooms[ny][nx] == rooms[y][x] + 1:
            cnt += next_room(ny, nx)
        
    return cnt

for t in range(T):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    
    max_value = 0
    room_numbers = N * N + 1
    
    for i in range(N):
        for j in range(N):
            result = next_room(i, j)
            if result > max_value:          # 현재 최댓값보다 크면 최댓값, 방 숫자 모두 갱신
                max_value = result
                room_numbers = rooms[i][j]
            elif result == max_value:       # 최댓값이랑 같으면 방 숫자만 갱신
                if room_numbers > rooms[i][j]:
                    room_numbers = rooms[i][j]
    print(f'#{t + 1} {room_numbers} {max_value}')