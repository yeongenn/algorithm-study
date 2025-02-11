T = int(input())

for t in range(T):
    N = int(input())
    cards = input().split()
    
    if N % 2 == 0:
        end = N // 2
    else:
        end = (N // 2) + 1
    c_1 = cards[:end]
    c_2 = cards[end:]

    result = []
    for f, s in zip(c_1, c_2):
        result.extend([f, s])

    if N % 2 == 1:
        result.append(c_1[-1])

    print(f'#{t + 1} {result}')