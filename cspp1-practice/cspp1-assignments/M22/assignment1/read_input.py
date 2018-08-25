'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''main function'''
    lines = int(input())
    temp = []
    for i in range(lines):
        temp.append(input())
    for i in temp:
        print(i)
if __name__ == '__main__':
    main()
