import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

N = int(input())    # 노드 수
tree = [[] for _ in range(N + 1)]

def search(node):
    if node == 0:   # 더 이상 노드 없으면 종료
        return
    
    left = tree[node][0]
    right = tree[node][1]
    
    pre_order.append(chr(node + 64))
    search(left)
    in_order.append(chr(node + 64))
    search(right)
    post_order.append(chr(node + 64))

# 트리 만들기 - 인접 리스트 형태로
# A의 아스키코드 : 65
for _ in range(N):
    node, left, right = input().split()
    node_idx = ord(node) - 64           # 노드 인덱스 1번부터
    left_idx, right_idx = ord(left) - 64, ord(right) - 64
    
    if left != '.':
        tree[node_idx].append(left_idx)
    else:
        tree[node_idx].append(0)
    
    if right != '.':
        tree[node_idx].append(right_idx)
    else:
        tree[node_idx].append(0)
    
# print(tree)

pre_order = []
in_order = []
post_order = []

search(1)

print(''.join(pre_order))
print(''.join(in_order))
print(''.join(post_order))

