stat = {"A": 0, "C": 0, "G": 0, "T": 0}
with open('rosalind_ini.txt') as IN:
    s = IN.readline().strip()
    for i in range(len(s)):
        l = s[i]
        stat[l] += 1

print(stat)
for k, v in stat.items():
    print(v, end=" ")
