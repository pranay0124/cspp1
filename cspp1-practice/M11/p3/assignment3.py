''' Author : Pranay Kumar Y
    Date : 10-08-2018'''
def is_valid_word(word, hand, word_list):
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

    if length_word == count_value:
        if word in word_list:
            return True
        else:
            return False
    else:
        return False

def main():
    ''' main function'''
    word = input()
    n_value = int(input())
    adict = {}
    for i in range(n):
        data = input()
        l_in = data.split()
        adict[l_in[0]] = int(l_in[1])
    word_s = input().split()
    print(is_valid_word(word, adict, word_s))

if __name__ == "__main__":
    main()
