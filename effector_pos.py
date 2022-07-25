from Bio import SeqIO
import pandas as pd

gff = pd.read_table("/shared/home/sbache/annotation_fusarium/assembly/snakemake_functional/output_dir/4_GFF_SORTED/CAV180_SMARTDENOVO_STEP_CORRECTION_MEDAKA/CAV180_SMARTDENOVO_STEP_CORRECTION_MEDAKA_sorted.gff3")
gff.columns = ["contig", "source", "feature", "start", "end", "score1", "strand", "score2", "id"]

gff = gff[gff["feature"] == "gene"]
gff["id"] = gff["id"].str.replace(r'Name=', "")
gff["id"] = gff["id"].str.replace(r'\;[0-9a-zA-Z]*', "")
gff["id"] = gff["id"].str.replace(r'ID=', "")
gff["id"] = gff["id"].str.replace(r'T0_[0-9]*', "T0")

fasta = "/shared/home/sbache/annotation_fusarium/assembly/snakemake_functional/output_dir/5_FINAL_RESULT/EFFECTOR/CAV180_SMARTDENOVO_STEP_CORRECTION_MEDAKA/CAV180_SMARTDENOVO_STEP_CORRECTION_MEDAKA_effector.fasta"

list_id = []
for sequence in SeqIO.parse(fasta, "fasta"):
    list_id.append(sequence.id)

gff = gff[gff["id"].isin(list_id)]

gff.to_csv("gff_effectors_CAV180.gff3", sep = "\t")
