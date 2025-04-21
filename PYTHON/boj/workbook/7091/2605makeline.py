import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

N = int(input())
numbers = [0] + list(map(int, input().split()))
orders = []        # 순서 리스트

for i in range(1, N + 1):
    if numbers[i] == 0:
        orders.append(i)
    else:
        orders.insert(i - numbers[i] - 1, i)
print(*orders)