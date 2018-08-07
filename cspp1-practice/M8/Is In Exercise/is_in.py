''' Author : Pranay Kumar Y
    Date : 07-08-2018'''
def isIn_2(char,aStr):
    sorted_aStr = sorted(aStr)
    x = isIn(0,len(sorted_aStr),char,sorted_aStr)
    return x

def isIn(minimum,maximum,char,aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid = (minimum+maximum)//2
    if aStr[mid] == char:
        return "True"
    elif mid == minimum or mid == maximum:
        return "False"
    else:
        if aStr[mid] > char:
            return isIn(minimum,mid,char,aStr)
        elif aStr[mid] < char:
            return isIn(mid,maximum,char,aStr)

def main():
    data = input()
    data = data.split()
    print(isIn_2(data[0], data[1]))


if __name__ == "__main__":
    main()