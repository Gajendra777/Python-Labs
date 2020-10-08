#!/usr/bin/env python3

import  psutil
import  requests
import  socket
import  emails
import  os

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == "127.0.0.1":
        return True
    return False 

def check_cpu_percent():
    cpu_percent = psutil.cpu_percent()
    if cpu_percent > 80:
        return True
    return False

def check_available_memory():
    THRESHOLD = 500 * 1024 * 1024  # 500MB
    memory = psutil.virtual_memory()
    if memory.available < THRESHOLD: 
        return True
    return False

def check_free_disk_space():
    disk_space = psutil.disk_usage("/")
    if  (disk_space.free/disk_space.total) * 100 < 20 :
        return True
    return False

def send_email(error_msg):
    #! send  an email 
    sender = "automation@example.com"
    receiver = "student-02-a08368710453@example.com"
    subject = error_msg
    body = " Please check your system and resolve the issue as soon as possible."

    
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)

def System_Check():
    error_meg = ""

    try:
        if check_cpu_percent():
            send_email("Error - CPU usage is over 80%") 
        elif  check_free_disk_space():
            send_email("Error - Available disk space is less than 20%")
        elif check_available_memory():
            send_email("Error - Available memory is less than 500MB")
        elif not check_localhost():
            send_email("Error - localhost cannot be resolved to 127.0.0.1")
    except Exception as err:
        print("Error is {} \n {}",err,type(err))


def main():
    System_Check()

    

if __name__ == "__main__":
    main()