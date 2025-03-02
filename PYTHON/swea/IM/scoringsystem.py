import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    answers = list(map(int, input().split()))
    submitted = [list(map(int, input().split())) for _ in range(N)]
    
    max_scored = 0
    min_scored = M * (M + 1) // 2   # 최대 점수
    
    for s in submitted:
        score = 0   # 학생별 총점
        point = 1   # 기본 점수
        for i in range(M):
            if s[i] == answers[i]:
                score += point
                point += 1
            else:
                point = 1   # 리셋
                
        max_scored = max(score, max_scored)
        min_scored = min(score, min_scored)
            
    print(f'#{t + 1} {max_scored - min_scored}')