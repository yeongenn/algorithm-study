import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

# 왼쪽 노드 < 현재 노드 < 오른쪽 노드 -> 중위 순회
def make_tree(n):
    global num
    if n <= N:
        make_tree(n * 2)    # left = i * 2  -> '인덱스' 기준 2배!
        arr[n] = num
        num += 1
        make_tree(n * 2 + 1)    # right = i * 2 + 1    

for t in range(T):
    N = int(input())
    arr = [0] * (N + 1)
    num = 1      # 1부터 시작
    make_tree(num)

    print(f'#{t + 1} {arr[1]} {arr[N // 2]}')