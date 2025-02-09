T = int(input())

for t in range(T):
    N = int(input())
    li = list(map(int, list(input())))
    result = 0
    sum = 0
    for n in li:
        if n == 1:
            sum +=1
        else:
            sum = 0
        result = max(result, sum)
    
    print(f'#{t + 1} {result}')