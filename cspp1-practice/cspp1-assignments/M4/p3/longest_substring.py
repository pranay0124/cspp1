''' author:Pranay Kumar Yenishetty
    date:02-08-2018'''

def main():
    '''This module is to print the longest characters in a string'''
    st_r1 = input()
    st_r2 = ''
    st_r3 = ''
    ma_x = 0
    co_t = 0
    for j in range(len(st_r1)-1):
        if ord(st_r1[j]) <= ord(st_r1[j+1]):
            st_r2 = st_r2 + st_r1[j]
            co_t += 1
        else:
            if ma_x < co_t:
                st_r3 = st_r2 + st_r1[j]
                ma_x = co_t
                co_t = 0
            st_r2 = st_r1[j+1]
    if co_t > ma_x:
        st_r3 = st_r2
    print(st_r3)
if __name__ == "__main__":
    main()
