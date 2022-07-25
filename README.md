# Supplementary scripts not included in the workflows

gff_count_genes counts the number of genes per contig in a gff and creates a csv file.

gene_density counts the number of bases included in genes in each contig of an assembly, from a gff and the fasta file of the assembly. The resulting file is used to calculate gene densities per contig.

effector_pos parses the gff to keep only lines corresponding to effectors. The resulting file is used in the Circa plot showing the distribution of effectors.

mimps searchs for a consensus mimp sequence in a fasta file of an assembly and returns a csv file with the positions.

fasta_cazymes create a protein fasta files with only protein sequences corresponding to cazymes.

plot_orthofinder is used to generate a barplot showing the distribution of prthogroups among the assemblies.
