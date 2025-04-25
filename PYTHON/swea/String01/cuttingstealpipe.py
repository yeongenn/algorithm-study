import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

# 파이썬 버전
for t in range(T):
    li = input()

    count = 0
    pipe = []
    li = li.replace("()", "L")
    for i in range(len(li)):
        if li[i] == "L":
            if len(pipe) == 0:
                continue
            else:
                count += len(pipe)  # 쌓여있는 파이프 수 만큼 잘린 조각 추가
        elif li[i] == "(":
            pipe.append("O")    # 아무 값이나 넣어도 상관 X
        else:
            pipe.pop()          # 파이프 끝
            count += 1
  
    print(f'#{t + 1} {count}')