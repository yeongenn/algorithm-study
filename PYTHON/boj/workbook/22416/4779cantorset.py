# input 사용 시 eof
# try - except로 처리
def cantor_set(n, section):
    global my_set
        
    pass
        

while True:
    try:
        N = int(input())
        my_set = [1] * (3 ** N)
        # print(cantor_set)
        n = 3 ** (N - 1)

        section = []
        section.append(n)   # 시작점(?) 설정
        
        cantor_set(n, section)
        print(my_set)
    except:
        break