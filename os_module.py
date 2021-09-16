#program to find last modified files and big files

import os
import datetime as dt

os.chdir("C:\\Users\\fnuj\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\New folder")

inp=input("1: File modifed, 2:Big file, 3:Big Directory")
now = dt.datetime.now()
ago = now-dt.timedelta(minutes=300)
for root, dirs,files in os.walk('.'):
    dir_size=0
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        size = st.st_size
        if inp==1 and mtime > ago:
            print('%s modified %s'%(path, mtime))
        if inp==2 and size>524288:
            print('%s size is %s' %(path,size))
        dir_size=dir_size+size
        if inp==3 and dir_size>524288:
            print('%s Dir size is %s' %(path,dir_size1))

#to find the size of directory we haev to sum up the fixe size in above traversal
if inp == '3':
    for root, dirs,files in os.walk('.'):
        dsize=0
        for dname in dirs:
            path = os.path.join(root, dname)
            st = os.stat(path)
            dsize = dsize+st.st_size
            if dsize>1048576:
                print('%s Dir size is %s' %(path,size))
