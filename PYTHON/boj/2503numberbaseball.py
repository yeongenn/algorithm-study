from itertools import permutations

import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

# 후보군 123 ~ 987
poss = [p for p in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)]

N = int(input())

for _ in range(N):
    number, st, b = map(int, input().split())
    # number to list
    number = list(map(int, str(number)))
    # print(number)
    candidat = []
    for p in poss:
        cnt_s, cnt_b = 0, 0 # 스트 볼 카운트 초기화
        
        for i in range(3):
            if p[i] == number[i]:   # 스트
                cnt_s += 1
            if p[i] != number[i] and number[i] in p:
                cnt_b += 1  # 볼
        
        if cnt_s == st and cnt_b == b:
            candidat.append(p)

    poss = candidat[:]

print(len(poss))
