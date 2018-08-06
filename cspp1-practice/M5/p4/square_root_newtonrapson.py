'''

Author : Pranay Kumar Y
Date : 03-04-2018

'''

def main():
    ''' Square root calculation using newton raphson'''
    num_1 = input()
    epi_1 = 0.01
    int_1 = int(num_1)
    gu_ess = int_1/2.0
    while abs(gu_ess*gu_ess - int_1) >= epi_1:
        gu_ess = gu_ess - (((gu_ess**2) - int_1)/(2*gu_ess))
    print(str(gu_ess))

if __name__ == "__main__":
    main()
