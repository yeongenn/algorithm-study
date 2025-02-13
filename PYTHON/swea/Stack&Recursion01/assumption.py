T = int(input())

count = 0

def assumption(n):
    global count
    if n == 1: return

    count += 1
    if n % 2 == 0:
        return assumption(n // 2)
    else:
        return assumption((n * 3) + 1)

for t in range(T):
    count = 0

    N = int(input())
    assumption(N)
    print(f'#{t + 1} {count}')