T = int(input())

for t in range(T):
    N = int(input())
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))

    count = 0
    for i, (b, a) in enumerate(zip(before, after)):
        if before != after:
            if b != a:
                for j in range(i, N):
                    before[j] = 0 if before[j] == 1 else 1
                count += 1
        else: break        
    print(f'#{t + 1} {count}')