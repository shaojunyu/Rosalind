output = {}
with open("rosalind_ini6.txt") as IN:
    words = IN.readline().strip().split()
    for w in words:
        if w in output:
            output[w] += 1
        else:
            output[w] = 1
# print(output)
for k, v in output.items():
    print(k + " " + str(v))
