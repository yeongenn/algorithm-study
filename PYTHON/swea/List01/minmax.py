T = int(input())

def difference(li):
    return (max(li) - min(li))

for t in range(T):
    N = int(input())
    li = list(map(int, input().split()))
        
    result = difference(li)
    print(f'#{t + 1} {result}')
    