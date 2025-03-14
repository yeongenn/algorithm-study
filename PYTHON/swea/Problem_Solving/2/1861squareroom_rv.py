""""
1861 정사각형 방

접근 방법 2
1부터 N ** 2를 인덱스로 갖는 배열 A를 만든다
숫자 i의 인접에 1큰 수가 있는 경우 A[i]에 1을 표시한다
연속한 1의 개수가 최대인 경우를 찾는다
"""

T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)     #  + 1 : 인덱스 맞추기

    
    # 현재 위치 숫자 기준 1 큰 곳 확인
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                
                # 인덱스 체크
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue
                
                # 다음 위치가 1 큰 수 인지 체크
                if arr[ny][nx] == arr[y][x] + 1:
                    visited[ny][nx] = 1     # 마킹
                    break                   # 델타 체크 중단
                
    # 연속된 1의 갯수가 가장 긴 곳 찾기
    # 가장 긴 곳, 현재 갯수, 출발 방 숫자
    max_cnt = cnt = start = 0
    for i in range(1, N * N + 1):
        if visited[i]:
            cnt += 1          
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                
                # 연속된 구간에서 마지막 인덱스가 저장 -> 연속된 갯수만큼 빼주면 출발점이 된다
                # 혹은 visited를 역순으로 순회하면 마지막으로 출발점 인덱스가 저장된다
                start = i - cnt             
            cnt = 0                         # 초기화
    
    print(f'#{t + 1} {start} {max_cnt + 1}')