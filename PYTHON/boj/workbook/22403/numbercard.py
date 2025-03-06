N = int(input())
sangguen = list(map(int, input().split()))
sangguen.sort()     # 이분 탐색 위해서 정렬
M = int(input())
numbers = list(map(int, input().split()))
result = [0] * M

for i in range(M):
    left, right = 0, N - 1
    
    # 이중 for문 쓰면 시간 초과 -> 이분탐색
    while left <= right:
        mid = (left + right) // 2
        
        if numbers[i] == sangguen[mid]:
            result[i] = 1
            break
        elif numbers[i] < sangguen[mid]:
            right = mid - 1
        elif numbers[i] > sangguen[mid]:
            left = mid + 1
print(*result)