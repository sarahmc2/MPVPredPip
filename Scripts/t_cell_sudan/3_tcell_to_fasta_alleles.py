file1=open("./iedb_1_immunogenicity_output.txt").readlines()
file2=open("./tepitool_2_output.txt").readlines()
file3=open("./tcell_sudan.fasta").readlines()
output1=open("./tcell_sudan_alleles.fasta", "w")

for i in range(1, len(file3), 2):
                seq=file3[i].strip()
                mhc=file3[i-1].split("-")[1].split()[0].strip()
                alleles=[]
                a=0
                for j in range(1, len(file1)):
                        if seq == file1[j].split()[0].strip() and mhc == "I":
                                score=float(file1[j].split()[2].strip())
                                allele=file1[j].split()[3].strip()
                                if score > 0:
                                        alleles.append(allele)
                output1.write(file3[i-1].strip())
                a=len(alleles)
                if a == 0:
                        output1.write("\n"+file3[i].strip()+"\n")
                elif a == 1:
                        output1.write("\t"+alleles[0].strip()+"\n"+file3[i].strip()+"\n")
                elif a > 1:
                        output1.write("\t")
                        for k in range(0, len(alleles)-1):
                                output1.write(alleles[k].strip()+";")
                        output1.write(alleles[-1].strip()+"\n"+file3[i].strip()+"\n")
