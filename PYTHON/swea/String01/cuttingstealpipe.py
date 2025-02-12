T = int(input())

# 파이썬 버전
for t in range(T):
    li = input()

    count = 0
    pipe = []
    li = li.replace("()", "L")
    for i in range(len(li)):
        if li[i] == "L":
            if len(pipe) == 0:
                continue
            else:
                count += len(pipe)
        elif li[i] == "(":
            pipe.append("1")
        else:
            pipe.pop()
            count += 1
  
    print(f'#{t + 1} {count}')