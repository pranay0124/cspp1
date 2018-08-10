''' Author : Pranay kumar Y
    Date : 10-08-2018'''

def update_hand(hand, word):
    """
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    for i in word:
        if i in hand:
            hand[i] -= 1
    #for j in adict:
     #   if adict[j] > 0:
      #      print (adict[j])
    return hand

def main():
    '''main function'''
    n_value = input()
    adict = {}
    for _ in range(int(n_value)):
        data = input()
        l_in = data.split()
        adict[l_in[0]] = int(l_in[1])
    data1 = input()
    print(update_hand(adict, data1))

if __name__ == "__main__":
    main()
