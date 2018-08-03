'''
Author : Pranay Kumar Yenishetty
Date : 03-08-2018
'''
def main():
    ''' This algorithm is to guess the secret number '''
    print("Guess a number between 1 and 100")
    mi_n = 0
    ma_x = 100
    mi_d = (mi_n + ma_x)//2
    s_1 = ''
    #print("Is your number greater than M ")
    while s_1 != 'c':
        if s_1 == 'h':
            mi_n = mi_d
            mi_d = (mi_n + ma_x)//2
        if s_1 == 'l':
            ma_x = mi_d
            mi_d = (mi_n + ma_x)//2
        print("Mid number is" + str(mi_d))
        print("Is your number greater than Mid number ?")
        print("Enter 'h' if your number is higher")
        print("Enter 'l' if your number is lower")
        print("Enter 'c' if your number is correct")
        s_1 = input()
    print("Number is : " + str(mi_d))

if __name__ == "__main__":
    main()