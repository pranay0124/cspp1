def is_horizontal(mat):
    for i in mat:
        if i[0] == i[1] and i[0] == i[2]:
            return i[0]
    return False

def is_vertical(mat):
    for i in range(0,3):
        if mat[0][i] == mat[1][i] and mat[0][i] == mat[2][i]:
            return mat[0][i]
    return False

def is_diagonal(mat):
    c = mat[1][1]
    if (c == mat[0][2] and c == mat[2][0]) or (c == mat[0][0] and c == mat[2][2]):
        return c
    return False

def is_valid(mat):
    temp_set = set()
    for i in mat:
        for j in i:
            temp_set.add(j)
    if ('x' in temp_set and 'o' in temp_set) or '.' in temp_set:
        return True
    return False

def main():
    rows = 3
    mat = []
    for i in range(rows):
        mat.append(list(input().split()))
    valid_flag = is_valid(mat)
    flag_h = is_horizontal(mat)
    flag_v = is_vertical(mat)
    flag_d = is_diagonal(mat)
    if valid_flag == False:
        print("invalid input")
    elif flag_h and flag_v and flag_d == False:
        print("draw")
    elif flag_h != False:
        print(flag_h)
    elif flag_v != False:
        print(flag_v)
    else:
        print(flag_d)
    


    
if __name__ == '__main__':
    main()