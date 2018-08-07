''' Author : Pranay Kumar Y
    date : 07-08-2018'''

def sum_of_digits(n_1):
    if n_1 == 1:
        return n_1
    else:
        return (n_1 % 10) + sum_of_digits(n_1//10)


def main():
    a_1 = input()
    print(sum_of_digits(int(a_1)))

if __name__ == "__main__":
    main()

