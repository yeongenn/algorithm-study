import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

N = int(input())
sticks = [0] * 1001       # 1000으로 수정하기

# 값 입력받으면서 최대 높이 인덱스 저장하기
max_height = 0
max_height_idx = -1
for _ in range(N):
    L, H = map(int, input().split())
    sticks[L] = H
    if H > max_height:
        max_height = H
        max_height_idx = L
result = 0      # 결과 변수

# 왼쪽에서 오름차순
left_stick = 0
for i in range(0, max_height_idx):
    # if sticks[i] <= left_stick:
    #     result += left_stick
    # else:
    #     left_stick = sticks[i]   # 값 갱신
    #     result += left_stick
    
    left_stick = max(sticks[i], left_stick)
    result += left_stick

# 오른쪽에서 내림차순
right_stick = 0
for i in range(1000, max_height_idx, -1):
    # if sticks[i] <= right_stick:
    #     result += right_stick
    # else:
    #     right_stick = sticks[i]   # 값 갱신
    #     result += right_stick

    right_stick = max(sticks[i], right_stick)
    result += right_stick

result += max_height    # 좌우에서 오면서 최대 높이 막대는 아직 포함 X -> 추가해주기
print(result)
