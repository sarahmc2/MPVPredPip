file1=open("../b_consensus_sudan_zaire/iedb_bcells_consensus_table_ordered.txt").readlines()
file2=open("../t_consensus_sudan_zaire/iedb_tcells_consensus_table_ordered.txt").readlines()
output1=open("bt.fasta", "w")

type="B-cell_consensus_epitope"
for i in range(1, len(file1)):
        seq=file1[i].split()[1].strip()
        residue_pos=file1[i].split()[3].strip()
        output1.write(">"+type+"\t"+residue_pos+"\n"+seq+"\n")

type="T-cell_consensus_epitope"
for i in range(1, len(file2)):
        seq=file2[i].split()[1].strip()
        residue_pos=file2[i].split()[3].strip()
        output1.write(">"+type+"\t"+residue_pos+"\n"+seq+"\n")