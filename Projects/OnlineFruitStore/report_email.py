#!/usr/bin/env python3

import os
from  datetime import date
import  reports
import emails


def processData():
    
    src = os.path.expanduser("~/supplier-data/descriptions")
    filespath = os.listdir(src)
    summary_paragraph = []
    for filename in filespath:
        if filename.endswith("txt"):
            index = int(filename.strip(".txt"))
            filepath = os.path.join(src,filename)
            try:
                with open(filepath,mode='r') as file:
                    lines = file.readlines()
                    summary_paragraph.insert(index-1,[lines[0].strip(),lines[1].strip()])  
            except FileNotFoundError as err:
                print("File : {}  not found\n".format(filename))
            except Exception as err:
                print("Unable to Open and Read File :{} \n Error is : {}".format(filename,type(err)))

    return summary_paragraph

def main():
    summary_paragraph = processData()
    
    #! Generate PDF File
    report_name  = "processed.pdf"
    report_title = "Processed Update on {}".format(date.today().strftime("%B %d, %Y"))
    report_body  = ""


    for item in summary_paragraph:
        report_body += "name: " + item[0].strip() + "<br/>"  + "weight: " + item[1].strip() + "<br/><br/>" 

    reports.generate_report(report_name,report_title,report_body)

    #! send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    
    message = emails.generate_email(sender, receiver, subject, body, "processed.pdf")
    emails.send_email(message)

if __name__=="__main__":
    main()