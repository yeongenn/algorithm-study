def peek(stack):
    length = len(stack)
    
    if length == 0:
        return -1
    return stack[length - 1]

for t in range(10):
    N, P = input().split()
    stack = []

    for n in P:
        if len(stack) == 0 or n != peek(stack):
            stack.append(n)
        else:
            stack.pop()

    print(f'#{t + 1}', ''.join(map(str, stack)))