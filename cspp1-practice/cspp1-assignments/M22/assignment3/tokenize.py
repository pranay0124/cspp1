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
    temp = []
    for i in range(lines):
    	temp[i] = input()
    	temp[i] = re.sub('[^ a-zA-Z0-9]', '', temp)
    	temp[i] = list(temp.split())
    	for j in range(lines):
    		temp_dict = tokenize(temp)
    	adict.update(temp_dict)
    print(adict)
if __name__ == '__main__':
    main()
