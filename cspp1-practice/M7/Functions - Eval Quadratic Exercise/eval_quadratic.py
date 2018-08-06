'''
    author : Pranay kumar Y
    date : 06-08-2018
'''
def eval_quadratic(a_1, b_1, c_1, x_1):
    '''Quadratic eqn'''
    return (a_1*(x_1**2)) + (b_1*x_1) + c_1

def main():
    '''quadratic equation'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    k_1 = len(data)
    for x_1 in range(k_1):
        temp = str(data[x_1]).split('.')
        if temp[1] == '0':
            data[x_1] = int(float(str(data[x_1])))
        else:
            data[x_1] = data[x_1]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
