#!/usr/bin/env python # myCommentfilter.py
import sys
import os
path=os.getcwd()
string='ans'
for root, dirs, files in os.walk(path):
    if string in dirs: break
    else:os.mkdir('ans')
ifile=open(sys.argv[1],'r')
ofile=open('ans/'+sys.argv[1],'w')
newlines=[]
for line in ifile:
    line0 = str.strip(line)
    if line0 !='':
        if line0[0] != '#': #and line0[0] != '%' and line0[-1] != ';':
            newlines.append(line)
ofile.write('#!/usr/bin/env python #'+sys.argv[1]+'\n')
ofile.writelines(newlines)
ofile.close()
ifile.close()