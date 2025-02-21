def plus(n):
    if n <= 3:
        return 2 ** (n - 1)
    
    return plus(n - 1) + plus(n - 2) + plus(n - 3)

N = int(input())

for t in range(N):
    n = int(input())
    print(plus(n))

# 피보나치를 계속 풀어서 그런가 직전 2개 합만 생각이 나고 직전 3개일 거라고는 생각이 바로 안남...
# 수열, 조합... 별 아이디어 다 생각해봄
# 다시 f(1)부터 적어보다가 f(4)에서 직전 3개 합 발견! 휴~