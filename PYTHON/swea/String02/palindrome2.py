def max_palindrome(arr):
    max_len = 0
    for r in range(100):
        for c in range(100):
            for end in range(c, 100):
                word = arr[r][c:end + 1]
                if word == word[::-1]:
                    max_len = max(max_len, len(word))
    return max_len

for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    turned_arr = list(map(list, zip(*arr)))[::-1]

    result = max(max_palindrome(arr), max_palindrome(turned_arr))
    print(f'#{tc} {result}')
