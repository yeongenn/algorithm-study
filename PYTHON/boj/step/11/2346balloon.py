################################## w/ deque ##################################
# # deque에는 rotate라는 끝내주는 함수가 있답니다..^^

# from collections import deque

# N = int(input())

# paper = list(map(int, input().split()))
# paper = deque(list(enumerate(paper, 1)))

# result = []

# while len(paper) != 1:
#     now = paper.popleft()
#     step = now[1]   # 풍선 안 종이에 적힌 값
#     result.append(now[0])   # 현재 터뜨리는 풍선 번호
#     if step > 0:
#         paper.rotate(-((step - 1) % len(paper)))
#     elif step < 0:
#         paper.rotate(abs(step) % len(paper))
    
# else: result.append(paper.pop()[0])

# print(*result)

################################## w/o deque ##################################
# index 양수로 맞추려다가 오답 잔치
# tkim : 인덱스가 꼭 양수일 필요는 없잖아? 파이썬에서는 음수인 채로도 연산 가능함ㅎㅋ

N = int(input())

paper = list(map(int, input().split()))
paper = list(enumerate(paper, 1))

index = 0
result = []

while len(paper) != 1:
    now = paper.pop(index)
    step = now[1]
    result.append(now[0])
    
    if step > 0:
        index += (step - 1)
        index %= len(paper)
    else:
        index += step
        index %= len(paper)
else:
    result.append(paper.pop()[0])
    
print(*result)

