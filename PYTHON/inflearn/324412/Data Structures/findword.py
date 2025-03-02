N = int(input())

to_used = [input() for _ in range(N)]
used = [input() for _ in range(N - 1)]

while len(to_used) > 1:
    if to_used[0] in used:
        to_used.pop(0)
    else:
        to_used.append(to_used.pop(0))
else:
    print(*to_used)