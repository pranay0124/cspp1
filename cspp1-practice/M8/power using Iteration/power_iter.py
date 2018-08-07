''' Author : Pranay Kumar Y
    date : 07-0-2018'''

def iter_Power(base, exp):
    '''function to find the base^exp
    '''
    base_1 = 1
    while exp >= 1:
        base_1 *=  base
        exp -= 1
    return base_1


def main():
    '''main function'''
    data = input()
    data = data.split()
    print(iter_Power(float(data[0]),int(data[1]))) 

if __name__ == "__main__":
    main()
