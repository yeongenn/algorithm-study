import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
# sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

# def hide_and_seek(n, k):
#     pass

# N, K = map(int, input().split())

# if N > K:
#     print(K - N)
# elif N == K:
#     print(0)
# else:
#     pass

# """
# # dp 배열 관리해야겠지?? 

# N < K:
#     재귀(K)

# 재귀함수(K):
#     # 종료 조건 어떻게 설정?
#     if [조건]:
#         return dp[K] ???

#     if K % 2 == 0:
#         return 재귀함수(K // 2)
#     else:
#         return 1 + 재귀함수(K + 1)
# """

##################################################################################

# 1. x - 1, x + 1 순서에 따라 결과 달라짐
#   ? 왜 ?
#       - curr * 2 가 최대한 많으면 유리 (이것까지는 이해)
#       - * 2를 많이 쓰기 위해서는 반대로 - 1이 많을수록 유리 (인덱스 이유인가...?)

# 2. 방문 배열 체크 안하면 시간 초과 뜸

def hide_and_seek(start, end):
    pq = [(0, start)]   # 시작점까지는 0초
    checked = [0] * 100001

    while pq:
        sec, curr = pq.pop(0)     # 
        
        if curr == end:
            return sec
        
        # 갈 수 있는 노드 추가
        if curr * 2 > 0 and curr * 2 < 100001 and not checked[curr * 2]:
            pq.append((sec, curr * 2))
            checked[curr * 2] = 1
        if curr - 1 >= 0 and not checked[curr - 1]:
            pq.append((sec + 1, curr - 1))
            checked[curr - 1] = 1
        if curr + 1 < 100001 and not checked[curr + 1]:
            pq.append((sec + 1, curr + 1))
            checked[curr + 1] = 1

N, K = map(int, input().split())

print(hide_and_seek(N, K))