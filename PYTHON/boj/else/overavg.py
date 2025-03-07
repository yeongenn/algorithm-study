T = int(input())

for t in range(T):
    li = list(map(int, input().split()))
    N = li[0]
    scores = li[1::]

    avg = sum(scores) / N
    over = list(filter(lambda n : n > avg, scores))

    result = (len(over) / N) * 100

    print(f'{round(result, 3)}%')