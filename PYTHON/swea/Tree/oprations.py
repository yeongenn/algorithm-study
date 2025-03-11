import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

import operator

T = 10

operand = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.floordiv
    }

def read_word(n):   # 중간 노드
    if n <= N:
        if len(tree[n]) == 3:   # 자식 노드 있으면
            a = read_word(int(tree[n][1]))    # left
            b = read_word(int(tree[n][2]))    # right
            tree[n][0] = str(operand[tree[n][0]](a, b))
        return int(tree[n][0])

for t in range(T):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    
    for _ in range(N):
        temp = list(input().split())
        tree[int(temp[0])] = temp[1::]
    # print(tree)
    
    result = read_word(1)    
    print(f'#{t + 1} {result}')