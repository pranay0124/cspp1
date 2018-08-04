'''
    author : Pranay Kumar Y
    date : 04-08-2018
'''
def main():
    '''
    Program to print numbers from 1 to N. For multiples of 3 print Fizz,
    for multiples of 5 print Buzz and for multiples of 3&5 print FizzBuzz
       '''
    num = int(input())
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()
