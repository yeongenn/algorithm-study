T = int(input())

for t in range(T):
    result = 0  # 1 : 면겹, 2 : 선겹, 3 : 점겹, 4 : 겹X
    
    x1, y1, x2, y2 = map(int, input().split()) # 첫번째 사각형
    x3, y3, x4, y4 = map(int, input().split()) # 두번째 사각형

    x_gap, y_gap = 0, 0

    # 총 4가지 경우
    # if x2 < x4 and y2 < y4:
    #     x_gap = x2 - x3
    #     y_gap = y2 - y3

    # elif x2 < x4 and y2 > y4:
    #     x_gap = x2 - x3
    #     y_gap = y4 - y1

    # elif x2 > x4 and y2 < y4:
    #     x_gap = x4 - x1
    #     y_gap = y2 - y3
    # else:
    #     x_gap = x4 - x1
    #     y_gap = y4 - y1

    # x 차이
    if x2 < x4:
        x_gap = x2 - x3
    else: x_gap = x4 - x1

    # y 차이
    if y2 < y4:
        y_gap = y2 - y3
    else: y_gap = y4 - y1

    if x_gap > 0 and y_gap > 0: result = 1
    elif x_gap == 0 and y_gap == 0: result = 3
    elif x_gap == 0 or y_gap == 0: result = 2
    else: result = 4
    
    print(f'#{t + 1} {result}')