T = int(input())

for t in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    min_idx = li.index(min(li))
    
    max_idx_list = [i for i, v in enumerate(li) if v == max(li)]
    max_idx = max_idx_list[-1]
    
    result = abs(max_idx - min_idx)
    print(f'#{t + 1} {result}')