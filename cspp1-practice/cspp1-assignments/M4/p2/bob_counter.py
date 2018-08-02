''' author:Pranay Kumar Yenishetty
    date:02-08-2018'''

def main():
    '''This code prints the number of times bob is repeated in the given string'''
    st_r = input()
    co_t = 0
    for i in range(0, len(st_r)-2):
        if (st_r[i] == 'b' and st_r[i+1] == 'o' and st_r[i+2] == 'b'):
            co_t += 1
    print(co_t)

if __name__ == "__main__":
    main()
