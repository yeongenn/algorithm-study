import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\yeongenn\\algorithm-study\\PYTHON\\boj\\input.txt", "r")

M = int(sys.stdin.readline())
S = set()

for m in range(M):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == 'all':
            S = set(i for i in range(1, 21))
        elif temp[0] == 'empty':
            S = set()
    else:
        commands, number = temp
        x = int(number)

        if commands == 'add':
            S.add(x)
        elif commands == 'remove':
            S.discard(x)
        elif commands == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif commands == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
