#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def inc(x):
    return x+1

def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    output = (apply_to_each(list1, inc))
    print(output)

if __name__ == "__main__":
    main()
