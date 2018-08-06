'''
    Author : Pranay Kumar Y
    date : 06-08-2018'''

def square(x_1):
    '''square of a number'''
    x_1 = x_1**2
    return x_1

def fourthpower(x_1):
    '''four power of a number'''
    x_1 = square(x_1)**2
    return x_1

def main():
    '''main function to find the fourth power of a given number'''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourthpower(int(float(str(data)))))
    else:
        print(fourthpower(data))

if __name__ == "__main__":
    main()
