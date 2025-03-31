T = int(input())
for t in range(T):
    o, e = map(int, input().split())
    N = int(input())
    teams = []
    for _ in range(N):
        s, f = map(int, input().split())

        # o ~ e 시간 내에 있는 팀만 추가
        if s >= o and f <= e:
            teams.append([s, f])

    # 종료 시간 기준 정렬
    teams.sort(key=lambda x : (x[1], x[0]))
    n = len(teams)

    count = 1           # 첫번째 팀은 항상 포함
    prev = teams[0][1]  # 첫번째 팀 종료 시간
    for i in range(1, n):
        if teams[i][0] >= prev:
            count += 1
            prev = teams[i][1]  # 이전 팀 종료 시간 갱신

    print(f'#{t + 1} {count}')