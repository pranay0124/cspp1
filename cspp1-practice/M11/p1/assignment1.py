'''
    Author : Pranay Kumar Y
    Date : 10-08-2018'''

def get_word_score(word, num):
    """
    Returns the score for a word. Assum_valuees the word is a valid word.

    The score for a word is the sum_value of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    scrabble_letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

    sum_value = 0
    length_word = len(word)
    for i in word:
        sum_value += scrabble_letter_values[i]
    x_1 = sum_value*length_word
    if num == length_word:
        x_1 += 50
    return x_1

def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()
