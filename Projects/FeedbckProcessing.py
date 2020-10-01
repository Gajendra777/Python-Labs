#!/usr/bin/env python3

import os
import csv
import requests

src = os.path.abspath("/data/feedback/")

def UploadTOWebsite(feedback_dict):
    param = feedback_dict
    try:
        response = requests.post("http://34.121.196.7/feedback/", json=param)
        if not response.ok:
            raise Exception("GET failed with status code {}".format(response.status_code))
    except Exception as err:
        print(err)

def ConvertTextToDictionary(filename):
    feedback_dict = {}
    seq = ("title","name","date","feedback")    
    feedback_dict = dict.fromkeys(seq)
    try:
        with open(filename,mode='r') as file:
            lines = file.readlines()
            feedback_dict["title"] = lines[0].strip()
            feedback_dict["name"] = lines[1].strip()
            feedback_dict["date"] = lines[2].strip()
            feedback_dict["feedback"] = lines[3].strip()
    except FileNotFoundError as err:
        print("File : {}  not found\n".format(filename))
    except Exception as err:
        print("Unable to Open and Read File :{} \n Error is : {}".format(filename,type(err)))
    
    UploadTOWebsite(feedback_dict)

def ProcessFiles():
    filespath = os.listdir(src)
    for files in filespath:
        ConvertTextToDictionary(os.path.join(src,files))

if __name__=="__main__":
    ProcessFiles()