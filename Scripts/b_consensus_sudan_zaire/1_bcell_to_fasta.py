file1=open("./abcpred_output_sudan.txt").readlines()
file2=open("./abcpred_output_zaire.txt").readlines()
output1=open("./bcell_sudan_zaire.fasta", "w")

db="Sudan ABCPred B-cell epitope"
for i in range(1, len(file1)):
        seq=file1[i].split()[1].strip()
        start_pos=int(file1[i].split()[2])
        end_pos=start_pos+len(seq)-1
        output1.write(">"+db+"\t"+str(start_pos)+"\t"+str(end_pos)+"\n"+seq+"\n")

db="Zaire ABCPred B-cell epitope"
for i in range(1, len(file2)):
        seq=file2[i].split()[1].strip()
        start_pos=int(file2[i].split()[2])
        end_pos=start_pos+len(seq)-1
        output1.write(">"+db+"\t"+str(start_pos)+"\t"+str(end_pos)+"\n"+seq+"\n")
