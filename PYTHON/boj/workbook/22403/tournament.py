import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

N, K, L = map(int, input().split())

# K, L 순서 오름차순 보장 X
if K > L:
    K, L = L, K

def is_odd(x):
    if x % 2 == 1:
        return True
    else:
        return False
    
def arrange(y):
    if y % 2 == 1:
        return (y + 1) // 2
    return y // 2

total_round = 1
while N > 1:
    if N % 2 == 0:
        N = N // 2
    else:
        N = (N - 1) // 2
    total_round += 1

for crt_round in range(1, total_round + 1):
    if is_odd(K) and L == (K + 1):
        print(crt_round)
        break
    
    K, L = arrange(K), arrange(L)