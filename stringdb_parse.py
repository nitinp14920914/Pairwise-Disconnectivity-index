import sys
foin =open(sys.argv[1] , 'r')
fout = open(sys.argv[2],'w')
lines = foin.readlines()[1:]
for line in lines:
	word = line.split()
	fout.write(str(word[0])+'\t'+str(word[1])+'\t'+str(word[-1])+'\n')
