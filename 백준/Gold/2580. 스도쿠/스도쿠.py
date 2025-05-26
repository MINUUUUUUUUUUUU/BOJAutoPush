import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

def sudoku(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                numbers = check(i, j, puzzle)
                # print(numbers)
                for num in numbers:
                    puzzle[i][j] = num
                    if sudoku(puzzle):
                        return puzzle
                    puzzle[i][j] = 0
                return False
    return True
                
                
def check(i, j, puzzle): # 가능한 숫자들을 리턴해야
    
    possible = set()
    for k in range(1,10):
        possible.add(k)
    
    row = set(puzzle[i])
    col = set()
    for k in range(9):
        col.add(puzzle[k][j])
        
    ## box
    box = set()
    if i % 3 == 0:
        if j % 3 == 0:
            box.add(puzzle[i][j+1])
            box.add(puzzle[i][j+2])
            box.add(puzzle[i+1][j])
            box.add(puzzle[i+1][j+1])
            box.add(puzzle[i+1][j+2])
            box.add(puzzle[i+2][j])
            box.add(puzzle[i+2][j+1])
            box.add(puzzle[i+2][j+2])
        elif j % 3 == 1:
            box.add(puzzle[i][j+1])
            box.add(puzzle[i][j-1])
            box.add(puzzle[i+1][j])
            box.add(puzzle[i+1][j+1])
            box.add(puzzle[i+1][j-1])
            box.add(puzzle[i+2][j])
            box.add(puzzle[i+2][j+1])
            box.add(puzzle[i+2][j-1])
        elif j % 3 == 2:
            box.add(puzzle[i][j-1])
            box.add(puzzle[i][j-2])
            box.add(puzzle[i+1][j])
            box.add(puzzle[i+1][j-1])
            box.add(puzzle[i+1][j-2])
            box.add(puzzle[i+2][j])
            box.add(puzzle[i+2][j-1])
            box.add(puzzle[i+2][j-2])
    elif i % 3 == 1:
        if j % 3 == 0:
            box.add(puzzle[i][j+1])
            box.add(puzzle[i][j+2])
            box.add(puzzle[i+1][j])
            box.add(puzzle[i+1][j+1])
            box.add(puzzle[i+1][j+2])
            box.add(puzzle[i-1][j])
            box.add(puzzle[i-1][j+1])
            box.add(puzzle[i-1][j+2])
        elif j % 3 == 1:
            box.add(puzzle[i][j+1])
            box.add(puzzle[i][j-1])
            box.add(puzzle[i+1][j])
            box.add(puzzle[i+1][j+1])
            box.add(puzzle[i+1][j-1])
            box.add(puzzle[i-1][j])
            box.add(puzzle[i-1][j+1])
            box.add(puzzle[i-1][j-1])
        elif j % 3 == 2:
            box.add(puzzle[i][j-1])
            box.add(puzzle[i][j-2])
            box.add(puzzle[i+1][j])
            box.add(puzzle[i+1][j-1])
            box.add(puzzle[i+1][j-2])
            box.add(puzzle[i-1][j])
            box.add(puzzle[i-1][j-1])
            box.add(puzzle[i-1][j-2])
    elif i % 3 == 2:
        if j % 3 == 0:
            box.add(puzzle[i][j+1])
            box.add(puzzle[i][j+2])
            box.add(puzzle[i-1][j])
            box.add(puzzle[i-1][j+1])
            box.add(puzzle[i-1][j+2])
            box.add(puzzle[i-2][j])
            box.add(puzzle[i-2][j+1])
            box.add(puzzle[i-2][j+2])
        elif j % 3 == 1:
            box.add(puzzle[i][j+1])
            box.add(puzzle[i][j-1])
            box.add(puzzle[i-1][j])
            box.add(puzzle[i-1][j+1])
            box.add(puzzle[i-1][j-1])
            box.add(puzzle[i-2][j])
            box.add(puzzle[i-2][j+1])
            box.add(puzzle[i-2][j-1])
        elif j % 3 == 2:
            box.add(puzzle[i][j-1])
            box.add(puzzle[i][j-2])
            box.add(puzzle[i-1][j])
            box.add(puzzle[i-1][j-1])
            box.add(puzzle[i-1][j-2])
            box.add(puzzle[i-2][j])
            box.add(puzzle[i-2][j-1])
            box.add(puzzle[i-2][j-2])
            
    for k in range(1,10):
        # 행열체크
        if k in row or k in col or k in box:
            possible.discard(k)
    return possible

answer = sudoku(board)
for a in answer:
    print(*a)