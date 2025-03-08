# 이분 검색
import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\inflearn\\input.txt", "r")

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()     # 이진 탐색 위해서는 정렬이 되어있어야

left, right = 0, N - 1
# while True:
while left <= right:    # 교차했다? -> 정렬 내에 없다
    mid = (left + right) // 2
    if num_list[mid] == M: 
        print(mid + 1)
        break
    elif num_list[mid] > M:
        right = mid - 1
    elif num_list[mid] < M:
        left = mid + 1
