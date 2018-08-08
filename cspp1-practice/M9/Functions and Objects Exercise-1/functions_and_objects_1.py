''' Author : Pranay Kumar Y
    Date : 08-08-2018'''


def apply_to_each(L, f):
    ''' function'''
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

def main():
    '''main function'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    output = apply_to_each(list1, abs)
    print (output)

if __name__ == "__main__":
    main()
