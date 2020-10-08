#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate_error_report(sender,recipient,subject,body):
    """ Creates an Email with an attachment"""
    
    #Basic Email Formatting
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    
    return message


def generate_email(sender,recipient,subject,body,attachment_path):
    """ Creates an Email with an attachment"""
    
    #Basic Email Formatting
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    #Process the Attachment and add it to Email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/',1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=attachment_filename)

    return message

def send_email(message):
    mail_Server = smtplib.SMTP('localhost')
    mail_Server.send_message(message)
    mail_Server.quit()