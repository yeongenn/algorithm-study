T = int(input())

for t in range(T):
    li = list(input())
    score = 0
    sum = 0

    for i in range(len(li)):
        if li[i] == "O":
            score += 1
        else:
            score = 0

        sum += score
    print(sum)