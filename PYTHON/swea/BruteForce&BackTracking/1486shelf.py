# import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

import sys
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

for t in range(T):
    N, B = map(int, input().split())    # N : 점원 수, B : 탑 높이
    clerks = list(map(int, input().split()))
    # print(clerks)
    
    temp = []
    min_value = 200001
    
    for i in range(1<<len(clerks)):
        subset = []
        for j in range(len(clerks)):
            if i & (1<<j):
                subset.append(clerks[j])
                if sum(subset) >= B:
                    min_value = min(min_value, sum(subset))
        
    print(f'#{t + 1} {min_value - B}')
    
# https://velog.io/@94applekoo/%EB%B9%84%ED%8A%B8%EC%97%B0%EC%82%B0%EC%9E%90%EB%A1%9C-%EB%B6%80%EB%B6%84-%EC%A7%91%ED%95%A9%EC%9D%84-%EC%83%9D%EC%84%B1%ED%95%98%EB%8A%94-%EB%B2%95-python