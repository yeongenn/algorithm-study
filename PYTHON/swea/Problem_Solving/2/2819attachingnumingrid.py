import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

""""
주의할 점

상하좌우로 이동할 때 이동했던 경로를 저장하면서 나아가야 한다

DFS
level : 6
branch : 4개 (상하좌우)

내가 놓쳤던 부분
set....?.....??????
코드 똑같은데...???????????????ㅅㅂ

재귀 호출하는 부분에서 잘못 설계
재귀 호출할 때 문자열을 이미 같이 넘겨주기 때문에 별도의 로직이 필요 X
따라서 string += grid[ny][nx] 이런 거 필요 없음ㅎㅋ
"""

T = int(input())

def recur(y, x, string):
    if len(string) == 7:
        result.add(string)
        return
    
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i, j in zip(dy, dx):
        ny, nx = y + i, x + j
        if 0 <= ny < 4 and 0 <= nx < 4:
            recur(ny, nx, string + grid[ny][nx])
        
      

for t in range(T):
    grid = [list(input().split()) for _ in range(4)]
    # print(grid)
    result = set()
    
    for y in range(4):
        for x in range(4):
            recur(y, x, grid[y][x])

    print(f'#{t + 1} {len(result)}')