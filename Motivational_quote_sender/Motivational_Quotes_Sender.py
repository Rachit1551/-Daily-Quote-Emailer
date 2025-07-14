import os 
os.system('cls')

import smtplib as s
from email.message import EmailMessage
import datetime as d
import random


def file_handling():
    with open("E\\quotes.txt","r") as file:
        lines = file.readlines()




    random.shuffle(lines)                                           
    random_quote=random.choice(lines).strip(    )
    print("1")  
    return random_quote                       




def email(random_quote):
    print("3")
    
    my_email="senderEmail@gmail.com"                      
    password="Your generated App password"
    recipients = [
        "Receiver1@gmail.com",
        "Receiver2@gmail.com",
        "Receiver3@gmail.com"
    ]
    msg=EmailMessage()
    msg["Subject"]="Quote Of the Day !!!!!"
    msg["Sender"]=my_email
    msg["To"]=",".join(recipients)
    msg.set_content(random_quote)

    with s.SMTP("smtp.gmail.com",587) as con:
        con.starttls()
        con.login(my_email,password)
        con.send_message(msg)



def Time():
    now=d.datetime.now()
    week=now.weekday()
    print("2")
    lines=file_handling()
    email(lines)
        

Time()