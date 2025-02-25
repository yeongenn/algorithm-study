import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    imp = list(enumerate(docs))
    # print(imp)

    turn = 0

    if N == 1:
        turn = 1
    else:
        for i in range(N):
            if imp[i][1] >= max(docs[i::]):
                continue
            else:
                imp.append(imp.pop(i))

        for j in range(N):
            if imp[j][0] == M:
                turn = j
                break

    print(turn)