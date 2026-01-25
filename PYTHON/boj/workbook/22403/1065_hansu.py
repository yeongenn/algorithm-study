import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
0 < N <= 1000

1 ~ 99는 반드시 한수 -> 99개
100 이상 자연수에서 한수 카운트
"""

N = int(input())

def to_digits(N):
    digits = []
    while N > 0:
        digits.append(N % 10)
        N //= 10
    digits.reverse()
    return digits

cnt_hansu = 0

if N < 100:
    # 100 미만이면 해당 자연수가 한수 개수
    cnt_hansu = N
else:
    cnt_hansu = 99
    for n in range(100, N + 1):
        digits = to_digits(n)
        gap = digits[1] - digits[0]
        is_hansu = True
        for i in range(2, len(digits)):
            if digits[i] - digits[i - 1] != gap:
                is_hansu = False
                break
    
        if is_hansu:
            cnt_hansu += 1
        
print(cnt_hansu)