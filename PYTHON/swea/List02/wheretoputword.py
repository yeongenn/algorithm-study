T = int(input())

def put_word(puzzle, N, K):
    count = 0
    coordinates = []    # 확인용
    
    for i in range(N):
        for j in range(N - K + 1):
            if puzzle[i][j] == 0:
                continue
            
            blank_r = puzzle[i][j:j + K]
            if 0 in blank_r:
                continue
            
            # 앞뒤로 공간이 있으면 안되니까
            if j > 0:   # 앞
                if puzzle[i][j - 1] == 1:
                    continue
                
            if (j + K) < N: # 뒤
                if puzzle[i][j + K] == 1:
                    continue
                
            
            # coordinates.append((i, j))
            count += 1
    
    # print(coordinates)
    return count   

for t in range(T):
    N, K = map(int, input().split())    # K는 단어 길이
    cross_word_puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    
    result += put_word(cross_word_puzzle, N, K)
    
    turned_puzzle = list(map(list, zip(*cross_word_puzzle)))[::-1]  # 왼쪽으로 90도 돌려서 검사
    result += put_word(turned_puzzle, N, K)
 
    print(f'#{t + 1} {result}')

