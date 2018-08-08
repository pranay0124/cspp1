'''    Author : Pranay Kumar Y
    Date : 08-08-2018
'''
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    temp_stng = secret_word
    for each_char in letters_guessed:
        temp_stng = temp_stng.replace(each_char, "")

    for each_char in temp_stng:
        if each_char != "":
            secret_word = secret_word.replace(each_char, "")
    return secret_word


def main():
    '''
    Main function '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1,len(data)):
        list1.append(data[j][0])
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
