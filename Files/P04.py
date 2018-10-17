"""
Write a Python program to read last n lines of a file
"""

#import sys
#import os

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'
n=3

def file_read_from_tail(fname,lines):
        bufsize = 8192
        #fsize = os.stat(fname).st_size
        iters = 0
        fdata=open(fname,'r')
        fsize=fdata.seek(0,2)
        print("Fiel Size: %i"%fsize)
        print("current position: %i"%fdata.tell())
        if bufsize > fsize:
            bufsize = fsize-1
            data = []
            while True:
                iters +=1
                fdata.seek(fsize-bufsize*iters) 
                print("current position: %i"%fdata.tell())
                data.extend(fdata.readlines())
                print(data)
                print(len(data))
                if len(data) >= lines or fdata.tell() == 0:
                    print(''.join(data[-lines:]))
                    fdata.close()
                    break
                
file_read_from_tail(filePath,n)

