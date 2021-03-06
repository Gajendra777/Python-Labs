#!/usr/bin/env python3

from PIL import Image,UnidentifiedImageError
import os,sys

#For Windows
dest = os.path.abspath("C:\\Users\\HP\\Downloads\\opt\\icons")
#For Linux
# dest = os.path.expanduser("/opt/icons") 
def processImages(image_path,image_name):
    image_size= (128,128)
    infile = image_path
    file_name,_ = os.path.splitext(image_name)
    try:
        with Image.open(infile) as img:
            img = img.resize(image_size)
            img = img.rotate(270)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            image_output = os.path.join(dest,file_name)
            img.save(image_output,"jpeg")
    except UnidentifiedImageError:
        pass
    except OSError as err:
        print("cannot convert {} \n Error is {}".format(infile,type(err)))

def main():
    # For Windows
    src = os.path.abspath("C:\\Users\\HP\\Downloads\\images")
    #For Linux
    #src = os.path.expanduser("~/images")
    if not os.path.exists(dest):
        os.makedirs(dest)
    try:
        for _,_,file_names in os.walk(src):
            for file_name in file_names:
                image_path = os.path.join(src,file_name)
                processImages(image_path,file_name)
    except Exception as err:
        print("Error is {}".format(err))

if __name__ == "__main__":
    main()