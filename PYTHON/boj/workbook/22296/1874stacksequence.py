import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

n = int(input())

def peek(stack):
    length = len(stack)

    if length == 0:
        return -1
    return stack[length - 1]

comp = [x for x in range(1, n + 1)]
given = [int(input()) for _ in range(n)]

stack = []  # comp에서 pop한 숫자 담을 스택
oper = []   # 연산 종류 담을 리스트
# while comp:
#     if peek(stack) == given[0]:
#         oper.append("-")
#         given.pop(0)
#         stack.pop()
#     else:
#         oper.append("+")
#         stack.append(comp.pop(0))
# else:
#     while stack:
#         if peek(stack) == given[0]:
#             oper.append("-")
#             given.pop(0)
#             stack.pop()
#         else:
#             print("NO")
#             sys.exit()  # exit 안 쓸려면 flag 하나 세우면 된다

# # 다 통과했으면 출력
# for o in oper:
#     print(o)

#####################################################################################################

# 위 코드는 중복 되는 부분이 발생
# push 오름차순이 보장 -> 하나씩 처리하다가 조건 안 맞으면 잘못된 케이스
flag = True

for now in given:
    while comp and comp[0] <= now:
        stack.append(comp.pop(0))
        oper.append("+")

    # comp에서 다 빼냈으면 stack만 보면 된다
    # while에서 따로 분기할 필요 X
    if peek(stack) == now:
        stack.pop()
        oper.append("-")
    else:
        flag = False

if not flag:
    print("NO")
else:
    for o in oper:
        print(o)