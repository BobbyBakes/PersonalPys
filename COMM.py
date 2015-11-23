#!/usr/bin/env python # COMM.py
import sys
import os
path=os.getcwd()
string='ans'
for root, dirs, files in os.walk(path):
    if string in dirs: break
    else:os.mkdir('ans')
print 'root',root
print 'dirs',dirs
print 'files',files
for root, dirs, files in os.walk(path):
    for name in files:
        if name[-2:]=='.m':
##            print name
            ifile=open(name,'r')
            ofile=open('ans/'+name,'w')
            newlines=[]
            for line in ifile:
                line0 = str.strip(line)
                if line0 !='':
                    if line0[0] != '%': #and line0[0] != '%' and line0[-1] != ';':
                        if '%' in line0:
                            newlines.append(line[:line.find("%")]+'\n')
                        else:
                            newlines.append(line)

##            ofile.write('#!/usr/bin/env python # '+name+'\n')
            ofile.writelines(newlines)
            ofile.close()
            ifile.close()
print 'root',root
##print 'dirs',dirs
##print 'files',files