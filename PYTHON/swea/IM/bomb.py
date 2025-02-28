import sys
sys.stdin = open("c:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\python\\swea\\input.txt", "r")

T = int(input())

for t in range(T):
    M, N = map(int, input().split())    # 행, 렬
    K = int(input())
    matrix = [list(input()) for _ in range(M)]
    # print(before)

    result = []
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]   # 델타
    # visited = [[0] * N for _ in range(M)]   # 마킹 배열

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == '@':
                matrix[i][j] = '%'
                for x, y in zip(dx, dy):
                    for k in range(1, K + 1):   # 화력만큼
                        nx, ny = i + x * k, j + y * k
                        if 0 <= nx < M and 0 <= ny < N:
                            if matrix[nx][ny] == "_":   # 빈칸 일 때
                                matrix[nx][ny] = '%'
                            else: break
    print(f'#{t + 1}')
    
    for i in range(M):
        for j in range(N):
            print(matrix[i][j], end="")
        print()
    
    