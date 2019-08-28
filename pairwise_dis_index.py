import matplotlib.pyplot as plt
from igraph import *
import sys

print ('usage: inputfile output_filename')

fout=open(sys.argv[2],'w')
g_s=Graph.Read_Ncol(sys.argv[1], names=True, weights="if_present" , directed=True)
print ('No. of nodes in given file ', len(g_s.vs))

pair=[]
crucial=0
noncrucial=0
counter =0
for i in range(len(g_s.vs)):
    counter +=1
    g = g_s.copy()
    a= len(g.es)
    dlt=g.delete_vertices(i)
    b= len(g.es)
    c= float(a-b)/float(a)
    pair.append(c)
    fout.write(str(c)+"\t"+str(counter)+'\n')
    if c == 1:
        crucial +=1
    if c == 0:
        noncrucial +=1
print "crucial nodes" ,crucial
print "non crucial nodes " ,noncrucial 


