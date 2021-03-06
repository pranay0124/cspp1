''' Author : Pranay Kumar Y
    Date : 24th August, 2018'''
def is_horizontal(mat):
    '''horizontal function'''
    for i in mat:
        if i[0] == i[1] and i[0] == i[2]:
            return i[0]
    return False
    # for i in range(len(mat)):
    #     if mat[i][0] == mat[i][1] and mat[i][0] == mat[i][2]:
    #         return mat[i][0]
    # return False

def is_vertical(mat):
    '''vertical function'''
    for i in range(0, 3):
        if mat[0][i] == mat[1][i] and mat[0][i] == mat[2][i]:
            return mat[0][i]
    return False

def is_diagonal(mat):
    '''diagonal function'''
    center_1 = mat[1][1]
    if ((center_1 == mat[0][2] and center_1 == mat[2][0]) \
    or (center_1 == mat[0][0] and center_1 == mat[2][2])):
        return center_1
    return False

def is_valid(mat):
    '''if the game has valid characters'''
    temp_set = set()
    for i in mat:
        for j in i:
            temp_set.add(j)
    if ('x' in temp_set and 'o' in temp_set) or '.' in temp_set:
        if 'p' not in temp_set:
            return True
    return False

def is_count(mat):
    '''if a single character is repeated more than other character'''
    count_x = 0
    count_o = 0
    count_sp = 0
    # sum = 0
    # for i in mat:
    #     sum += i.count("x") + i.count("o") + i.count(".")
    for i in mat:
        for j in i:
            if j == 'x':
                count_x += 1
            elif j == '0':
                count_o += 1
            else:
                count_sp += 1
    if count_x > 5 or count_o > 5:
        return False
    # if count_x == count_o or count_sp == count_x:
    #     return False
    return True

def main():
    '''main tictactoe function'''
    rows = 3
    mat = []
    for _ in range(rows):
        mat.append(list(input().split()))

    flag_h = is_horizontal(mat)
    flag_v = is_vertical(mat)
    flag_d = is_diagonal(mat)
    count_flag = is_count(mat)
    if not count_flag:
        print("invalid game")
    else:
        valid_flag = is_valid(mat)
        if not valid_flag:
            print("invalid input")
        else:
            if not flag_h  and not flag_v and not flag_d:
                print("draw")
            # elif flag_h != False and flag_v != False:
            #     print("invalid game")
            elif flag_h:
                print(flag_h)
            elif flag_v:
                print(flag_v)
            elif flag_d:
                print(flag_d)
            else:
                print("invalid game")

if __name__ == '__main__':
    main()
