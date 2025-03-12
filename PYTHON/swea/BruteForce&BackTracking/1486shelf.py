import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

for t in range(T):
    N, B = map(int, input().split())    # N : 점원 수, B : 탑 높이
    clerks = list(map(int, input().split()))
    print(clerks)
    
    temp = []
    min_value = B
    
    def subset(n, cnt, total):
        global min_value
        
        if total >= B:
            print(total)
            min_value = min(min_value, total - B)
            return
        
        if n == cnt:
            # if total >= B:
            #     print(total)
            #     min_value = min(min_value, total - B)
            return
        
        for num in clerks:
            temp.append(num)
            subset(n, cnt + 1, total + num)
            temp.pop()
    
    
    for i in range(1, N + 1):
        subset(i, 0, 0)
        temp = []               # 리셋
        
    print(f'#{t + 1} {min_value}')