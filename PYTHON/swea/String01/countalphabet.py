T = int(input())

for t in range(T):
    word = list(input())
    alphabet = [0] * 26

    for char in word:
        alphabet[ord(char) - 97] += 1

    print(f'#{t + 1}', *alphabet)