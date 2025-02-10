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

    max_emp = max(punc_emp_dict.values())
    emp_list = []
        
    for k, v in punc_emp_dict.items():
        if punc_emp_dict[k] == max_emp:
            emp_list.append(k)

    print(f'#{t + 1} {min(emp_list)}')