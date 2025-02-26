# input 사용 시 eof
# try - except로 처리
def cantor_set(n, s):
    global my_set
    if n == 0:
        return
    
    k = 3 ** (n - 1)
    my_set[(s + k):(s + 2 * k)] = [' '] * k
    
    # return도 안 만났는데 for문 실행도 안되고 종료 -> 뭐지 -> 디버깅으로 인덱스 문제 인지
    # 시작점 현재 기준으로 삼는 것까지는 했는데 끝점을 멍청하게 놓쳐버림;;
    for i in range(s, s + 3 ** n, k):
        cantor_set(n - 1, i)
    
while True:
    try:
        N = int(input())
        my_set = ['-'] * (3 ** N)

        cantor_set(N, 0)
        # print(my_set)
        print(''.join(map(str, my_set)))
        
    except:
        break
    
# 분할정복 인덱스 설정 너무 헷갈린다
# !!! 시작점과 끝점은 '현재' 위치 기준 !!!
