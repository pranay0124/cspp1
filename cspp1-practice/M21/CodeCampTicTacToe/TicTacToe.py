
def main():
    rows = 3
    mat = []
    # for i in range(0,rows):
    #   mat.append(list(map(int, input().split())))
    for i in range(rows):
        mat.append([])
    for i in range(rows):
        temp = input().split()
        for j in range(rows):
            mat[i].append(int(temp[j])) 
    print(mat)
    
if __name__ == "main":
    main()