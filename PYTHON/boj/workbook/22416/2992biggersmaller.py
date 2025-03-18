import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

X = int(input())        # X와 구성이 같으면서 X보다 큰 수 중 가장 작은 수
P = list(map(int, list(str(X)))) 

min_value = 1000000
visited = [0] * len(P)

def get_number(n, arr):
    global min_value
    
    if n == len(P):
        number = int(''.join(map(str, arr)))
        if number > X:
            min_value = min(min_value, number)
        else:
            return
        return
    
    for i in range(len(P)):         # for문 안에서 인덱스 i로 넣어야 하는데 n으로 넣어서 한참 헤맴
        if visited[i]: continue 
        
        visited[i] = 1
        get_number(n + 1, arr + [P[i]])
        visited[i] = 0    

get_number(0, [])

print(0) if min_value == 1000000 else print(min_value)