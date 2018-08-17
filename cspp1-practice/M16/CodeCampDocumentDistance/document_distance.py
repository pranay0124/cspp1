'''
    Author : Pranay Kumar Y
    date : 17-08-2018
'''
import re
import collections
import math
import copy

# def remove_stopword(adict):
#     stopword = load_stopwords("stopwords.txt")
#     for i in stopword:
#         adict.pop(i, None)
#     return adict

def calculation(d_1):
    '''calculates the distance'''
    num = 0
    den_1 = 0
    den_2 = 0
    for i in d_1:
        num += d_1[i][0] * d_1[i][1]
        den_1 += d_1[i][0] ** 2
        den_2 += d_1[i][1] ** 2
    #print(num, den_1, den_2)
    distance = num/(math.sqrt(den_1) * math.sqrt(den_2))
    return distance

def similarity(dict1, dict2):
    '''lower case, removing special characters and numbers'''
    dict1 = re.sub('[^ a-z]', '', dict1.lower())
    dict2 = re.sub('[^ a-z]', '', dict2.lower())

    dict1 = dict1.strip('!@#$%^&*()?><,./;:')
    dict2 = dict2.strip('!@#$%^&*()?><,./;:')

    #hand = ['0', '1', '2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','?']
    #replacing ' in between words (Eg:we're == were)
    dict1 = dict1.replace("'", "")
    dict2 = dict2.replace("'", "")

    dict1 = dict1.split()
    dict2 = dict2.split()

    #removing stopwords
    stopword = load_stopwords()
    key_list = list(stopword.keys())

    word_list = dict1[:]

    for i in word_list:
        if i in key_list:
            dict1.remove(i)

    word_list = dict2[:]

    for i in word_list:
        if i in key_list:
            dict2.remove(i)

    # for i in key_list:
    #     for j in dict1:
    #         if i == j:
    #             dict1.remove(j)

    # for i in key_list:
    #     for j in dict2:
    #         if i == j:
    #             dict2.remove(j)

    # print(dict1)
    # print(dict2)
    #writing combined dictionary
    dict1 = dict(collections.Counter(dict1))
    dict2 = dict(collections.Counter(dict2))

    combined_dict = {}
    for i in dict1:
        if i in dict2:
            combined_dict[i] = [dict1[i], dict2[i]]
        else:
            combined_dict[i] = [dict1[i], 0]
    for j in dict2:
        if j not in combined_dict:
            combined_dict[j] = [0, dict2[j]]

    temp_dict = copy.deepcopy(combined_dict)
    for k in temp_dict:
        if len(k) == 0:
            del combined_dict[k]
    return calculation(combined_dict)

def load_stopwords():
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    filename = "stopwords.txt"
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
