file1=open("./iedb_bcells_consensus.txt").readlines()
sudan=open("../sudan.fasta").readlines()
zaire=open("../zaire.fasta").readlines()
output1=open("./iedb_bcells_consensus_table.txt", "w")


output1.write("Epitope No.\tConsensus Sudan and Zaire sequences of B-cell epitopes predicted by ABCPred\tLength\tResidue Position Sudan\tResidue Position Zaire\n")

n=1
for i in range(0,len(file1)):
	if file1[i].split("\t")[1]=="Consensus":
		seq=file1[i].split("\t")[2].strip()
		length=str(len(seq))
		start_pos_sudan=sudan[1].index(seq)+1
		end_pos_sudan=start_pos_sudan+len(seq)-1
		start_pos_zaire=zaire[1].index(seq)+1
		end_pos_zaire=start_pos_zaire+len(seq)-1
		output1.write(str(n)+"\t"+seq+"\t"+str(length)+"\t"+str(start_pos_sudan)+"-"+str(end_pos_sudan)+"\t"+str(start_pos_zaire)+"-"+str(end_pos_zaire)+"\n")
		n=n+1