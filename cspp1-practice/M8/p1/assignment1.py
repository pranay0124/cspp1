''' Author : Pranay Kumar Y
    Date : 07-08-2018
    '''

def factorial_num(n_1):
	'''recursive function for factorial'''
    if n_1 == 1 or n_1 == 0:
        return n_1
    else:
        return n_1 * factorial_num(n_1 - 1)

def main():
	'''main function'''
    a_1 = input()
    print(factorial_num(int(a_1)))

if __name__ == "__main__":
    main()
