a, b = map(int, input().split())

a = int(''.join(list(str(a))[::-1]))
b = int(''.join(list(str(b))[::-1]))

print(a) if a > b else print(b)

