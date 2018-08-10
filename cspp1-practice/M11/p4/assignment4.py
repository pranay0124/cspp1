''' Author : Pranay Kumar Y
    Date : 10-08-2018
'''

def calculate_hand_len(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    sum = 0
    for values in hand.values():
        sum += values
    return sum

def main():
    n_value = input()
    adict = {}
    for _ in range(int(n)):
        data = input()
        l_in = data.split()
        adict[l_in[0]] = int(l_in[1])
    print(calculate_hand_len(adict))

if __name__ == "__main__":
    main()
