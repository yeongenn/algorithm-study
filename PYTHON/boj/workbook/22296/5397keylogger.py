import sys
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

####################################### 시간 초과 #######################################

T = int(input())

for _ in range(T):
    logged = list(input())
    # print(logged)
    
    password = []
    idx = 0
    for char in logged:
        if char == "<":
            if idx > 0:
                idx -= 1
        elif char == ">":
            if idx < len(password):
                idx += 1
        elif char == "-":
            if idx > 0:
            # password.pop()
                password.pop(idx - 1)
                idx -= 1
        else:
            # password.append(char)
            password.insert(idx, char)
            idx += 1
    print(''.join(password))
    
    # LinkedList로 해보기
    # ???
    
    