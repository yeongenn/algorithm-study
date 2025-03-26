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
