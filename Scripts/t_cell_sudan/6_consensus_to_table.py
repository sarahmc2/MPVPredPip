file1=open("./iedb_tcells_consensus.txt").readlines()
uniport_seq=open("../sudan.fasta").readlines()
output1=open("./iedb_tcells_consensus_table.txt", "w")


output1.write("Epitope No.\tT-cell MHC-I and MHC-II consensus epitope sequence\tLength\tResidue Positions\n")

n=1
for i in range(0,len(file1)):
        if file1[i].split("\t")[1]=="Consensus":
                seq=file1[i].split("\t")[2].strip()
                length=str(len(seq))
                start_pos=uniport_seq[1].index(seq)+1
                end_pos=start_pos+len(seq)-1
                output1.write(str(n)+"\t"+seq+"\t"+str(length)+"\t"+str(start_pos)+"-"+str(end_pos)+"\n")
                n=n+1