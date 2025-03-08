N = int(input())

scores = list(map(int, input().split()))
M = max(scores)
avg = sum(scores) / N

new_avg = avg / M * 100     # 새로운 평균
print(new_avg)