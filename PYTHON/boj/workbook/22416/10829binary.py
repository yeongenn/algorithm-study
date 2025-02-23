def to_binary(n):
    global result
    
    if n == 1:
        result.append(1)
        return
    elif n % 2 == 0:
        result.append(0)
    else:
        result.append(1)
        
    return to_binary(n // 2)

N = int(input())

result = []
to_binary(N)
print(''.join(map(str, result[::-1])))