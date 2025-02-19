from collections import deque

T = 10

for t in range(T):
    tc = int(input())
    numbers = deque(map(int, input().split()))    
    
    while True:
        for i in range(1, 6):
            temp = numbers.popleft()
            if temp - i <= 0:
                numbers.append(0)
                break
            else:
                numbers.append(temp - i)
        if numbers[-1] == 0:
            break

    print(f'#{t + 1}', *numbers)