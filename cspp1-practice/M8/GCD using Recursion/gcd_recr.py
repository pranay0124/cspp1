# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdRecur(a, b):
    minimum_value = min(a, b)
    if minimum_value == a:
    	a, b = b, a
    if a%b == 0:
    	return b
    else:
    	return gcdRecur(b, a%b)

def main():
    data = input()
    data = data.split()
    print(gcdRecur(int(data[0]),int(data[1])))

if __name__== "__main__":
    main()