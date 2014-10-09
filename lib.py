#!/bin/python3

import os,hashlib,io,base64,pickle,lib
from os.path import join, getsize


class FileList():
    hash_database=[]
    def compare(self,entry_b):
        pass 

    def show_list(self):
        for item in self.hash_database:
                print(item)
    
    def save_dump(self):
        hash_dumped=open("hash_dumped","wb+")
        pickle.dump(self.hash_database,hash_dumped)
        hash_dumped.close()
        print("Dumped Succesfully")

    def load_dump(self):
        hash_dumped=open("hash_dumped","rb")
        self.hash_database=pickle.load(hash_dumped)
        hash_dumped.close()
        print("Dumped Loaded Succesfully")

    def search_path(self,search_dir):
        for root, dirs, files in os.walk(search_dir, followlinks=False):
            print(root)
            for file_name in files:
                try:
                    f=open(root+"/"+file_name,"rb")
                    myline=f.read()
                    myhash=hashlib.sha224(myline).hexdigest()
                    self.hash_database.append([root+"/"+file_name,myhash,str(os.stat(root+"/"+file_name).st_size)])
                except:
                    pass

