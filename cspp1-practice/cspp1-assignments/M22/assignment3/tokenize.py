'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    string = list(collections.Counter(string))
    return string
            
def main():
    lines = int(input())
    for i in range(lines):
    	temp = input()
    	tokenize(temp)
    print(temp)
if __name__ == '__main__':
    main()
