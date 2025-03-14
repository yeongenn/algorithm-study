""""
swea 1952 완전 탐색으로 풀기
    - 각 달에 4가지 케이스를 모두 확인하면서 진행

level : 12
branch : 4가지 - 1일권, 1개월권, ...
"""

T = int(input())

def recur(month, total_cost):
    global min_answer
    
    if min_answer < total_cost:     # 가지치기 - 필요없는 재귀호출 걷어내기
        return
    
    if month > 12:      # level
        min_answer = min(min_answer, total_cost)
        return
    
    # branch - 4가지 경우 보기
    recur(month + 1, total_cost + (days[month] * cost_day))
    recur(month + 1, total_cost + cost_month)
    recur(month + 3, total_cost + cost_month3)          # 3개월권 - 넘겨주는 인덱스 주의
    recur(month + 12, total_cost + cost_year)           # 1년권


for t in range(T):
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split(0))
    days = [0] + list(map(int, input().split()))        # [0] + : 인덱스 맞추기
    min_answer = int(21e8)          # 초기값으로 아주 큰 값
    
    recur(1, 0)
    print(f'#{t + 1} {min_answer}')