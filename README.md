# Supplementary scripts not included in the workflows

gff_count_genes counts the number of genes per contig in a gff and creates a csv file.

gene_density counts the number of bases included in genes in each contig of an assembly, from a gff and the fasta file of the assembly. The resulting file is used to calculate gene densities per contig.

effector_pos parses the gff to keep only lines corresponding to effectors. The resulting file is used in the Circa plot showing the distribution of effectors.

mimps searchs for a consensus mimp sequence in a fasta file of an assembly and returns a csv file with the positions.

fasta_cazymes create a protein fasta files with only protein sequences corresponding to cazymes.

plot_orthofinder is used to generate a barplot showing the distribution of prthogroups among the assemblies.

effector_prop_plot is an example R file used to generate a barplot. The input file is tabulated table with the names of the contigs in the first column and the proportion of effectors in each contig in the second column. The same types of scripts were used for cazymes proportion/gene density/repeat content plots.
