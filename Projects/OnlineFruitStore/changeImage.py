#!/usr/bin/env python3

from PIL import Image,UnidentifiedImageError
import os,sys


def processImages(image_path,image_name):
    image_size= (600,400)
    infile = image_path
    dest = os.path.expanduser("~/supplier-data/images")
    file_name,_ = os.path.splitext(image_name)
    try:
        with Image.open(infile) as img:
            img = img.resize(image_size)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            image_output = os.path.join(dest,file_name + ".jpeg")
            img.save(image_output,"jpeg")
    except UnidentifiedImageError:
        pass
    except OSError as err:
        print("cannot convert {} \n Error is {}".format(infile,type(err)))

def main():
    src = os.path.expanduser("~/supplier-data/images")
    try:
        for _,_,file_names in os.walk(src):
            for file_name in file_names:
                image_path = os.path.join(src,file_name)
                processImages(image_path,file_name)
    except Exception as err:
        print("Error is {}".format(err))

if __name__ == "__main__":
    main()