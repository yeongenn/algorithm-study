necessaries = list(input())

T = int(input())
for t in range(T):
    plans = list(input())
    
    idx = 0 # 필수과목 queue에 저장해서 들었으면 pop하려고 했는데 전역이라 idx로 접근
    successed = False
    for i in range(len(plans)):
        if necessaries[idx] == plans[i]:
            idx += 1
            if idx == len(necessaries):
                successed = True
                break
            continue
    
    print(f'#{t + 1} {"YES" if successed else "NO"}')