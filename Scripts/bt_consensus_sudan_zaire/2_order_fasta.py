file1=open("./bt.fasta").readlines()
output1=open("./bt_ordered.fasta", "w")

starts=[]
for i in range(0, len(file1), 2):
        start=float(file1[i].split()[1].split("-")[0].strip())
        starts.append(start)
starts=sorted(list(set(starts)))

for i in range(0, len(starts)):
        start=starts[i]
        for j in range(0, len(file1), 2):
                if start == float(file1[j].split()[1].split("-")[0].strip()):
                        output1.write(file1[j].strip()+"\n"+file1[j+1].strip()+"\n")