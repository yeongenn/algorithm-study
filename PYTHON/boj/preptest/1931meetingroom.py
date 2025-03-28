import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
# sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

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

schedules.sort(key=lambda x : (x[1], x[0]))     #  정렬
# print(schedules)
n = len(schedules)
max_value = 0

for i in range(n):
    count = 1   # 사용 횟수 초기화
    prev = schedules[i][1]  # 이전 회의 종료 시간 관리
    for j in range(i + 1, n):
        if schedules[j][0] >= prev:
            count += 1
            prev = schedules[j][1]      # prev 갱신
    max_value = max(max_value, count)

print(max_value)