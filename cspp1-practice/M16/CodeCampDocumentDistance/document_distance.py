'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    
    dict1 = dict1.lower().split()
    dict2 = dict2.lower().split()
    dict1 = dict(dict1)
    dict2 = dict(dict2)
    dict1 = dict1.strip('!@#$%^&*()?><,./;:')    
    dict2 = dict2.strip('!@#$%^&*()?><,./;:')
    #hand = ['0', '1', '2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','?']
    
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = str(input())
    input2 = str(input())

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()