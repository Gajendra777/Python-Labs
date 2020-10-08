#!/usr/bin/env python3

import os
import csv
import requests

src = os.path.expanduser("~/supplier-data/images")

def UploadTOWebsite(image_path):
    url = "http://104.154.135.173/upload/"
    try:
        with open(image_path, 'rb') as opened:
            response = requests.post(url, files = {'file':opened})
            if not response.ok:
                raise Exception("GET failed with status code {}".format(response.status_code))
    except Exception as err:
        print(err)

def ProcessFiles():
    filespath = os.listdir(src)
    for files in filespath:
        if files.endswith("jpeg"):
            UploadTOWebsite(os.path.join(src,files))

if __name__=="__main__":
    ProcessFiles()