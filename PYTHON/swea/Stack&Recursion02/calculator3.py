import operator

in_stack = {
    "(" : 0,
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2
}
coming = {
    "(" : 3,
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2
}

oper = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.floordiv
}

T = 10   # 확인용

for t in range(T):
    N = int(input())
    expression = input()
    stack = []
    numbers = []

    for c in expression:
        if c in "(+-*/":
            if stack:
                while in_stack[stack[-1]] >= coming[c]:
                    numbers.append(stack.pop())
                    if not stack: break
            stack.append(c)
        elif c == ")":
            while stack[-1] != "(":
                numbers.append(stack.pop())
            stack.pop() # 열.괄은 날리기

        else:
            numbers.append(c)   # 변환없이 일단 push

    while stack:    # 남은 연산자 다 출력
        numbers.append(stack.pop())

    # 연산하기
    result = []
    for o in numbers:
        if o not in "+-*/":
            result.append(int(o))
        else:
            a = result.pop()
            b = result.pop()
            result.append(oper[o](b, a))
    print(f'#{t + 1}', *result)