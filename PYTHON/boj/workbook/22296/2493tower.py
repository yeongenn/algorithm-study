import sys

N = int(sys.stdin.readline())   # 최댓값 500 000
towers = list(map(int, sys.stdin.readline().split()))

def peek(stack):
    length = len(stack)

    if length == 0:
        return -1
    return stack[length - 1]

result = []
stack = []
for i in range(N):
    while stack and towers[peek(stack)] < towers[i]:
        stack.pop()
    else:   
        if not stack:   # stack이 비었다 == 나보다 큰 값 못 만났다
            stack.append(i)
            result.append(0)
        else:
            result.append(peek(stack) + 1)
            stack.append(i)          

print(*result)
