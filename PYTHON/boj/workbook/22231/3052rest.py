numbers = [int(input()) for _ in range(10)]

dat = [0] * 42
for num in numbers:
    rest = num % 42
    dat[rest] += 1

result = list(filter(lambda x : x != 0, dat))
print(len(result))