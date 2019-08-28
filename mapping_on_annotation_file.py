import sys
file1 = open(sys.argv[1],'r')
file2 = open(sys.argv[2],'r')
result1= open('Result_crucialnodes.txt','w')
result2= open('Result_noncrucialnodes.txt','w')
result3 =open('Result_moderatenodes.txt','w')

for line1 in file1:
    word1 = line1.split()
    file2.seek(0)
    for line2 in file2:
        word2 = line2.split()
        if word2[1] == word1[1]:
            if word1[0] == '1.0':
                result1.write(word1[0]+'\t'+word1[1]+'\t'+word2[1]+'\t'+word2[5]+'\t'+word2[-1]+'\n')
            if word1[0] == '0.0':
                result2.write(word1[0]+'\t'+word1[1]+'\t'+word2[1]+'\t'+word2[5]+'\t'+word2[-1]+'\n')
            if word1[0] > '0.0' and word1[0] < '1.0' :
                result3.write(word1[0]+'\t'+word1[1]+'\t'+word2[1]+'\t'+word2[5]+'\t'+word2[-1]+'\n')

                
