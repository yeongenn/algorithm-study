T = int(input())

for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    print(f'#{t + 1} {result}')