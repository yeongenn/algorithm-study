T = int(input())
order = list(map(int, input().split())) # 현재 줄
order.reverse()
stack = []  # 한명씩만 설 수 있는 공간
got_snack = []  # 이미 간식 받은 사람

for i in range(1, T + 1):
        while order and order[-1] != i:
            stack.append(order.pop())
        got_snack.append(order.pop())

        if not order:
            if stack[-1] == i:
                got_snack.append(stack.pop())
            else: print("Sad")

    

