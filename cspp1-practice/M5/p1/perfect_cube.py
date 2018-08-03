'''
Author : Pranay Kumar Yenishetty
Date : 03-08-2018
'''
def main():
    ''' This algorithm is to find the given number is a perfect cube or not '''
    n_1 = int(input("Enter the number"))
    an_s = 0
    while an_s**3 < n_1:
        an_s += 1
    if an_s**3 == n_1:
        print(str(n_1) + ' is a perfect cube')
    else:
        print(str(n_1) + ' is not a perfect cube')
if __name__ == "__main__":
    main()
    