import pprint
from BCBio import GFF
from BCBio.GFF import GFFExaminer
import pandas as pd

in_file = "/home/bache/PycharmProjects/pythonProject1/new_assemblies/annotation/CAV3049_SMARTDENOVO_STEP_CORRECTION_MEDAKA/CAV3049_SMARTDENOVO_STEP_CORRECTION_MEDAKA_merge.gff3"

genes = []
contigs_id = []

in_handle = open(in_file)
for rec in GFF.parse(in_handle):
    contigs_id.append(rec.id)
    genes.append(len(rec.features))
in_handle.close()


data = pd.DataFrame(genes, index = contigs_id)
data.to_csv("gene_number_CAV3049_smart.csv")
