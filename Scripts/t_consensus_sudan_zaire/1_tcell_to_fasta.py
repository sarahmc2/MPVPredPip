file1=open("../t_cell_sudan/iedb_tcells_consensus_table_ordered.txt").readlines()
file2=open("../t_cell_zaire/iedb_tcells_consensus_table_ordered.txt").readlines()
output1=open("./tcell_sudan_zaire.fasta", "w")

db="Sudan Consensus T-cell epitope"
for i in range(1, len(file1)):
        seq=file1[i].split()[1].strip()
        residue_pos=file1[i].split()[3].strip()
        output1.write(">"+db+"\t"+residue_pos+"\n"+seq+"\n")

db="Zaire Consensus T-cell epitope"
for i in range(1, len(file2)):
        seq=file2[i].split()[1].strip()
        residue_pos=file2[i].split()[3].strip()
        output1.write(">"+db+"\t"+residue_pos+"\n"+seq+"\n")
