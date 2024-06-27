years=[1994,1995,1996,1997,1998,1999,2000,2001]

with open ('Datasets/cit-HepPh-dates.txt','r') as f:
    alllines=f.readlines()

count=0
nodes=[]
for line in alllines:
    if(count==0):
        count+=1
        continue
    else:
        linespl=line.strip().split()
        date=linespl[1].split('-')
        if(int(date[0]) in years):
            if(linespl[0][0:2]!='11'):
                nodes.append(int(linespl[0]))
            else:
                nodes.append(int(linespl[0][2:]))

with open ('Datasets/cit-HepPh.txt','r') as f:
    lines=f.readlines()
    
count=0
edges=[]
for line in lines:
    if(count<4):
        count+=1
        continue
    else:
        linespl=line.strip().split()
        if(int(linespl[0]) in nodes):
            edges.append((int(linespl[0]),int(linespl[1])))

with open('Datasets/%dto%d.txt'%(years[0],years[-1]),'w') as f:
    for i in range(0,4):
        f.write('\n')
    for edge in edges:
        f.write('%d\t%d\n'%(edge[0],edge[1]))
