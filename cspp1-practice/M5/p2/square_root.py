'''
Author: Pranay Kumar Yenishetty
Date: 03-02-2018
'''

def main():
    ''' This algorithm is used to calcualte square root '''
    s_1 = input()
    ep_i = 0.01
    gu_ess = 0.0
    inc_r = 0.1
    while abs(gu_ess ** 2 - int(s_1)) >= ep_i and gu_ess <= int(s_1):
        gu_ess += inc_r
    if abs(gu_ess ** 2 - int(s_1)) >= ep_i:
        print('Failed on square root of' + str(s_1))
    else:
        print(gu_ess)

if __name__ == "__main__":
    main()
