import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

N, S = map(int, input().split())

# 처음 작성했던 코드 맞긴 한데

# 내가 놓쳤던 부분
# S가 0인 경우, 처음에 넘어가는 0이 카운트가 되버림
# 그래서 subset 생성해서 길이가 0 초과인 경우로 관리하려고 했는데
# n번쨰 포함하지 않은 재귀 호출하면서 중복 카운트 발생 -> 이 경우는 visited...?가 필요한가...?
# 처음 코드로 돌아와서 S가 0인 경우 별도 처리
def get_count(n, sum):
    global count
    
    if n == N:
        if sum == S:
            count += 1
        return
        
    get_count(n + 1, sum + arr[n])
    get_count(n + 1, sum)
    
arr = list(map(int, input().split()))
count = 0

get_count(0, 0)

if S == 0:      
    count -= 1

print(count)