T = int(input())

for t in range(T):
    tc, N = input().split()
    words = input().split()
    
    num_sys = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    result = [0] * int(N)
    for i in range(int(N)):
        result[i] = num_sys.index(words[i])

    result.sort()
    # print(result)

    for i in range(int(N)):
        result[i] = num_sys[result[i]]

    print(f'{tc}')
    print(*result)
