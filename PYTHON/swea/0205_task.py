# 250205 알고리즘 실습 문제
# List - 1

#

# DAT 연습 문제
# 블랙 리스트
# T = int(input())

# for t in range(T):
#     i, j = map(int, input().split())

#     # apt = []
#     apt = [list(map(int, input().split())) for _ in range(i)]

#     m, n = map(int, input().split())
#     given_black_list = []
#     for row in range(m):
#         row_list = map(int, input().split())
#         given_black_list.extend(row_list)

#     # print(given_black_list)

#     black_list = [0] * 100001
    
#     for black in given_black_list:
#         black_list[black] = 1

#     count_black = 0
#     for h in range(i):
#         for w in range(j):
#             if black_list[apt[h][w]] == 1:
#                   count_black += 1


#     print(f'#{t + 1} {count_black} {i * j - count_black}')

# 성실한 직원 찾기
T = int(input())

for t in range(T):
    i, j = map(int, input().split())

    emp_list = [list(map(int, input().split())) for _ in range(i)]

    punc_emp_dict = {}
    for h in range(i):
        for w in range(j):
            if punc_emp_dict.get(emp_list[h][w]) == None:
                punc_emp_dict[emp_list[h][w]] = 1
            else:
                punc_emp_dict[emp_list[h][w]] += 1

    punc_emp_dict = dict(sorted(punc_emp_dict.items(), key=lambda emp : emp[1]))

    max_emp = max(punc_emp_dict.values())

    for k in punc_emp_dict.keys():
        if punc_emp_dict[k] == max_emp:
            print(k)
            break
        



