# 2차 월말평가 대비
# 자료 구조 - 스택, 큐
# 평가에서는 import 사용 불가
import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

N = int(input())    # 스위치 개수 <= 100

status = list(map(int, input().split()))   # 0 : off, 1 : on
S = int(input())    # 학생 수

for _ in range(S):
    sg, sn = map(int, input().split())  #   1 : boy, 2 : girl
    if sg == 1:     # sn 배수 스위치 상태 바꾸기
        for i in range(sn - 1, N, sn):
            status[i] = 1 if status[i] == 0 else 0
    elif sg == 2:   # 최대 좌우대칭 스위치 상태 바꾸기
        # sn 기준 최대 범위 찾기
        max_range = 0
        for i in range(1, N):   # 가운데는 항상 바뀔테니까
            left, right = sn - 1 - i, sn - 1 + i
            if 0<= left < N and 0 <= right < N:
                if status[left] == status[right]:
                    max_range = i
                else: break     # 연속적으로 대칭하지 않으면 break
        
        # 스위치 상태 바꾸기
        status[sn - max_range - 1:sn + max_range] = [1 - status[i] for i in range(sn - max_range - 1, sn + max_range)]

for i in range(N // 20 + 1):    # 스위치 20개씩 출력
    print(*status[20 * i:20 * (i + 1)])