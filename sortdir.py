#! /usr/bin/python
# -*- coding: utf-8 -*-


import os
import shutil
import time

# The Path of the directory to be sorted

path = 'path/to/directory/you/want/sorted'


# This populates a list with the filenames in the directory

list_ = os.listdir(path)
print(time.strftime('%a - %H:%M:%S - %Y'))

# Traverses every file
for file_ in list_:
    name, ext = os.path.splitext(file_)
    # Stores the extension type
    ext = ext[1:]
    # If it is directory, it forces the next iteration
    if ext == '':
        continue
    # It moves the file to that directory
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
        # If the directory does not exist, it creates a new directory
    else:
        os.makedirs(path+'/'+ext)
shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)

