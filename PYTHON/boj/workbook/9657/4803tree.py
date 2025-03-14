import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

def search(n):
    pass

############################# while 문 내 코드는 문제 없음 #############################
# search() 내에서 cycle 체크하는 부분 다시 생각해서 작성하기

tc = 1
while True:
    T = 0
    is_tree = True
    
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
        
    tree = [[] for _ in range(N + 1)]
        
    # 인접 리스트 형태로 트리 만들기
    for _ in range(M):
        s, e = map(int, input().split())
        tree[s].append(e)
    print(*tree)
                
    visited = [0] * (N + 1)
    
    for i in range(1, N + 1):
        if not visited[i]:
            search(i)
            if is_tree:
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