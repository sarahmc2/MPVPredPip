file1=open("./tepitool_1_output.txt").readlines()
file2=open("./iedb_1_immunogenicity_output.txt").readlines()
file3=open("./tepitool_2_output_seqs.txt").readlines()
output1=open("./tcell_sudan.fasta", "w")

immuno=file2
seqs=[]

db="MHC-I epitope"
for i in range(1, len(file1)):
        seq=file1[i].split()[3].strip()
        score= -1
        y=0
        for j in range(1, len(immuno)):
                if seq == immuno[j].split()[0].strip() and y==0:
                        score=float(immuno[j].split()[2].strip())
                        immuno.pop(j)
                        y=1
                        if score > 0 :
                                start_pos=int(file1[i].split()[1])
                                end_pos=start_pos+len(seq)-1
                                if seq not in seqs:
                                        output1.write(">"+db+"\t"+str(start_pos)+"\t"+str(end_pos)+"\n"+seq+"\n")
                                        seqs.append(seq)
                                        seqs=list(set(seqs))
                                        break
                                break
                        break

db="MHC-II epitope"
for i in range(1, len(file3)):
        seq=file3[i].split()[3].strip()
        start_pos=int(file3[i].split()[1])
        end_pos=start_pos+len(seq)-1
        alleles=file3[i].split()[5].strip()
        output1.write(">"+db+"\t"+str(start_pos)+"\t"+str(end_pos)+"\t"+alleles+"\n"+seq+"\n")