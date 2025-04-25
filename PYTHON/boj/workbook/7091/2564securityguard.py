import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

########################################## X ##########################################
W, H = map(int, input().split())
N = int(input())    # 상점 갯수
stores = [list(map(int, input().split())) for _ in range(N)]      # 상점들 위치, 1 : 북쪽, 2 : 남쪽, 3 : 서쪽, 4 : 동쪽
cur_dir, cur_loc = map(int, input().split())      # 현재 위치 
# print(stores)

distance = 0
for store in stores:
    dir, loc = store
    if dir == cur_dir:
        distance += abs(cur_loc - loc)
    elif dir + cur_dir == 3:    # 북, 남
        distance = min((loc + H + cur_loc), ((W - loc) + H + (W - cur_loc)))
    elif dir + cur_dir == 7:    # 동, 서
        distance = min((loc + W + cur_loc), ((H - loc) + W + (H - cur_loc)))
    else:
        if cur_dir == 1:    # 북일 때
            if dir == 4:    # 동
                distance += (W - cur_loc) + loc
            elif dir == 3:  # 서
                distance += cur_loc + loc
        elif cur_dir == 2:  # 남일 때
            if dir == 3:    # 서
                distance += cur_loc + (H - loc)
            elif dir == 4:  # 동
                distance += (W - cur_loc) + (H - loc)
        elif cur_dir == 3:  # 서일 때
            if dir == 1:    # 북
                distance += cur_loc + loc
            elif dir == 2:  # 남
                distance += (H - cur_loc) + loc
        elif cur_dir == 4:  # 동일 때
            if dir == 2:    # 남
                distance += (W - loc) + (H - cur_loc)
            elif dir == 1:  # 북
                distance += cur_loc + (W - loc)
print(distance)