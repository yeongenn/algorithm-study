import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

def search(parent, n):    
    visited[n] = 1
        
    for i in range(len(tree[n])):
        # 내가 놓쳤던 부분 - 부모 노드 정보 저장
        # 부모 노드 방문 기록까지 visited에서 조회하게 되면
        # 부모 - 자식 관계에서는 모두 싸이클이 발생하게 되는 꼴
        # 부모 노드 정보는 따로 관리!
        if parent == tree[n][i]: continue
        
        if visited[tree[n][i]]:
            return False
        
        is_tree = search(n, tree[n][i])
        if not is_tree:
            return False
    
    return True

############################# while 문 내 코드는 문제 없음 #############################
# search() 내에서 cycle 체크하는 부분 다시 생각해서 작성하기

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
        tree[e].append(s)       # 트리는 방향 X -> 양방향으로 기록
    # print(*tree)
                
    visited = [0] * (N + 1)
    
    for i in range(1, N + 1):   # 정점 N개 순회
        if not visited[i]:
            a = search(0, i)
            if a:
                T += 1
    
    result = ''
    if T > 1:
        result = f'A forest of {T} trees.'
    elif T == 1:
        result = 'There is one tree.'
    else:
        result = 'No trees.'
        
    print(f'Case {tc}: {result}')
    tc += 1