import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

def hide_and_seek(n, k):
    pass

N, K = map(int, input().split())

if N > K:
    print(K - N)
elif N == K:
    print(0)
else:
    pass

"""
# dp 배열 관리해야겠지?? 

N < K:
    재귀(K)

재귀함수(K):
    # 종료 조건 어떻게 설정?
    if [조건]:
        return dp[K] ???

    if K % 2 == 0:
        return 재귀함수(K // 2)
    else:
        return 1 + 재귀함수(K + 1)
"""