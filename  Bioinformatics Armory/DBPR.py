# pip install biopython
# http://biopython.org/DIST/docs/api/

from Bio import ExPASy
from Bio import SwissProt

with ExPASy.get_sprot_raw("Q1BCB9") as handle:
    record = SwissProt.read(handle)
    for r in record.cross_references:
        # biological processes
        if r[0] == "GO" and r[2].startswith("P:"):
            print(r[2].strip("P:"))
