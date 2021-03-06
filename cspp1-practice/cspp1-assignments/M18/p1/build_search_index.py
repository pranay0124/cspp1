'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
import collections
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    #print(text)
    words_list = re.sub('[^ a-z]', '', text.lower())
    words_list = words_list.replace("'", "")
    words_list = words_list.split()

    stopword = load_stopwords("stopwords.txt")
    key_list = list(stopword.keys())

    copy_words_list = words_list[:]

    for i in copy_words_list:
        if i in key_list:
            words_list.remove(i)

    return words_list

def build_search_index(docs_list):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    a_1 = docs_list
    #docs = docs_list
    final_dict = {}
    for i, _ in enumerate(a_1):
        a_1[i] = word_list(a_1[i])
        a_1[i] = collections.Counter(a_1[i])
    for k, l_1 in enumerate(a_1):
        for word in l_1:
            if word in final_dict:
                final_dict[word].append((k, a_1[k][word]))
            else:
                final_dict[word] = [(k, a_1[k][word])]
    return final_dict

# helper function to print the search index
# use this to verify how the search index looks

def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))


if __name__ == '__main__':
    main()
