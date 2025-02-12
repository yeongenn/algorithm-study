T = int(input())

for t in range(T):
    A, B = input().split()
    A = A.replace(B, "0")
    print(f'#{t + 1} {len(A)}')