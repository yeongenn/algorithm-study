import sys
import pprint
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

N = int(input())
tree = [[0] * (N + 1) for _ in range(N + 1)]
# visited = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    parent, child, w = map(int, input().split())
    tree[parent][child] = w
    tree[child][parent] = w
# pprint.pprint(tree)

q = []
q.append(1)
visited[1] = 0

while q:
    row = q.pop(0)
    visited[row]
    
    for i in range(1, N + 1):
        if tree[row][i] != 0 and not visited[i]:
            q.append(i)
            visited[i] = visited[row] + tree[row][i]
        else:
            continue
        
pprint.pprint(visited)
    
    