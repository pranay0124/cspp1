''' Author : Pranay Kumar Y
    Date : 07-08-2018
    '''

def factorial_num(n_1):
    if n_1 == 1:
        return n_1
    else:
        return n_1 * factorial(n_1 - 1)    

def main():
    a = input()
    print(factorial_num(int(a)))    

if __name__ == "__main__":
    main()
