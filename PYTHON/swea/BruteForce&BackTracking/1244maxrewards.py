import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

""""
그리디로 접근하면 X - 반례있음

완전 탐색으로 접근 - 다 서로 바꿔보자

최대 숫자 자리 수 : 6자리
최대 교환 횟수 : 10번

-> 모든 경우의 수 = 30 ^ 10
    
-> 경우의 수 줄이기
    -> 1 <-> 2 는 2 <-> 1과 동일 -> 절반으로 줄어든다
    -> 모든 경우의 수 = 15 ^ 10 <- 여전히 오래 걸림
    
-> 재귀 호출의 최적화
1. 경우의 수 줄이기 (가지치기)
2. 중복 제거하기
    - 1번 뒤집었는데; 같은 수가 나오면 나올 수 있는 경우의 수가 모두 동일
    - 이런 케이스가 많겠지
    - visited로 해결부터 해보자 - swap_cnt, number 함께 저장
"""

# level(종료 조건) : 교환 횟수
# branch : i, j 스왑 경우의 수
def dfs(swap_cnt):
    global max_result
    if swap_cnt == total_swap_cnt:
        # Todo : 최대 상금
        # number : 문자열 list 형태 -> int로 형변환 해줘야
        max_result = max(max_result, int(''.join(number)))       
        return
    
    # 모든 케이스를 swap 하도록 구현
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            number[i], number[j] = number[j], number[i]
            
            # swap_cnt 만에 사용하지 않는 숫자라면 재귀 호출
            str_number = ''.join(number)        # 형변환
            if visited.get((swap_cnt, str_number)) is None:
                visited[(swap_cnt, str_number)] = 1
                dfs(swap_cnt + 1)
                # visited[(swap_cnt, str_number)] = 0     # 언마킹 안해도 되는 이유 : 어차피 보지 않는 경우기 때문에
            
            number[i], number[j] = number[i], number[j]     # 돌아왔을 때 swap 했던 수들을 원래 상태로 돌려준다    

T = int(input())
for t in range(T):
    number, total_swap_cnt = input().split()
    number = list(number)
    total_swap_cnt = int(total_swap_cnt)
    
    visited = {}    # key : (몇 번 swap, swap 후 숫자)    
    max_result = -1     # 최대 상금
    dfs(0)
    
    print(f'#{t + 1} {max_result}')