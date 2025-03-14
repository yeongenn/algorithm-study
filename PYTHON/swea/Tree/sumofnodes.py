import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

def get_node_value(n):  # n : 현재 노드 번호
    if n > N: return 0  # 노드 번호 넘어가면 종료
    
    if n >= N - M + 1:
        return tree[n]
    
    return get_node_value(n * 2) + get_node_value(n * 2 + 1)    # 왼쪽 노드 + 오른쪽 노드

for t in range(T):
    N, M, L = map(int, input().split())     # N : 노드 개수, M : 리프 노드 갯수, L : 출력할 노드 번호
    tree = [0] * (N + 1)
    for _ in range(M):
        i, v = map(int, input().split())
        tree[i] = v
    
    print(f'#{t + 1} {get_node_value(L)}')
    
    """"
    완전 이진 트리
    
    마지막 레벨을 제외한 모든 노드는 완전히 채워져 있어야 한다
    또한 최하단 레벨의 노드는 좌측만 노드가 채워져 있거나 좌측과 우측 모두 채워져 있어야 한다
    
    ex)    (O)          (X)
            1            1
           / \          / \
          2   3        2   3
         / \          /     \
        4   5        4       5
    """