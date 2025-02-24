while True:

    N = int(input())

    if N == -1:
        break
    
    # 2 < n < 100 000 이라 제곱근까지 안해도 가능
    flag = int(N ** (1 / 2))
    # print(flag)
    result = []

    for i in range(1, flag + 1):
        if N % i == 0:
            result.append(i)
            if N // i not in result and N // i != N:
                result.append(N // i)

    # print(result)
    result.sort()
    if sum(result) != N:
        print(f'{N} is NOT perfect.')
    else:
        print(f'{N} = ', end="")
        # for num in range(len(result) - 1):
        #     print(result[num], end=" + ")
        # print(result[-1])
        print(' + '.join(map(str, result)), sep=" ")    # 한 줄로 줄여쓰기


        