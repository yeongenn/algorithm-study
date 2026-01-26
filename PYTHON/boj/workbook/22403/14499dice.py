import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

"""
주사위 도면:
    +---+
    | 2 |
+---+---+---+
| 4 | 1 | 3 |
+---+---+---+
    | 5 |
    +---+
    | 6 |
    +---+
"""
dice = [0] * 6

"""
1: 동, 2: 서, 3: 북, 4: 남

1, 2 이동 시 dice[1], dice[4]는 고정
3, 4 이동 시 dice[2], dice[3]은 고정

주사위 제일 윗면: dice[5]
주사위 바닥 면: dice[0]
"""