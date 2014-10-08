#!/bin/python3
import os,hashlib,io,base64,pickle

from os.path import join, getsize

hash_database=[]


for root, dirs, files in os.walk('/etc', followlinks=False):
    print(root)
    for file_name in files:
        try:
            f=open(root+"/"+file_name,"rb")
        except:
            pass
        myline=f.read()
        #print(myline)
        #base64.b64encode(myline)
        myhash=hashlib.sha224(myline).hexdigest()
        print("\t"+file_name+"\t\t"+myhash)
        hash_database.append([root+"/"+file_name,myhash])
        #print(hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest())


#print(hash_database[:])

for item in hash_database:
    print(item)

hash_dumped=open("hash_dumped","w+")
pickle.dump(hash_database,hash_dumped)
hash_dumped.close()
