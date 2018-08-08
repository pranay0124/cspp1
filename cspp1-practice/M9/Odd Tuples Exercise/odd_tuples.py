''' Author : Pranay Kumar Y
    Date : 08-08-2018'''

def oddTuples(aTup):
    '''function'''
    return aTup[::2]

def main():
    ''' main function'''
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += ((data[j]),)
    print(oddTuples(aTup))
        

if __name__ == "__main__":
    main()
    