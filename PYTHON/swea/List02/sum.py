# Sum
for t in range(10):
    TN = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_1 = 0
    sum_2 = 0   # 우하향
    sum_3 = 0   # 좌하향
    # sum_4 = 0

    max_s = 0

    for i in range(100):
        max_s = max(max_s, sum(arr[i]))
        for j in range(100):
            if i == j:
                sum_2 += arr[i][j]
            if i + j == 99:
                sum_3 += arr[i][j]

    max_s = max(max_s, sum_2, sum_3)

    for j in range(100):
        sum_4 = 0
        for i in range(100):
            sum_4 += arr[i][j]

        max_s = max(max_s, sum_4)
    print(f'#{t + 1} {max_s}')