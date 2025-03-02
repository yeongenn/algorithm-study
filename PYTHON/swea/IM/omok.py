import sys, math
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

T = int(input())

def play(x, y, s):
    dx, dy = [-1, 0, 1, 1], [1, 1, 1, 0]    # 우상, 우, 우하, 하
    
    for n, m in zip(dx, dy):
        check = [(x, y)]  # 초기화
        for k in range(1, 19):
            nx, ny = x + n * k, y + m * k
            if 0 <= nx < 19 and 0 <= ny < 19:
                if omok_board[nx][ny] == s:
                    check.append((nx, ny))
                else: break
        if len(check) < 5: continue
        elif len(check) > 5: continue
        else:
            if omok_board[x - n][y - m] != s:
                return 1    # 승부 결정났다고 리턴
            else: return 0  # 바로 이전값이 동일하다면 길이가 5 이상이라는 말이니까
    
    # 여기까지 왔다 -> 결정 안 났다
    return 0

for t in range(T):
    # 0 : X, 1 : 검, 2 : 백
    omok_board = [list(map(int, input().split())) for _ in range(19)]
    result_x, result_y = -1, -1
    final_result = "PLAYING", ''
    
    # 결과는 흑돌 기준
    for i in range(19):
        for j in range(19):
            if omok_board[i][j] != 0:
                is_decided = play(i, j, omok_board[i][j])
                if is_decided:
                    if omok_board[i][j] == 2:   # 백돌이 이겼으면 lose
                        final_result = "Noheul LOSE T.T", (i + 1, j + 1)
                        break
                    else:   # 흑돌 이겼으니 win
                        final_result = "Noheul WIN!", (i + 1, j + 1)
    
    print(f'#{t + 1}', *final_result)
