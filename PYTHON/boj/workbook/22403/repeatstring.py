T = int(input())

for t in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)
    # print(R, S)
    P = ''
    for s in S:
        P += s * R
    
    print(P)