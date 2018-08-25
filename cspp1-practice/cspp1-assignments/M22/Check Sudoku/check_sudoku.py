'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def is_horizontal(sudoku):
    set_h = set()
    for i in sudoku:
        for j in i:
            set_h.add(j)
            # print(set_h)
    if len(set_h) == 9:
        return True
    return False

def is_vertical(sudoku):
    set_v = set()
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            set_v.add(sudoku[j][i])
        break
        # set_v.add(i[0])
    if len(set_v) == 9:
        return True
    return False     

def is_matrix(sudoku):
    set_1 = set()
    for i in range(0, 3):
        for j in range(0, 3):
            set_1.add(sudoku[i][j])
    set_2 = set()
    for i in range(0, 3):
        for j in range(3, 6):
            set_1.add(sudoku[i][j])
    set_3 = set()
    for i in range(0, 3):
        for j in range(6, 9):
            set_1.add(sudoku[i][j])
    set_4 = set()
    for i in range(3, 6):
        for j in range(0, 3):
            set_1.add(sudoku[i][j])
    set_5 = set()
    for i in range(3, 6):
        for j in range(3, 6):
            set_1.add(sudoku[i][j])
    set_6 = set()
    for i in range(3, 6):
        for j in range(6, 9):
            set_1.add(sudoku[i][j])
    set_7 = set()
    for i in range(6, 9):
        for j in range(0, 3):
            set_1.add(sudoku[i][j])
    set_8 = set()
    for i in range(6, 9):
        for j in range(3, 6):
            set_1.add(sudoku[i][j])
    set_9 = set()
    for i in range(6, 9):
        for j in range(6, 9):
            set_1.add(sudoku[i][j])

    if len(set_1) == 9 and len(set_2) == 9 and len(set_3) == 9 and len(set_4) == 9 and len(set_5) == 9 and \
        len(set_6) == 9 and len(set_7) == 9 and len(set_8) == 9 and len(set_9) == 9:
        return True
    return False 

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    flag_h = is_horizontal(sudoku)
    flag_v = is_vertical(sudoku)
    flag_m = is_matrix(sudoku)
    if flag_h == True and flag_v == True and flag_m == True:
        return True
    return False

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()