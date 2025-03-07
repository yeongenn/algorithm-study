import sys
sys.setrecursionlimit(10 ** 6)    # recursion error 방지

N = int(input())

def parent(N):
    global visited
    
    visited[N] = 1 if visited[N] == 0 else 0
    
    for n in tree[N]:
        if visited[n] == 1:
            continue
        ans[N].append(n)
        result[n] = N       # 자식의 부모 노드 저장
        parent(n)

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n, i = map(int, input().split())    # 양방향 그래프
    tree[n].append(i)
    tree[i].append(n)    
# print(tree)

ans = [[] for _ in range(N + 1)]    # 루트 1로 하는 그래프
visited = [0] * (N + 1)

result = [0] * (N + 1)      # 결과 출력용

parent(1)   # 1을 최고 루트로 하는 그래프 그리기
# print(ans)
# print(result)

for i in range(2, N + 1):
    print(result[i])
    
# 양방향 그래프 -> 단방향
# 단방향으로 바꾸면서 자식 노드의 부모 노드 저장하기
# 위 코드에서 단방향 그래프 저장용 ans는 필요 X