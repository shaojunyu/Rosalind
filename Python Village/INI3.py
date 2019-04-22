with open("rosalind_ini3.txt") as IN:
    string = IN.readline()
    index = [int(x) for x in IN.readline().split()]
    print(string[index[0]:index[1]+1] + " " + string[index[2]:index[3]+1])
