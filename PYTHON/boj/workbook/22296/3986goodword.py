import sys
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

def peek(stack):
    length = len(stack)
    
    if length == 0:
        return "C"
    return stack[length - 1]

N = int(input())
words = [list(input()) for _ in range(N)]
# print(words)

bads = 0
for word in words:
    stack = []
    for w in word:
        if peek(stack) == w:
            stack.pop()
        else:
            stack.append(w)
    if stack:   # 스택에 아직 남아있으면 교차했다는 말이니까
        bads += 1
        
print(N - bads)