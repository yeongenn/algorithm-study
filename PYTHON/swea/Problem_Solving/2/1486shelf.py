# swea/BruteForce&BackTracking/1486shelf.py
""""
접근 방법

모든 탑 쌓아보기 - 조건 만족하는 탑 여러 개
가능한 탑들 중 높이가 가장 낮은 탑 -> 모든 케이스를 확인하지 않아도 된다
"""

""""
재귀 호출로 부분 집합 구하기

level : 점원의 수
branch : 포함되느냐 아니냐
"""

T = int(input())

def recur(cnt, total_height):
    global answer
    
    # 기저 조건 가지치기
    # 탑 높이가 B 이상이면 더 이상 쌓을 필요 X
    if total_height >= B:
        answer = min(answer, total_height)
        return
    
    if cnt == N:
        return
    
    # 포함 시키는 경우
    #   -> 현재 키 합에서 포함되는 직원 키 더하기
    recur(cnt + 1, total_height + heights[cnt])
    
    # 포함 시키지 않는 경우      
    recur(cnt + 1, total_height)
    
    
for t in range(T):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = 200001
    
    print(f'#{t + 1}')