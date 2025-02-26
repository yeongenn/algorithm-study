import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

# T = int(input())

# for _ in range(T):
#     N, M = map(int, input().split())
#     docs_to_print = list(map(int, input().split()))
#     docs_w_order = list(enumerate(docs_to_print))
#     # print(docs_w_order)

#     turn = 0
#     print_order = []

#     if N == 1:  # 문서 하나일 때
#         print_order.append(docs_w_order.pop())
#         turn = 1
#     else:
#         while len(docs_w_order) != 1:
#             doc = docs_w_order.pop(0)
#             imp = [x[1] for x in docs_w_order]
            
#             if doc[1] >= max(imp):  # 젤 중요하면
#                 print_order.append(doc)
#             else:
#                 docs_w_order.append(doc)
                
#         else:
#             print_order.append(docs_w_order.pop())

#         # print(print_order)

#         for j in range(N):
#             if print_order[j][0] == M:
#                 turn = j + 1
#                 break

#     print(turn)

#####################################################################################################

# enumerate 미사용 버전 -> 순서 카운트용 flag 추가

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    order = 1 # 프린트할 순서

    while data:
        if data[0] < max(data):
            data.append(data.pop(0))
        else:   # 현재 문서 중요도가 젤 높을 때
            if M == 0: break
            
            data.pop(0)
            order += 1  # 다음에 출력할 프린트 순서 설정

        M = M - 1 if M > 0 else len(data) - 1   # 문서 출력했으니까 순서 재설정

    print(order)