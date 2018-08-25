'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	''' function for frequency graph'''
    dictionary = dict(sorted(dictionary.items()))
    for k in dictionary.keys():
        print(k, "-", '#' * dictionary[k])

def main():
	'''main funcition'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
