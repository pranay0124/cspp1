''' Author : Pranay Kumar Y
    date : 07-08-2018'''

def sum_of_digits(n_1):
    '''function for sum of digits'''
    if n_1 == 0:
        return 0
    return (n_1 % 10) + sum_of_digits(n_1//10)

def main():
    '''main function'''
    a_1 = input()
    print(sum_of_digits(int(a_1)))

if __name__ == "__main__":
    main()
