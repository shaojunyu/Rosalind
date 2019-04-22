from Bio import Entrez
lines =  open("rosalind_gbk.txt").readlines()
genus = lines[0].strip()
date1 = lines[1].strip()
date2 = lines[2].strip()
term = '(%s[Organism]) AND  ("%s"[Publication Date] : "%s"[Publication Date])' % (genus, date1, date2)
print(term)
Entrez.email = 'hustysj@gmail.com'
handle = Entrez.esearch(db="nucleotide", term=term)
record = Entrez.read(handle)
print(record['Count'])
