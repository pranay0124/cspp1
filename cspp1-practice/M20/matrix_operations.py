def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    pass

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    a = input().split(",")
    m = int(a[0])
    n = int(a[1])
    mat = []
    for i in range(n):
    	mat.append([])
    for i in range (m):
    	for j in range (n):
    		mat[i].append(int(input()))
    # for i in range (m):
    # 	for j in range (n):
    # 	    mat[i][j] = int(input().split())
    print(mat)


def main():
    matrix_1 = read_matrix()

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    pass

if __name__ == '__main__':
    main()
