class Cipher:
    def __init__(self, text):
        self.text = text
    def shift(self, shift_number):
        small_alphabet = ""
        upper_alphabet = ""
        small_alphabet = "-" + string.ascii_lowercase + string.ascii_lowercase
        upper_alphabet = "-" + string.ascii_uppercase + string.ascii_uppercase
        shifted_string = " "
        for i in range (0, len(self.text)):
            if self.text[i] in small_alphabet:
                shifted_string += small_alphabet[small_alphabet[index(self.text(i))] + shift_number]
            elif self.text[i] in large_alphabet:
                shifted_string += large_alphabet[large_alphabet[index(self.text(i))] + shift_number]
            else:
                shifted_string += self.text[i]

        return(shifted_string)


def main():
    '''
        Function to handle testcases
    '''
    data_input = input()
    shift_number = int(input())
    Cipher_obj = Cipher(data_input)
    Cipher_obj.shift(shift_number)
    
    print(data.apply_shift(int(input())))

if __name__ == "__main__":
    main()
