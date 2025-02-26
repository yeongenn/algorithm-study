letters = input()

result = []

def peek(stack):
    length = len(stack)

    if length == 0:
        return -1
    return stack[length - 1]

while letters:
    temp = []
    if peek(letters) == "<":
        while peek(letters) != ">": # 닫꺽 만날 때까지
            result = letters.pop(0)
    else:
        while peek(letters) != " ": # 공백 만날 때까지
            temp.append(letters.pop(0))
        else:
            result.extend(temp[::-1])
            result.append(letters.pop(0))   # 공백 출력
else:
    pass