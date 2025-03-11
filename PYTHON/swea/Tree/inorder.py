import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = 2

def read_word(n):   # 중간 노드
    if n <= N:
        read_word(n * 2)        # left
        print(tree[n], end="")
        read_word(n * 2 + 1)    # right

for t in range(T):
    N = int(input())
    tree = ['' for _ in range(N + 1)]
    
    for _ in range(N):
        # i, v, l, r = input().split()
        # tree[int(i)] = v
        temp = list(input().split())
        tree[int(temp[0])] = temp[1]
        
    print(tree)
    
    print(f'#{t + 1}', end=" ")
    read_word(1)
    print()
    