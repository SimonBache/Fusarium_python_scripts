import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import sys
import re

query = re.compile("TT[TA]TTGC[ATCG][ATCG]CCCACTG")
list_pos = []
list_contig = []

for record in SeqIO.parse(open(sys.argv[1],'r'),'fasta'):
    for match in query.finditer(str(record.seq)):
        list_pos.append(match.end())
        list_contig.append(record.id)

df = pd.DataFrame(list_pos, list_contig)
df.columns = ["end_pos"]
df.to_csv(sys.argv[2])
