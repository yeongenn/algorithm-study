N, M = map(int, input().split())
baskets = [0] * (N + 1)

for _ in range(M):
    # i번 바구니부터 j번 바구니까지, k번 번호가 적혀있는 공 넣기
    i, j, k = map(int, input().split())
    for idx in range(i, j + 1):
        baskets[idx] = k  
print(*baskets[1:])