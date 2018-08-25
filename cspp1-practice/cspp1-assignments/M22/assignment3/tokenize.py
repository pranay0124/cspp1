'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import collections
import re
def tokenize(string):
    string = dict(collections.Counter(string))
    return string
            
def main():
    lines = int(input())
    adict = {}
    for i in range(lines):
    	temp = input()
    	temp = re.sub('[^ a-zA-Z0-9]', '', temp)
    	temp = list(temp.split())
    	adict.update(tokenize(temp))
    print(adict)
if __name__ == '__main__':
    main()
