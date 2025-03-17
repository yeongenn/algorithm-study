T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    binary = list(input())
    result = 0

    for i in range(N - K):
        for j in range(K, N - i + 1):
            temp = binary[i:i + j]

            # 1이 K개 있어야 하고, 최상위 자리와 최하위 자리가 1이여야 하므로
            if temp.count('1') == K and temp[0] == '1' and temp[-1] == '1':
                result = max(result, len(temp))

    print(f'#{t + 1} {result}')