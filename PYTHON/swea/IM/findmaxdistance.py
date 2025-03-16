import sys
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

T = int(input())

for t in range(T):
    K = int(input())    # 포함되어야 하는 A 갯수
    string = list(input())
    result = 0
    
    N = len(string)
    
    for i in range(N - K + 1):
        for j in range(K, N - i + 1):
            temp = string[i:i + j]
            
            if temp.count('A') == K and temp[0] == 'A' and temp[-1] == 'A':
                result = max(result, len(temp) - 1)
                break
    
    print(f'#{t + 1} {result}')
    