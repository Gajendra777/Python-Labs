#!/usr/bin/env python3

import subprocess
from multiprocessing import Pool
import os

def run(dirlist):
    dest = os.path.expanduser("~/data/prod_backup/")
    print("Copying file from {} to {}".format(dirlist,dest))
    subprocess.call(["rsync","-arq", dirlist, dest])

if __name__== "__main__":
    try:
        dirlist = []
        number_of_dir = 0
        src = os.path.expanduser("~/data/prod/")
        for _,dirs,_ in os.walk(src):
            number_of_dir = len(dirs)
            for _dir in dirs:
                dir_path = os.path.join(src,_dir)
                dirlist.append(dir_path)
            break
        p = Pool(number_of_dir)
        p.map(run,dirlist)        
    except Exception as err:
        print("Error is {}".format(err))
    finally:
        p.close()