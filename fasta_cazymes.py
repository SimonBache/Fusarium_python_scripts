from Bio import SeqIO
import pandas as pd

caz = pd.read_table("/shared/home/sbache/annotation_fusarium/assembly/snakemake_functional/ancients_resultats/6_CAZYMES/dbcan_UK0001/overview.txt")
caz = caz[caz["#ofTools"] == 3]
list_id = list(caz["Gene ID"])

fasta = "/shared/home/sbache/annotation_fusarium/assembly/snakemake_functional/ancients_resultats/1_PROTEIN_SORTED/UK0001.fasta"

list_keep = []
for sequence in SeqIO.parse(fasta, "fasta"):
    if sequence.id in list_id:
        list_keep.append(sequence)

SeqIO.write(list_keep, "UK0001_cazymes.fasta", "fasta")
