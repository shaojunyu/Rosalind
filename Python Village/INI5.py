i = 1
with open("rosalind_ini5.txt") as IN:
    for line in IN:
        if i % 2 == 0:
            print(line.strip())
        i += 1
