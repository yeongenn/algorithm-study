import sys
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

T = int(input())

for t in range(T):
    N = int(input())
    is_counted = [False] * 10
    
    k = 0
    while False in is_counted:
        k += 1
        k_N = str(N * k)
        for i in k_N:
            number = int(i)
            if not is_counted[number]:
                is_counted[number] = True
    
    print(f'#{t + 1} {N * k}')
