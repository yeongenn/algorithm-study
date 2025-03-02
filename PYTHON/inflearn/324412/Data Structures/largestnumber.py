import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\inflearn\\input.txt", "r")

def peek(stack):
    length = len(stack)
    
    return stack[length - 1] if length > 0 else  -1

T = int(input())
for t in range(T):
    number, m = map(int, input().split())   # m : 제거해야 할 숫자 수

    number = list(map(int, str(number)))

    stack = [number.pop(0)] # 첫번째 숫자 넣고 시작

    while number:
        n = number.pop(0)
        
        if peek(stack) < n:
            while peek(stack) < n and stack and m > 0:
                stack.pop()
                m -= 1  # 숫자 버리기
        stack.append(n)
    else:   # 이때 숫자는 내림차순 정렬이 보장
        if m > 0:   # 제거해야할 숫자가 남아있다면
            # while m > 0:
            #     stack.pop() # pop
            #     m -= 1
            stack = stack[:-m]  # 슬라이싱으로 while문 한 줄로 쓰기

    print(f'{t + 1} {"".join(map(str, stack))}')