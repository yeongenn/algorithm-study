from collections import defaultdict

def findroute(s, linked_dict, visited):
    if visited[s] is False:
        visited[s] = True

    # 키 해당하는 길 없으면
    if len(linked_dict[s]) == 0:
        return 0
    
    # 키 해당하는 길 중에 99 있으면
    if 99 in linked_dict[s]:
        return 1

    r = 0
    while linked_dict[s]:
        n = linked_dict[s].pop(0)
        if not visited[n]:
            r += findroute(n, linked_dict, visited)
            if r >= 1: break
    return r

for t in range(10):
    TC, N = input().split()
    routes = list(map(int, input().split()))
    visited = [False] * 100

    linked = []
    for i in range(0, int(N) * 2, 2):
        linked.append(routes[i:i + 2])

    linked_dict = defaultdict(list)
    for s, e in linked:
        linked_dict[s].append(e)

    result = findroute(0, linked_dict, visited)

    print(f'#{t + 1} {result}')
