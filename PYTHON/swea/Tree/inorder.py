import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = 2

def read_word():
    pass

for t in range(T):
    N = int(input())
    tree = ['' for _ in range(N)]
    
    for _ in range(N):
        i, v, l, r = input().split()
        tree[int(i)] = v
    print(tree)
    
    print(f'#{t + 1}')