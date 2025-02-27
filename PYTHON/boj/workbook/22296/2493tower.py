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
    pass

print(result)
