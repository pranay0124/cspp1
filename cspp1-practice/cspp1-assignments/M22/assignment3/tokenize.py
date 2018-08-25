'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import collections
import re
def tokenize(string):
    '''tokenize function'''
    string = dict(collections.Counter(string))
    return string
        
def main():
    '''main function'''
    lines = int(input())
    adict = {}
    temp = ""
    for i in range(lines):
        tep = input()
        tep = re.sub('[^ a-zA-Z0-9]', '', tep)
        temp = temp + " " + tep
    temp = re.sub('[^ a-zA-Z0-9]', '', temp)
    temp = list(temp.split())
    adict = tokenize(temp)
    print(adict)
if __name__ == '__main__':
    main()
