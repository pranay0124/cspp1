def mult_matrix(m_1, m_2, r_1, r_2, c_1, c_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    multiplication_matrix = []
    if c_1 == r_2:
        for i in range (r_1):
            temp = []
            for j in range(r_1):
                sum_val = 0
                for k in range(c_1):
                    sum_val = sum_val + (m_1[i][k] * m_2[k][j])
                temp.append(sum_val)
            multiplication_matrix.append(temp)
        return multiplication_matrix
    else:
        return "Error: Matrix shapes invalid for mult"

def add_matrix(m_1, m_2, r_1, r_2, c_1, c_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    addition_matrix = []
    if r_1 == r_2 and c_1 == c_2:
        for i in range (c_1):
            temp = []
            for j in range (c_1):
                temp.append(m_1[i][j] + m_2[i][j])
            addition_matrix.append(temp)
        return addition_matrix
    else:
        return "Error: Matrix shapes invalid for addition"

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    
    dimensions = input().split(",")
    m = int(dimensions[0])
    n = int(dimensions[1])
    mat = []
    # for i in range(n):
    #     mat.append([])
    # for i in range (n):
    #     temp = input().split()
    #     for j in range (n):
    #         mat[i].append(int(temp[j]))
    
    for i in range(0, m):
        mat.append(list(map(int,input().split())))
    
    flag = True
    for i in mat:
        count = 0
        for j in i:
            count += 1
        if count != n:
            flag = False
            
    return mat, m, n, flag


def main():
    (matrix_1, row_1, column_1,flag_1) = read_matrix()

    (matrix_2, row_2, column_2,flag_2) = read_matrix()

    #print(flag_1, flag_2)

    if flag_1 == True and flag_2 == True:
        addition_matrix = add_matrix(matrix_1,matrix_2,row_1,row_2,column_1,column_2)
        multiplication_matrix = mult_matrix(matrix_1,matrix_2,row_1,row_2,column_1,column_2)

        print(addition_matrix)
        print(multiplication_matrix)

    else:
        print("Error: Invalid input for the matrix")
    
if __name__ == '__main__':
    main()
