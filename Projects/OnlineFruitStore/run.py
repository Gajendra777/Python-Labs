#!/usr/bin/env python3

import os
import csv
import requests


src = os.path.expanduser("~/supplier-data/descriptions")

def UploadTOWebsite(image_description):
    url = "http://104.154.135.173/fruits/"
    param = image_description
    try:
        response = requests.post(url, json=param)
        if not response.ok:
            raise Exception("GET failed with status code {}".format(response.status_code))
    except Exception as err:
        print(err)

def ConvertTextToDictionary(filename):
    image_description = {}
    seq = ("name","weight","description","image_name")    
    image_description = dict.fromkeys(seq)
    filepath = os.path.join(src,filename)
    try:
        with open(filepath,mode='r') as file:
            lines = file.readlines()
            image_description["name"] = lines[0].strip()
            weight = lines[1].strip().strip(" lbs")
            image_description["weight"] = int(weight)
            description = ""
            for line in lines[2:]:
                description += line.strip()
            image_description["description"] = description
            image_description["image_name"] = filename.replace("txt","jpeg")
    except FileNotFoundError as err:
        print("File : {}  not found\n".format(filename))
    except Exception as err:
        print("Unable to Open and Read File :{} \n Error is : {}".format(filename,type(err)))
    
    UploadTOWebsite(image_description)

def ProcessFiles():
    filespath = os.listdir(src)
    for files in filespath:
        if files.endswith("txt"):
            ConvertTextToDictionary(files)

if __name__=="__main__":
    ProcessFiles()