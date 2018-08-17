'''
    Author : Pranay Kumar Y
    date : 17-08-2018
'''
import re
import collections
import math
'''
def remove_stopword(adict):
    stopword = load_stopwords("stopwords.txt")
    for i in stopword:
        adict.pop(i, None)
    return adict
'''
def calculation(d1):
    num = 0
    den_1 = 0
    den_2 = 0
    for i in d1:
        num += d1[i][0]* d1[i][1]
        den_1 +=  d1[i][0] ** 2
        den_2 += d1[i][1] ** 2
    print(num, den_1, den_2)
    return num/(math.sqrt(den_1) * math.sqrt(den_2)) 

def similarity(dict1, dict2):
    '''lower case, removing special characters and numbers'''
    dict1 = re.sub('[^ a-z]', '', dict1.lower())
    dict2 = re.sub('[^ a-z]', '', dict2.lower()) 
    dict1 = dict1.strip('!@#$%^&*()?><,./;:')    
    dict2 = dict2.strip('!@#$%^&*()?><,./;:')

    #hand = ['0', '1', '2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','?']
    '''replacing " ' " in between words (Eg:we're == were)'''
    dict1 = dict1.replace("'", "")
    dict2 = dict2.replace("'", "")
    
    dict1 = dict1.split()
    dict2 = dict2.split()
    
    '''removing stopwords'''
    stopword = load_stopwords("stopwords.txt")
    key_list = stopword.keys()
    
    for i in key_list:
        for j in dict1:
            if i == j:
                dict1.remove(j)
    
    for i in key_list:
        for j in dict2:
            if i == j:
                dict2.remove(j)
    
    '''writing combined dictionary'''
    dict1 = dict(collections.Counter(dict1))
    dict2 = dict(collections.Counter(dict2))
    combined_dict = {}
    for k in dict1:
        if k in dict2:
            combined_dict[k] = [dict1[k], dict2[k]]
        else:
            combined_dict[k] = [dict1[k], 0]
    for l in combined_dict:
        if l not in combined_dict:
            combined_dict[l] = [0, dict2[l]]

    return (calculation(combined_dict))

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
