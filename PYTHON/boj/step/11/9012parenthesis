T = int(input())

def is_vps(string):
    result = False
    ps_stack = []
    for ps in string:
        if ps == "(" or not ps_stack or ps_stack[-1] != "(":
            ps_stack.append(ps)
        else:
            ps_stack.pop()
        
    if not ps_stack:
        result = True

    return result

for t in range(T):
    string = input()
    print("YES" if is_vps(string) else "NO")