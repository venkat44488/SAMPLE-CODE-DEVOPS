
root@netflow-nfs-2:/opt/netflow_scripts# cat check-ipdr-files.py
#!/usr/bin/python
from pprint import pprint
from datetime import datetime, timedelta
#import time
import os
import smtplib
import email.utils
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email import Encoders
from email.mime.base import MIMEBase


def sendMail(email,files, a, b):
    msg = MIMEMultipart()
    msg['From'] = 'venkat@gmail.com'
    msg['To'] = ", ".join(email)
    msg['Subject'] = 'IPDR Netflow generated less files'


    message = "Dear Team,\n\n IPDR Netflow app  not generated all the files  in nfs server:\n\n\n\n"
    message = message+"{} \n{} \n{}".format(files,a, b)
    msg.attach(MIMEText(message+"\n\n\n\n\nThis is an automated mail!"))

    try:
        mailserver = smtplib.SMTP('10.70.13.10',2525)
        mailserver.sendmail('venkat@gmail.com', email, msg.as_string())
        print("after sendmail,, seeing less no of files")
        mailserver.quit()
        return "Mail Sent"
    except:
        return "Mail Server Issue"


email =  ['venkat@gmail.com','abc@gmail.com','xy@gmail.com']

a="Regards"
b="IPDR-Netflow"


print("===================",datetime.now(),"==================") # prints current date and time

expected_no_of_files=8

# date and time format in yyyymmddhhmm
prev_minute = datetime.now()-timedelta(minutes=1)
date_time=int(prev_minute.strftime("%Y%m%d%H%M"))
print(date_time)

# calculate actual no of files that are generated in /mnt/netflow path

os.chdir("/mnt/netflow")
cmd="ls -ltr | grep %s | wc -l" % date_time # captures no of actual files
cmd2="ls -ltr | grep %s" % date_time        # cmd2 holds the files
files=os.popen(cmd2).read()
actual_no_of_files=int(os.popen(cmd).read())
#print(files)

# condition to check actial and expected no of files generated
if actual_no_of_files >= expected_no_of_files :
    print("got enough files")
else:
    sendMail(email,files,a,b)
