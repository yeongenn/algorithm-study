T = int(input())

def check_rows(sudoku, numbers):
    for i in range(9):
        comp = sorted(sudoku[i])
        if comp != numbers:
            return 0
    return 1

def check_columns(sudoku, numbers):
    for j in range(9):
        comp = []
        for i in range(9):
            comp.append(sudoku[i][j])
        if sorted(comp) != numbers:
            return 0
    return 1

def check_boxes(sudoku, numbers):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            comp = []
            
            for k in range(3):
                comp.extend(sudoku[i + k][j:j + 3])

            if sorted(comp) != numbers:
                return 0
            
    return 1
                
        

for t in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    params = (sudoku, numbers)
    results = [check_rows(*params), check_columns(*params), check_boxes(*params)]
    
    if 0 in results:
        result = 0
    else: result = 1
        
    print(f'#{t + 1} {result}')
