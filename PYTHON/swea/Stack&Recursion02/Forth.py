import operator

T = int(input())

for t in range(T):
    order = list(input().split())
    # print(order)

    stack = []
    ###################eval 안된답니다###################
    # operand = ['+', '-', '*', '/']
    
    # for o in order:
    #     if o == '.':
    #         break
    #     elif o not in operand:
    #         stack.append(int(o))
    #     else:
    #         try: 
    #             a = stack.pop(-1)
    #             b = stack.pop(-1)
    #             stack.append(eval(f'{b} {o} {a}'))
    #         except:
    #             stack = ['error']
            
    operand = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.floordiv
    }
    
    for o in order:
        if o == '.':
            break
        elif o not in list(operand.keys()):
            stack.append(int(o))
        else:
            try:
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(operand[o](b, a))
            except:
                stack = ['error']

    print(f'#{t + 1}', *stack)
