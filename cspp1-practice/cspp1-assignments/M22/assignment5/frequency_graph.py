'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    dictionary = dict(sorted(dictionary.items()))
    for i in dictionary:
    	n = dictionary.values()
    	value = ""
    	for j in range(n+1):
    		value = value + "#"
    	print(value)
    for k in dictionary.keys():
        print(k, "-", dictionary[k])

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
