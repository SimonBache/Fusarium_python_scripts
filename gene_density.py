from Bio import SeqIO
import pandas as pd

list_contig = []
list_total_gene_base = []
count = 0

fasta = "/home/bache/PycharmProjects/pythonProject1/new_assemblies/fasta_N90%/CAV3049_SMARTDENOVO_STEP_CORRECTION_MEDAKA.fasta"
for sequence in SeqIO.parse(fasta, "fasta"):
    list_contig.append(sequence.id)

for sequence in list_contig:
    gff = pd.read_table("/home/bache/PycharmProjects/pythonProject1/new_assemblies/annotation/CAV3049_SMARTDENOVO_STEP_CORRECTION_MEDAKA/CAV3049_SMARTDENOVO_STEP_CORRECTION_MEDAKA_merge.gff3")
    gff.columns = ["contig", "source", "feature", "start", "end", "score", "strand", "score_2", "id"]
    gff = gff[gff["feature"] == "gene"]
    count = 0
    gff = gff[gff["contig"] == sequence]
    for index, row in gff.iterrows():
        count = count + (row['end'] - row['start'])
    list_total_gene_base.append(count)

df = pd.DataFrame(list_contig)
df["total_gene_base"] = list_total_gene_base
df.to_csv("total_gene_base_3049.csv")
