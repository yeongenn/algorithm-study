T = int(input())

for t in range(T):
    word = input()
    result = 1 if word == word[::-1] else 0
    print(f'#{t + 1} {result}')