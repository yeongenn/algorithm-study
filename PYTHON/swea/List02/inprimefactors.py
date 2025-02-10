# 간단한 소인수 분해

T = int(input())
dv = [2, 3, 5, 7, 11]

for t in range(T):
    dv_count = [0] * 12
    N = int(input())
    
    for num in dv:
        while N % num == 0:
            dv_count[num] += 1
            N /= num

    result = []
    for num in dv:
        result.append(dv_count[num])

    # print(result)

    print(f'#{t + 1}', *result)