import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")

W, H = map(int, input().split())
N = int(input())

if W == 0 and H == 0:
    print(0)
    exit()
    
h, v = [0, H], [0, W]
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        h.append(b)
    else: v.append(b)

h.sort()
v.sort()

# print(h, v)

# 가로 길이
w_len = 0
for i in range(len(v) - 1):
    w_len = max(w_len, v[i + 1] - v[i])
    
# 세로 길이
h_len = 0
for i in range(len(h) - 1):
    h_len = max(h_len, h[i + 1] - h[i])
    
print((w_len) * (h_len))