'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import collections
def tokenize(string):
    string = dict(collections.Counter(string))
    return string
            
def main():
    lines = int(input())
    for i in range(lines):
    	temp = list(input())
    	tokenize(temp)
    print(temp)
if __name__ == '__main__':
    main()
