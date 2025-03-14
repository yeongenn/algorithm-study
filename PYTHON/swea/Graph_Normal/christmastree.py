import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

def dfs(node):
    if node == -1: return   # 더 이상 확인할 자식 노드가 없으면 종료
    
    # 어느 방법이든 왼쪽, 오른쪽 탐색은 동일
    left = ornms[node][0]
    right = ornms[node][1]
    
    # 1. 부모 먼저 확인
    # print(node, end=" ")
    # dfs(left)
    # dfs(right)
    
    # 2. 왼쪽 보고 부모 확인
    # dfs(left)
    # print(node, end=" ")
    # dfs(right)
    
    # 3. 왼오 모두 보고 부모 확인
    # dfs(left)
    # dfs(right)
    # print(node, end=" ")
    
    preorder.append(node)       # root - left - right => pre
    dfs(left)
    inorder.append(node)        # left - root - right => in
    dfs(right)
    postorder.append(node)      # left - right - root => post

for t in range(T):
    N = int(input())
    ornms = [[] for _ in range(N + 1)] 
    for _ in range(N):
        n, l, r = map(int, input().split())
        ornms[n].append(l)
        ornms[n].append(r)
    # print(ornms)
    
    # 순서별 노드 따로 저장하기
    inorder = []        # 중위
    preorder = []       # 전위
    postorder = []      # 후위
  
    print(f'#{t + 1}')
    dfs(1)      # 시작점은 1(root node of this tree)
    print(*inorder)
    print(*preorder)
    print(*postorder)
    