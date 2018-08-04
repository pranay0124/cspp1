'''
    author : Pranay Kumar Y
    date : 04-08-2018
'''
def main():
    '''
    Program to print blank spaces in place of special characters in a given string
    '''
    str_1 = input()
    for i in str_1:
        if i in('!', '@', '#', '$', '%', '^', '&', '*'):
            print(" ")
        else:
            print(i)

if __name__ == "__main__":
    main()
