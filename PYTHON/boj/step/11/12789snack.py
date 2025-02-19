N = int(input())
order = list(map(int, input().split())) # 현재 줄
order.reverse()

stack = []  # 한 명씩 설 수 있는 공간

can_get_snack = True
for i in range(1, N + 1):
    if stack and order:
        if stack[-1] == i:
            stack.pop()
        elif order[-1] > i and stack[-1] > i:
            can_get_snack = False
            break
        else:
            while order[-1] != i:
                stack.append(order.pop())
            else: order.pop()
    elif not stack and order:
        while order[-1] != i:
            stack.append(order.pop())
        else: order.pop()
    elif stack and not order:
        if stack[-1] != i:
            can_get_snack = False
            break
        else: stack.pop()
        
print('Nice' if can_get_snack else 'Sad')

# 때려처 안해 간식 먹지마
