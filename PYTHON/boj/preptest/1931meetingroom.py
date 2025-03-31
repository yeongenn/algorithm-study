import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

# 3회차 월말 평가 대비

######################################### 시간 초과 #########################################

N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]
# print(schedules)

# n = len(schedules)
# # times = []
# times = 0
# max_value = 0
# def get_schedules(level, start, prev):
#     global max_value, times

#     # print(times)
#     # max_value = max(max_value, len(times))  # 최대 길이 갱신하기
#     max_value = max(max_value, times)

#     for i in range(start, n):
#         if schedules[i][0] >= prev:
#             # times.append(schedules[i])
#             times += 1
#             get_schedules(level + 1, i + 1, schedules[i][1])
#             # times.pop()
#             times -= 1

# get_schedules(0, 0, 0)
# print(max_value)

# # 위 코드에서 내가 놓친 것
# #   -> 시작 시간과 끝 시간이 같은 경우
# #   -> 이건 문제가 아닌 것 같은,,,

# # 부분 집합으로 접근하면 안되는 건가,,,

###############################################################################################

# 정렬?
# 똑같이 시간 초과 나잖아~!~!~!~!

schedules.sort(key=lambda x : (x[1], x[0]))     #  정렬, 우선순위대로 튜플에 설정
# print(schedules)
n = len(schedules)

# for i in range(n):
#     count = 1   # 사용 횟수 초기화
#     prev = schedules[i][1]  # 이전 회의 종료 시간 관리
#     for j in range(i + 1, n):
#         if schedules[j][0] >= prev:
#             count += 1
#             prev = schedules[j][1]      # prev 갱신
#     max_value = max(max_value, count)

# 정렬 후 첫번째 회의는 무조건 배정
prev = schedules[0][1]  # 이전 회의 종료 시간 관리
count = 1
for i in range(1, n):
    if schedules[i][0] >= prev:
        count += 1
        prev = schedules[i][1]
    
print(count)

###############################################################################################
# 첫번째 회의를 반드시 선택하지 않아도 같은 최적해 구할 수 있는데?

# 그리디 알고리즘에서는 항상 최적해 보장하는 여러 가지 선택지가 존재
# 중요한 것은 빨리 끝나는 회의를 우선적으로 선택하면 최적해 유지가 가능하다는 점
# -> 여러 개의 최적해가 존재하더라도 빨리 끝나는 회의를 선택하는 전략이 항상 최적해로 이어진다