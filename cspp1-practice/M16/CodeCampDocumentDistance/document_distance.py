'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import collections
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    
    dict1 = re.sub('[^ a-zA-Z]','',dict1.lower())
    dict2 = re.sub('[^ a-zA-Z]','',dict2.lower()) 
    dict1 = dict1.strip('!@#$%^&*()?><,./;:')    
    dict2 = dict2.strip('!@#$%^&*()?><,./;:')
    #hand = ['0', '1', '2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','?']
    dict1 = dict1.replace("'","")
    dict2 = dict2.replace("'","")

    dict1 = dict1.split()
    dict2 = dict2.split()
    
    dict1 = dict(collections.Counter(dict1))
    dict1 = dict(collections.Counter(dict1))

    stopword_1 = load_stopwords("stopwords.txt")
    stopword_2 = load_stopwords("stopwords.txt")
    for i in stopword_1:
        dict1.pop(i, None)
    for i in stopword_2:
        dict2.pop(i, None)
    
    

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
