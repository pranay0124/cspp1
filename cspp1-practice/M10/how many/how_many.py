''' Author : Pranay Kumar Y
    Date : 09-08-2018
'''

def how_many(aDict):
    ''' function'''
    val = aDict.values()
    print (val)
    make_list = list(val)
    a = 0
    #print(make_list)
    for i in make_list:
        a += len(i)
    return a
    

def main():
    ''' main function'''
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
    print(how_many(aDict))
    

if __name__== "__main__":
    main()