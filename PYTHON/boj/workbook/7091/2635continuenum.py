import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")


N = int(input())    # 양의 정수

num_list = [] * N
num_list.append(N)

max_length = len(num_list)
max_list = num_list

for n in range(N, 0, -1):
    num_list.append(n)
    idx = 2
    while True:
        temp = num_list[idx - 2] - num_list[idx - 1]
        if temp >= 0:
            num_list.append(temp)
        else:
            break
        idx += 1
    
    if max_length <= len(num_list):
        max_length = len(num_list)
        max_list = num_list
    num_list = [N]      # 초기화

print(max_length)
print(*max_list)