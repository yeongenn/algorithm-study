# S = input()
# bomb = input()

# ########################################### 시간 초과 ###########################################
# in 연산, replace 연산 모두 시간 오래 걸린다

# while S and bomb in S:
#     S = S.replace(bomb, '')
# else:
#     if not S:
#         print("FRULA")
#     else:
#         print(S)
        
################################################################################################

S = input().strip()
bomb = list(input())
stack = []

for s in S:
    stack.append(s)
    
    if len(stack) < len(bomb):
        continue
    else:
        if stack[-len(bomb):] == bomb:
            del stack[-len(bomb):]
            # stack = stack[:-len(bomb)]    # 이렇게 쓰면 시간초과
            
if not stack:
    print("FRULA")
else:
    print(''.join(stack))

################################################################################################

# del stack[-len(bomb):] 과 stack = stack[:-len(bomb)] 차이
# 전자는 정해진 길이(len(bomb))만큼, 후자는 정해진 길이의 '나머지'
# -> 문제 조건에서 문자열 최대 길이는 1,000,000이고 폭탄 문자열 최대 길이는 36
# -> del stack[-len(bomb):]이 훨씬 효율적

