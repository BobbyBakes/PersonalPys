import sys
##import string
# Get the subtitle input file!
fil=sys.argv[1]
ifile=open(fil,'r')
lin=[]
a=range(10)
for line in ifile:
    if (line[0]) not in str(a):
##        line0 = line.strip('.')
        line = line.strip().strip('.')
        if line != '':# and line!='\n':
##            line = line.strip().strip('.')
##            if line[0].isupper: line='.'+line
            line.replace('?','?\n')
            line.replace('."','."\n')
            lin.append(line+' ')
##lin=' '.join(lin)
##maxlen = 40
##newlin=[]
##for line in lin:
##    if line[-1] == '\n': line = line[:-1]
##    toolong = len(line) > maxlen
##    while toolong:
##        pos = str.rfind(line, ' ', 0, maxlen+1)
##        if pos == -1:
##            pos = str.find(line, ' ')
##        if pos == -1:
##            toolong = False
##        else:
##            print line[0:pos]
##            line = line[pos+1:]
##            toolong = len(line) > maxlen
##    newlin.append(line)
# write the lines as the output
ofile=open(fil.split('.')[0]+'-hacked.'+fil.split('.')[1],'w')
ofile.writelines(lin)
ofile.close()