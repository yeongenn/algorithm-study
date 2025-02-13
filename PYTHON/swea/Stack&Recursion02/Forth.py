T = int(input())

for t in range(T):
    order = list(input().split())
    print(order)

    stack = []
    # 연산자 아스키 코드
    # + : 43, - : 45, * : 42, / : 47
    # . : 46
    operand = [43, 45, 42, 47]

    for o in order:
        if ord(o) == 46:
            break
        elif ord(o) not in operand:
            stack.append(int(o))
        else:   # 숫자 두개 꺼내서 결과 다시 스택에 넣기
            a = stack.pop(-1)
            b = stack.pop(-1)
            stack.append(f'{b} {o} {a}')


    print(f'#{t + 1}', *stack)