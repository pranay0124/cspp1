'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
import collections
def print_dictionary(dictionary):
    # dictionary = sorted(dictionary)
    dictionary = dict(collections.OrderedDict(sorted(dictionary.items())))
    for k in dictionary.keys():
        print(k, " - ", dictionary[k])

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
