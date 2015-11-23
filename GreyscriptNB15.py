#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kyu
#
# Created:     01/11/2012
# Copyright:   (c) Kyu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Combi Try!

import sys
import os
path=os.getcwd()

def makeit(allincd,l):
#combi='\"copy -b\"'+allmp3s+' '+path+'\\comb\\'+files[1][:-9]+'.mp3\"\"';
    combi='\"copy /b '+allincd+' \"CD '+str(l)+'.mp3\"';
    print combi
    os.system(combi);

if __name__ == '__main__':
##    cdname=[]
    j=0
    allincd=''
    # Get files to unzip
    for root, dirs, files in os.walk(path):
        cdname=[]
        for i in range(106,121):

##            j=j+1
            for fil in files:
                if 'Track '+str(i).zfill(3) in fil:
                   print '>>> founddddd = track ',i
                   if '.mp3' in fil:
                      cdname.append('\"'+fil+'\"')
            print cdname
            print 'all in cd = ',allincd,'\n'
            if len(cdname)==15:
               j=j+1
               allincd=' + '.join(cdname)
               makeit(allincd,j)
               cdname=[]


# New walk to get unziped mp3 files
##mp3files=[];
##for root, dirs, files in os.walk(path):
####    print files
##    for fil in files:
##        if fil[-4:]=='.mp3':
##           mp3files.append('\"'+fil+'\"')
##    allmp3s=''
####    for mp3f in mp3files:
##    allmp3s=' + '.join(mp3files)
##    print 'all mp3 cat = ',allmp3s,'\n'
##    #combi='\"copy -b\"'+allmp3s+' '+path+'\\comb\\'+files[1][:-9]+'.mp3\"\"';
##    combi='\"copy /b '+allmp3s+' '+'nice.mp3\"';
##    print combi
##    os.system(combi);
##
### Delete unziped and copied file
##    dell='\"del '+allmp3s+'\"'
##    os.system(dell)
##


# Garbage
##    ofile=open(files,'w')
##       ifile=open('a.mp3','r')
####            ofile=open('ans/'+name,'w')
##              newlines=[]
##              for line in ifile:
####                line0 = str.strip(line)
####                if line0 !='':
####                    if line0[0] != '%': #and line0[0] != '%' and line0[-1] != ';':
####                        if '%' in line0:
####                            newlines.append(line[:line.find("%")]+'\n')
####                        else:
##                            newlines.append(line)
##                            print line
##
