''' Author : Pranay Kumar Y
    Date : 10-08-2018'''
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    count_value = 0
    length_word = len(word)
    for i in word:
        if i in hand:
            count_value += 1

    if l_value == count_value:
        if word in wordList:
            return True
        else:
            return False
    else:
        return False
    
def main():
    ''' main function'''
    word = input()
    n = int(input())
    adict = {}
    for i in range(n):
        data = input()
        l = data.split()
        adict[l[0]] = int(l[1])
    l2 = input().split()
    print(isValidWord(word,adict,l2))
        
if __name__== "__main__":
    main()
