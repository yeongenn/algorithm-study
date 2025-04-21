import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_dd = [0] * 5
    B_dd = [0] * 5

    for i in range(1, 1 + A[0]):
        A_dd[A[i]] += 1

    for j in range(1, 1 + B[0]):
        B_dd[B[j]] += 1

    if A_dd[4] != B_dd[4]:
        print('A' if A_dd[4] > B_dd[4] else 'B')
    elif A_dd[3] != B_dd[3]:
        print('A' if A_dd[3] > B_dd[3] else 'B')
    elif A_dd[2] != B_dd[2]:
        print('A' if A_dd[2] > B_dd[2] else 'B')
    elif A_dd[1] != B_dd[1]:
        print('A' if A_dd[1] > B_dd[1] else 'B')
    else:
        print('D')