file1=open("./iedb_btcells_consensus_table.txt").readlines()
output1=open("iedb_btcells_consensus_table_ordered.txt", "w")

starts=[]

for i in range(1, len(file1)):
        start_pos=int(file1[i].split("-")[0].split()[-1])
        starts.append(start_pos)
starts=sorted(set(list(starts)))

output1.write(file1[0].strip()+"\n")
n=1
for i in range(0, len(starts)):
	sp=starts[i]
	for j in range(1, len(file1)):
		if sp == int(file1[j].split("-")[0].split()[-1]):
			no=file1[j].split()[0].strip()
			output1.write(str(n)+"\t"+file1[j].lstrip(no).strip()+"\n")
			n=n+1