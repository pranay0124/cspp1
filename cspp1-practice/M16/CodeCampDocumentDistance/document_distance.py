'''
    Document Distance - A detailed description is given in the PDF
'''
import re
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
    stopword = load_stopwords("stopwords.txt")
    for word in stopword:
    	if word in dict1:
    		dict1 = dict1.replace(word,"")
    for word in stopword:
    	if word in dict2:
    		dict2 = dict2.replace(word,"")
    print(dict1)
    


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
