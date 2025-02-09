T = int(input())

def sum_of_section(li, s_len):
    s_list = []
    for i in range(len(li) - s_len + 1):
        sum = 0
        for j in range(s_len):
            sum += li[i + j]
        s_list.append(sum)
    
    return  max(s_list) - min(s_list)

for t in range(T):
    N, s_len = map(int, input().split())
    li = list(map(int, input().split()))
    
    result = sum_of_section(li, s_len)

    
    print(f'#{t + 1} {result}')