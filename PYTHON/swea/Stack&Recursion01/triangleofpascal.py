T = int(input())

def pascal(i, j):
    if j == 0 or i == j:
        return 1
    if i < j:
        return 0
    
    return pascal(i - 1, j) + pascal(i - 1, j - 1)

for t in range(T):
    N = int(input())
    arr = [[0] * N] * N

    print(f'#{t + 1}')
    for i in range(N):
        for j in range(i + 1):
            print(pascal(i, j), end=" ")
        print()