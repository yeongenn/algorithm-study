def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

T = int(input())
for t in range(T):
    N = int(input())    # 콘센트 개수
    lst = []            # 정점 좌표
    wires = []          # (a, b, c) : a, b 사이 길이 c
    parents = [x for x in range(N + 1)]
    for i in range(1, N + 1):
        x1, y1 = map(int, input().split())

        wires.append([i, 0, abs(x1) + abs(y1)])     # 차단기
        for j in range(len(lst)):                   # 나머지 콘센트
            x_len, y_len = abs(lst[j][0] - x1), abs(lst[j][1] - y1)
            wires.append([i, j + 1, x_len + y_len])

        lst.append([x1, y1])

    wires.sort(key=lambda x : x[2]) # 전선 길이 기준 정렬

    cnt = 0
    result = 0
    for a, b, c in wires:
        if find_set(a) != find_set(b): # 순환 연결 아닐 때
            union(a, b)
            cnt += 1
            result += c

    print(f'#{t + 1} {result}')