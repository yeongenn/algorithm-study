N = int(input())

def fibonacci(N):
    if N < 2:
        return N

    return fibonacci(N - 1) + fibonacci(N - 2)

print(fibonacci(N))