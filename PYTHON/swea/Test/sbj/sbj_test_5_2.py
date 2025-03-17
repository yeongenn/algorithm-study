# 완전 이진 트리~
T = int(input())

def search(n):
    if n > N:
        return

    # 자식 노드 인덱스
    left = n * 2
    right = n * 2 + 1

    preorder.append(nodes[n])
    search(left)
    inorder.append(nodes[n])
    search(right)
    postorder.append(nodes[n])

def to_number(arr):     # 10진수로 변환
    arr.reverse()
    num = 0
    for i in range(len(arr)):
        if int(arr[i]) == 1:
            num += 2 ** i

    return num

for t in range(T):
    N = int(input())    # 정점 수
    nodes = [0] + list(map(int, input().split()))   # 인덱스 조정
    result = 0

    preorder = []
    inorder = []
    postorder = []

    search(1)   # 1번 노드부터 순회

    result = max(to_number(preorder), to_number(inorder), to_number(postorder))

    print(f'#{t + 1} {result}')