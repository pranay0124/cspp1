'''
    author:Pranay
    date:02-08-2018
    '''

def main():
    '''this function is to display vowels in a given string'''
    s_t = input()
    co_t = 0
    for ch_r in s_t:
        if ch_r in ('a', 'e', 'i', 'o', 'u'):
            co_t += 1
    print("Number of vowels:", str(co_t))

if __name__ == "__main__":
    main()
