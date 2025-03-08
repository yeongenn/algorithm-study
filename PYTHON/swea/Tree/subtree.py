import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

def tree(root):
    result = 1  # 루트 노드 본인은 항상 포함
    if len(edges[root - 1]) == 0: return 1
    
    q = edges[root - 1]
    for i in range(len(q)):
        result += tree(q[i])
    
    return result
    
for t in range(T):
    E, N = map(int, input().split())    # E : 간선 수, N : 루트 노드
    arr = list(map(int, input().split()))
    
    edges = [[] for _ in range(max(arr))]
    
    for i in range(0, len(arr), 2):
        edges[arr[i] - 1].append(arr[i + 1])
        
    result = tree(N)           
        
    print(f'#{t + 1} {result}')