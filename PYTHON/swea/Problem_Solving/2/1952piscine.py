# 완전 탐색 or DP
import sys
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

for t in range(T):
    daily, monthly, three_month, yearly = map(int, input().split())
    month = list(map(int, input().split()))
    
    cost = [0] * 13     # 해당 월까지 누적 금액
    
    # 1, 2월달 cost 초기값 설정
    cost[1] = min(month[0] * daily, monthly)
    cost[2] = min(month[1] * daily, monthly) + cost[1]
    
    for i in range(3, 13):
        # 일단 1일권, 1개월권 비교
        cost[i] = min(month[i - 1] * daily, monthly) + cost[i - 1]
        
        # 그러고 나서 3개월권 비교
        cost[i] = min(cost[i], three_month + cost[i - 3])
        
    # 12월까지 다 구한 다음 마지막으로 1년권 비교
    result = min(cost[12], yearly)
    
    print(f'#{t + 1} {result}')
    
# ########################################### review ###########################################

""""
DP로 풀 수 있는 문제의 조건

1. 기존 최솟값을 재활용
2. 이전 단계의 값을 변경하지 않는다
"""
