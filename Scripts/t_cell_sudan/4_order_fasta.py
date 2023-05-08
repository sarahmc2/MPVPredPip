file1=open("./tcell_sudan_alleles.fasta").readlines()
output1=open("tcell_sudan_alleles_ordered.fasta", "w")

starts=[]

for i in range(0, len(file1), 2):
        start_pos=int(file1[i].split()[2].strip())
        starts.append(start_pos)
starts=sorted(set(list(starts)))

fasta=file1
for i in range(0, len(starts)):
        sp=starts[i]
        for j in range(0, len(fasta), 2):
                if sp == int(fasta[j].split()[2].strip()):
                        output1.write(fasta[j]+fasta[j+1])
