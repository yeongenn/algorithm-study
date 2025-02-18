parenthesis = {
    ")" : "(",
    "]" : "["
}

while True:
    string = input()
    if string == ".": break
    stack = []
    for c in string:
        if c in "([":
            stack.append(c)
        elif c in "])":
            if not stack:
                stack.append(c)
            elif stack[-1] == parenthesis[c]:
                stack.pop()
            else: stack.append(c)
        else:
            continue

    print("yes" if not stack else "no")
