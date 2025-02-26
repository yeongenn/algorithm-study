import sys
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

letters = list(input())

result = []
temp = []
while letters:
    if letters[0] == "<":
        if temp:
            result.extend(temp[::-1])
            temp = []
        while letters[0] != ">": # 닫꺽 만날 때까지
            result.append(letters.pop(0))
        else:
            result.append(letters.pop(0))   # 닫꺽 담기
    elif letters[0] == ' ': # 공백일 때 처리
        result.extend(temp[::-1])
        temp = []   # 초기화
        result.append(letters.pop(0))
    else:   # 꺽쇠도 아니고 공백도 아닐 때
        temp.append(letters.pop(0))
else:
    if temp:
        result.extend(temp[::-1])

print(''.join(result))