''' Author : Pranay Kumar Yenishetty
    Date : 06-08-2018'''


def square_num(x_1):
    '''This function is to do the square'''
    x_1 = x_1**2
    return x_1

def main():
    '''main function to do the square'''
    data_in = input()
    data_in = float(data_in)
    temp = str(data_in).split('.')
    if temp[1] == '0':
        print(square_num(int(float(str(data_in)))))
    else:
        print(square_num(data_in))

if __name__ == "__main__":
    main()
