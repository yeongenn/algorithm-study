T = int(input())

for t in range(T):
    N = int(input())
    lines_count = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            lines_count[i] += 1
    
    P = int(input())
    
    C = []
    for _ in range(P):
        C.append(int(input()))
        
    result = map(lambda x : lines_count[x], C)
            
    print(f'#{t + 1}', *result)