'''
    author : Pranay Kumar Y
    date : 04-08-2018
'''
def main():
    '''
    Program to find the products of all the digits of a given number
    '''
    int_1 = int(input())
    int_2 = abs(int_1)
    int_3 = 0
    mu_l = 1
    len_1 = len(str(abs(int_1)))
    while len_1 > 0:
        int_3 = int_2 % 10
        mu_l = mu_l * int_3
        int_2 = int_2 // 10
        len_1 -= 1
    if int_1 > 0:
        print(mu_l)
    else:
        mu_l = mu_l * -1
        print(mu_l)

if __name__ == "__main__":
    main()
