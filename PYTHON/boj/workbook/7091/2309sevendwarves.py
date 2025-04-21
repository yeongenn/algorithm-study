import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

def sum_of_heights(cnt, total_heights, li):
    global result
    if total_heights > 100:
        return 
    
    if total_heights == 100 and len(li) == 7:
        result = li
        return
    
    if cnt == 9:
        return
    
    sum_of_heights(cnt + 1, total_heights + dwarf[cnt], li + [dwarf[cnt]])
    sum_of_heights(cnt + 1, total_heights, li)

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

result = []     # 결과 출력용 배열

sum_of_heights(0, 0, [])

result.sort()

for r in result:
    print(r)