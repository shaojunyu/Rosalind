from Bio import Entrez
from Bio import SeqIO

ids = open("rosalind_frmt.txt").readline().strip().split()
Entrez.email = 'hustysj@gmail.com'
shortest = None
min_len = float('inf')
with Entrez.efetch(db='nucleotide', id=[",".join(ids)], rettype="fasta") as handle:
    records = SeqIO.parse(handle, 'fasta')

    for r in records:
        if min_len > len(r.seq):
            min_len = len(r.seq)
            shortest = r
    print(SeqIO.FastaIO.as_fasta(shortest))
