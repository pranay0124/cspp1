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
    if len(set_h) == 9:
        return True
    return False

def is_vertical(sudoku):
    set_v = set()
    for i in range(len(sudoku)):
        for j in range(len(i)):
            a = int(i[0])
            set_v.add(sudoku[a][j])
        # set_v.add(i[0])
    print(set_v)
    if len(set_v) == 9:
        return True
    return False     

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    print(is_horizontal(sudoku))
    print(is_vertical(sudoku))
    
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