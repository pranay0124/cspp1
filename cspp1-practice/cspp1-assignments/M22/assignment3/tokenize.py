'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import collections
def tokenize(string):
    string = dict(collections.Counter(string))
    print(string)
            
def main():
    lines = int(input())
    for i in range(lines):
    	temp = list(input().split())
    	tokenize(temp)
if __name__ == '__main__':
    main()
