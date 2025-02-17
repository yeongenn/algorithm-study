N = int(input())

result = []
result.append(N)    # 첫번째 수 넣기
idx = 0 # 인덱스용

max_len = 0


for n in range(99, 0, -1):
    # 두번째 숫자
    result.append(n)
    idx += 1

    while True:
        temp = result[idx - 1] - result[idx]
        if temp < 0:
            break
        result.append(temp)
        idx += 1

    if len(result) == 8:    # 확인용 하드코딩
        break
    
    result = [100]
    idx = 0


print(*result)


