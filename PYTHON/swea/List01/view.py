# 250205 알고리즘 과제
# List

# View - 조망권 문제

for t in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))
    with_view = 0

    for i in range(2, N -2):
        max_height = max(buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2])
        if buildings[i] > max_height:
            with_view += (buildings[i] - max_height)

    print(f'#{t + 1} {with_view}')