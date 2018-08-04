'''
    author : Pranay Kumar Y
    date : 04-08-2018
'''
def main():
    '''
    Program to print blank spaces in place of special characters in a given string
    '''
    str_1 = input()
    str_2 = ''
    for i in str_1:
        if i in('!', '@', '#', '$', '%', '^', '&', '*'):
            str_2 = str_2 + " "
        else:
            str_2 = str_2 + i 
    print(str_2)

if __name__ == "__main__":
    main()
