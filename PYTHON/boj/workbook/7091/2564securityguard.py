import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

W, H = map(int, input().split())
N = int(input())    # 상점 갯수
stores = [list(map(int, input().split())) for _ in range(N)]      # 상점들 위치, 1 : 북쪽, 2 : 남쪽, 3 : 서쪽, 4 : 동쪽
dir, dist = map(int, input().split())      # 현재 위치 

total_dist = 0

############################################ 노가다 버전 - 100% 구현 ############################################

def shorter_dist(x, y):
    if x > y:
        return y
    else:
        return x

if dir == 1:
    for store_d, store_dist in stores:
        if store_d == 1:
            total_dist += abs(store_dist - dist)
        elif store_d == 2:
            dist_cw = (W - dist) + H + (W - store_dist)
            dist_ccw = dist + H + store_dist
            total_dist += shorter_dist(dist_cw, dist_ccw)
        elif store_d == 3:
            total_dist += dist + store_dist
        else:
            total_dist += (W - dist) + store_dist
elif dir == 2:
    for store_d, store_dist in stores:
        if store_d == 1:
            dist_cw = dist + H + store_dist
            dist_ccw = (W - dist) + H + (W - store_dist)
            total_dist += shorter_dist(dist_cw, dist_ccw)
        elif store_d == 2:
            total_dist += abs(store_dist - dist)
        elif store_d == 3:
            total_dist += dist + (H - store_dist)
        else:
            total_dist += (W - dist) + (H - store_dist)
elif dir == 3:
    for store_d, store_dist in stores:
        if store_d == 1:
            total_dist += dist + store_dist
        elif store_d == 2:
            total_dist += (H - dist) + store_dist
        elif store_d == 3:
            total_dist += abs(dist - store_dist)
        elif store_d == 4:
            dist_cw = dist + W + store_dist
            dist_ccw = (H - dist) + W + (H - store_dist)
            total_dist += shorter_dist(dist_cw, dist_ccw)
else:   # dir == 4
    for store_d, store_dist in stores:
        if store_d == 1:
            total_dist += dist + (W - store_dist)
        elif store_d == 2:
            total_dist += (H - dist) + (W - store_dist)
        elif store_d == 3:
            dist_cw = (H - dist) + W + (H - store_dist)
            dist_ccw = dist + W + store_dist
            total_dist += shorter_dist(dist_cw, dist_ccw)
        elif store_d == 4:
            total_dist += abs(dist - store_dist)

############################################ 노가다 버전 - 100% 구현 ############################################
############################################ #################### ############################################

print(total_dist)