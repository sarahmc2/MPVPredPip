file1=open("./tepitool_2_output.txt").readlines()
output1=open("./tepitool_2_output_seqs.txt", "w")

seqs=[]
for i in range(1, len(file1)):
        seq=file1[i].split()[3].strip()
        seqs.append(seq)
seqs=list(set(seqs))

output1.write(file1[0].strip()+"\n")
for i in range(0, len(seqs)):
        seq=seqs[i].strip()
        alleles=[]
        for j in range(1, len(file1)):
                if seq == file1[j].split()[3].strip():
                        n=j
                        allele=file1[j].split()[5].strip()
                        alleles.append(allele)
        output1.write(file1[n].split("HLA-")[0].strip())
        alleles=list(set(alleles))
        a=len(alleles)
        if a == 1:
                output1.write("\t"+alleles[0]+"\n")
        if a > 1:
                output1.write("\t")
                for k in range(0, len(alleles)-1):
                        output1.write(alleles[k]+";")
                output1.write(alleles[-1]+"\n")
