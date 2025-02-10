T = int(input())

for t in range(T):
    N = int(input())
    pattern = list(map(int, input().split()))
    
    lights = [0] * N
    count = 0
        
    for i, (p, l) in enumerate(zip(pattern, lights), 1):
        if p == l:
            pass
        else:
            for j in range(i - 1, N, i):
                lights[j] = 1 if lights[j] == 0 else 0
            count += 1
        if lights == pattern:
            break

    print(f'#{t + 1} {count}')
