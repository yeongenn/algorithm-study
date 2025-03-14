import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

# to solve

from collections import deque

tc = 1
while True:
    T = 0
    
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
        
    tree = [[] for _ in range(N + 1)]
        
    # 인접 리스트 형태로 트리 만들기
    for _ in range(M):
        s, e = map(int, input().split())
        tree[s].append(e)
        
    # # 트리 확인
    # # nodes = deque([n for n in range(1, N + 1)])
    # visited = [0] * (N + 1)
    # for i in range(1, N + 1):
    #     if visited[i]:
    #         continue
        
    #     for j in range(len(tree[i])):
    #         if visited[tree[i][j]]:
    #             T += 1
    #         else:
                
    
    # 나머지 개별 노드 확인
    
    print(f'Case {tc}: ', *tree)
    tc += 1
