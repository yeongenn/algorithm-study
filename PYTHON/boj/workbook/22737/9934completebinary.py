import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

K = int(input())        # 트리 깊이
buildings = list(map(int, input().split()))     # 방문 순서 - 중위 순회
result = [[] for _ in range(K)]
checked = [0] * (len(buildings) + 1)

# 이진 탐색으로 중위 순회 -> 노드 삽입(?) 순서
def search(level,left, right):
    global result
    
    if level >= K:  # 깊이 체크
        return
    
    if left > right or left < 0 or right > len(buildings):  # 교차했거나 인덱스 범위 넘어가면
        return
    
    if left == right:   # 왼 == 오면 해당값 저장
        if not checked[buildings[left]]:
            result[level].append(buildings[left])
            checked[buildings[left]] = 1
    
    mid = (left + right) // 2

    if not checked[buildings[mid]]:
        result[level].append(buildings[mid])
        checked[buildings[mid]] = 1

    search(level + 1, left, mid - 1)    # 왼쪽 자식 노드 탐색
    search(level + 1, mid + 1, right)   # 오른쪽 자식 노드 탐색
    
search(0, 0, len(buildings))
    
for i in range(K):      # 출력하기
    print(*result[i])