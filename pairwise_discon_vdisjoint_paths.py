import matplotlib.pyplot as plt
from igraph import *
import sys

print ('usage: inputfile output_filename')

n=[]
n_removed=[]

fout=open(sys.argv[2],'w')

g=Graph.Read_Ncol(sys.argv[1], names=True, weights="if_present")
print ('No. of nodes in given file ', len(g.vs))
vs=[]
for i in range(len(g.vs)):
        vs.append(i)

for i in range(len(vs)-1):
    start=vs[i]
    stop =vs[i+1]
    no=g.vertex_disjoint_paths(source=start, target=stop, checks=True, neighbors="ignore")
    n.append(no)

i = 0
deleted =[]
while i == 0:
    st=0
    sp=1
    deleted.append(((str(g.vs[1]).split())[-1])[1:-3])
    dlt=g.delete_vertices(st)
    if len(g.vs) == 1:
        break
    n1=g.vertex_disjoint_paths(source=st, target=sp, checks=True, neighbors="ignore")
    n_removed.append(n1)

pairwise = []
crucial=0
noncrucial=0
for i in range(len(n)-1):
    if n[i] > 0:
         index=(n[i]-n_removed[i])/float(n[i])
         fout.write(str(index)+'\t'+str( deleted[i])+'\n')
         #print index , deleted[i]
         pairwise.append(index)
         if index == 1:
            crucial +=1
         if index == 0:
            noncrucial +=1
print "crucial nodes" ,crucial
print "non crucial nodes " ,noncrucial 


