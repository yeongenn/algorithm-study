from itertools import permutations

import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

# 후보군 123 ~ 987
poss = [p for p in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)]
candidat = []

N = int(input())

for _ in range(N):
    number, st, b = map(int, input().split())
    # number to list
    number = list(map(int, str(number)))
    print(number)
    for p in poss:
        cnt_s, cnt_b = 0, 0 # 스트 볼 카운트 초기화
        # if p[0] == number[0] and p[1] != number[1] and p[2] != number[2]:
        #     cnt_s += 1
        
        pass