#!/bin/python3
import os,hashlib,io,base64,pickle

from os.path import join, getsize

hash_database=[]


class fileobjects():
    pass

for root, dirs, files in os.walk('/etc', followlinks=False):
    print(root)
    for file_name in files:
        try:
            f=open(root+"/"+file_name,"rb")
            myline=f.read()
            myhash=hashlib.sha224(myline).hexdigest()
            print("\t"+file_name+"\t\t"+myhash+"\t"+str(os.stat(root+"/"+file_name).st_size))
            hash_database.append([root+"/"+file_name,myhash])
        except:
            pass


#print(hash_database[:])

for item in hash_database:
    print(item)

hash_dumped=open("hash_dumped","wb+")
pickle.dump(hash_database,hash_dumped)
hash_dumped.close()
