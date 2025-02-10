for i in range(10):
    tc = int(input())
    
    # 0 : 우, 1 : 하, 2 : 좌
    dx = [0, 1, 0]
    dy = [1, 0, -1]

    ladders = [list(map(int, input().split())) for _ in range(100)]    
    start = 0
    
    for c in range(100):
        x, y = 0, c     # 좌표
        
        if ladders[x][y] == 0:
            continue
        
        dir = 1 # 아래가 기본 방향
        while x < 99:
            if dir == 1:
                if y > 0 and ladders[x][y - 1] == 1:    # 좌
                    dir = 2
                elif y < 99 and ladders[x][y + 1] == 1: # 우
                    dir = 0
            else:
                if ladders[x + 1][y] == 1:  # 아래
                    dir = 1
            
            # 이동
            x += dx[dir]
            y += dy[dir]
            
        if ladders[x][y] == 2:
            start = c
            break

    print(f'#{tc} {start}')
