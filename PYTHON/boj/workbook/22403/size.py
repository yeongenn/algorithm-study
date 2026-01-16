import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

# 몸무게 x, 키가 y -> 덩치 (x, y)
# 키와 몸무게 모두 커야 덩치가 크다
# 나보다 더 큰 덩치의 사람 k -> 내 덩치 등수 k+1
# 같은 덩치 등수 여러명 가능

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
bigger_than_me = [0] * N 

for i in range(N):
    for j in range(i, N):
        # 나보다 덩치 큰 사람 카운트
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            bigger_than_me[i] += 1
        # 나보다 덩치 작은 사람 카운트
        elif people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            bigger_than_me[j] += 1
print(*[x + 1 for x in bigger_than_me])