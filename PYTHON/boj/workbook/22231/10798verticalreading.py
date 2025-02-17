import itertools

N = 5
result = []
words = [list(input()) for _ in range(N)]
for i in zip(itertools.zip_longest(*words, fillvalue="")):
    result.extend(*i)

print("".join(result))