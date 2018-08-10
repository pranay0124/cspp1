''' Author : Pranay kumar Y
    Date : 10-08-2018'''

def updateHand(hand, word):
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
    n=input()
    adict={}
    for i in range(int(n)):
        data=input()
        l=data.split()
        adict[l[0]]=int(l[1])
    data1=input()
    print(updateHand(adict,data1))
        
if __name__ == "__main__":
    main()