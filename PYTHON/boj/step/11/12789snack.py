N = int(input())
order = list(map(int, input().split())) # 현재 줄

stack = []  # 한 명씩 설 수 있는 공간

can_get_snack = True
for i in range(1, N + 1):
    # 현재 줄 서있는 곳에서 대기열로 이동하는데는 조건이 없다 -> 일단 stack에 넣자
    # 현재 번호표랑 맞는지는 pop해서 비교하면 된다 -> stack에 넣기 전에 검사할 필요가 없다는 말
    if (not stack) or (stack and stack[-1] != i):
        while order:
            if order[0] == i:
                order.pop(0)
                break
            else:
                stack.append(order.pop(0))
        else: 
            can_get_snack = False
            break
    elif stack[-1] == i:
        stack.pop()
    else:
        can_get_snack = False
        
print('Nice' if can_get_snack else 'Sad')

"""
타 코드 리뷰

loop 돌리는 대상 - N번까지 번호 뿐만 아니라 현재 줄 서 있는 리스트로도 가능
"""