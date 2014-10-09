#!/bin/python3
import os,hashlib,io,base64,pickle,lib

from os.path import join, getsize


mn=lib.FileList()

mn.search_path('/bin')

mn.show_list()

mn.save_dump()

mn.load_dump()

mn.show_list()
