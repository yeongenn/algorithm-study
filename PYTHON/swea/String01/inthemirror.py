T = int(input())

for t in range(T):
    string = list(input())
    result = ""

    # b : 98, d : 100 / p : 112, q : 113
    string.reverse()
    for i in range(len(string)):
        if string[i] == 'b' or string[i] == 'd':
            string[i] = chr(198 - ord(string[i]))
        elif string[i] == 'q' or string[i] == 'p':
            string[i] = chr(225 - ord(string[i]))
        
    print(f'#{t + 1} {"".join(string)}')