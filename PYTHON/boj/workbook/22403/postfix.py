S = list(input())

postfix = [S[i:len(S) + 1] for i in range(len(S))]
# print(postfix)

# postfix = sorted(postfix, key=lambda p : ord(p[0]))   # 이 방법은 첫번쨰 알파벳만 비교한다

# # 출력
# for p in postfix:
#     print(''.join(p))

postfix = [''.join(p) for p in postfix]
postfix.sort()

for p in postfix:
    print(p)