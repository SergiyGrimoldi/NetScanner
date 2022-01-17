
 # requests
from cmath import exp
from traceback import print_tb
from typing import MappingView
import requests

 # socket
import socket

 # scapy
from scapy.all import *

 # os
import os

 # getac
from getmac import get_mac_address as gma

 # time
import time
from datetime import datetime


 # smrplib --Mals
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

 # json
import json

 # csv
import csv

 # vendor
from mac_vendor_lookup import MacLookup

 # vlc
import vlc

config = []
old = []
MACS = []


def clear():

    try:
        os.system("cls" if os.name=="nt"else "clear")
    except:
        os.system("cls")
    finally:
        None


    

 # scan for MAC, IP, HOST

def exit_program():
    
    try:
        os.system("cls" if os.name=="nt"else "clear")
        exit()
    
    except:
        exit()
    
    finally:
        exit()
  
def scan():

    alert = "None"

    receiver = "grimo.sergiy@icloud.com"
    pssw = "byseqyguujsyfjuu"
    sender = "grimo.sergiy@gmail.com"

    h_name = socket.gethostname()
    IP_addres = socket.gethostbyname(h_name)
    partitioned_string = str(h_name).partition('.')
        
    h_name = str(partitioned_string[0])
   
    target_ip = "192.168.1.1/24"

    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]
    
    clients = []

    count_connected = 0

    for sent, received in result:
        
        # for each response, append ip and mac address to `clients` list
        clients.append({'ip': received.psrc, 'mac': received.hwsrc, 'host': socket.getfqdn(received.psrc)})
        count_connected +=1

    count = 0

    knowns = []
    known_mac = []
    reference = []
    check = []

    count = 0
    
    with open('/Users/sergiy/Documents/ProgettiGitHub/NetScanner/automated/known_mac.json') as json_file:
        data = json.load(json_file)
        known_mac.append(data.values())
        
    for items in known_mac:
        for item in items:
           
            reference.append(item)
    
    for host in clients:
        
        check.append(host['mac'])

    check.sort()
    reference.sort()

    for item in check:
        
        if item in reference:
            knowns.append(item)
        
        else:
            print("Not found in  Trusted List")

    count=0

    item = ""
    exception_list = []
    
    for host in clients:
            
        if host['mac'] in knowns: 

            alert = "None"
            count+=1
            #print(host['mac'])

            partitioned_string = str(host['host']).partition('.') 
            name = str(partitioned_string[0])
        
            
        else:
            count+=1
            
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
       
            try:
                
                print(f"INTRUSION DETECTED at: {current_time}\n\n - IP: {(host['ip'])}\n - MAC: {(host['mac'])}\n - HOST NAME: {(host['host'])}\n - VENDOR: {vendor}\n - STATUS: UNKNOWN - Connected")
            except:
                
                print(f"INTRUSION DETECTED at: {current_time}\n\n - IP: {(host['ip'])}\n - MAC: {(host['mac'])}\n - HOST NAME: {(host['host'])}\n - VENDOR: UNKNOWN\n - STATUS: UNKNOWN - Connected")

            print()
            alert = "Intrusion"

            try:
                vendor = MacLookup().lookup(host['mac'])
            except:
                vendor = "UNKNOWN"

            exceptions = f"""<br><br>
                    - IP: {host['ip']}<br>
                    - MAC: {host['mac']}<br>
                    - HOST: {host['host']}<br>
                    - VENDOR: {vendor}<br>"""

            datas = [f"{host['ip']} ",f"{host['mac']} ", f"{host['host']} ", f"{vendor} "]
            exception_list.append(datas)
            
    known_to_check = []
    scan_to_check = []
    
    for known in known_mac:
        for item in known:
            known_to_check.append(item)
        
        for host in clients:
            scan_to_check.append(host['mac'])  

    known_to_check.sort()
    scan_to_check.sort()   
   
    exception = str(exception_list).replace('\\n','').replace("'",'').replace('[','').replace(']','').replace(",","")
    
    if len(exception_list)>=1:
        
        
        alert = "Intrusion"

        try:
            sender_email = ""
            receiver_email = ""
            password = ""

            message = MIMEMultipart("alternative")
            message["Subject"] = f"INTRUSION DETECTED at: {current_time}"
            message["From"] = sender_email
            message["To"] = receiver_email

            text = """\
            INTRUSION DETECTED
            """
            html = f"""\
            <html>
            <body>
                <p>Hi, device not reconized<br>
                {exception}
                </p>
            </body>
            </html>
            """

            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")

            message.attach(part1)
            message.attach(part2)

            context = ssl.create_default_context()
            
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )
                
        except Exception as e:
            print("Email not sent\n", e)
        
        try:
            header = ['IP', 'MAC', 'HOST', 'VENDOR']
            for item in exception_list:
                
                data = item


                with open('/users/sergiy/log.csv', 'a', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)

                    # write the data
                    writer.writerow(data)
                print(f"Log file updated with: {data}")
                f.close()

        except Exception as e:
            print("Log file not created:\n", e)
    
    
    list_mac= []
    
    for item in known_to_check:
        if item not in scan_to_check:
            
            mac = item
            list_mac.append(mac)
           
            count+=1            
    
    if alert == "Intrusion":
       
        try:
            p = vlc.MediaPlayer("alarm.mp3")
            p.play()
            time.sleep(1)
            p.stop()
            print("Email sent, waiting for 30sec.")
            
            def countdown(time_sec):
                while time_sec:
                    mins, secs = divmod(time_sec, 60)
                    timeformat = '{:02d}:{:02d}'.format(mins, secs)
                    print(timeformat, end='\r')
                    time.sleep(1)
                    time_sec -= 1

            countdown(30)
            clear()
        except Exception as e:
            print(e)
 
    else:
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
       
        print(f"SCAN DONE at: {current_time}")
        
        

    if len(list_mac)>0: 
        
        for item in list_mac:
            print(f"{item} is not connected")
    print()      

 # cycle scan

def cycle():
        
    while True:
        clear()

        title = ("NetScanner - By Sergiy Grimoldi")
        print(title)
        print("\nScan...")
        scan()
        print("Waiting for next scan...")
        
        def countdown(time_sec):
            while time_sec:
                mins, secs = divmod(time_sec, 60)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                print(timeformat, end='\r')
                time.sleep(1)
                time_sec -= 1
            clear()
    
        countdown(10)

        
 # first config if not done

def configuration():
    
    clear()

    print("First configuration")
    print("Enter sender email:")
    sender = input("\n --> ")
    
    clear()
    
    print("First configuration")
    print(f"Sender: {sender}")
    print("[yellow]Enter password email (is not your own pssw but passwords for apps):")
    pssw = input("\n --> ")
    
    clear()
    
    print("First configuration")
    print((f"Sender: {sender}\nPssw: {pssw}"))
    print(("Enter receiver account (He will revicive all alert emails):"))
    receiver = input("\n --> ")
    
    clear()
    
    print("First configuration")
    print(f" - Sender: {sender}\n - Pssw: {pssw}\n - Receiver: {receiver}")
    print("Press Y to confirm or N to redo or X to exit_program:")
    confirm = input("\n --> ")
    
    if confirm =="y" or confirm == "Y":
        if sender != " " and pssw != " " and receiver != " " :
            with open("config.txt", "w+") as c:
            
                c.write(f"{sender}\n")
                c.write(f"{pssw}\n")
                c.write(f"{receiver}")
            
            clear()
            
            
            start = {"1":f"{gma()}"}
            jsonString = json.dumps(start)
            jsonFile = open("/Users/sergiy/Documents/ProgettiGitHub/NetScanner/automated/known_mac.json", "w+")
            jsonFile.write(jsonString)
            jsonFile.close()

        menu()
    
    elif confirm =="n" or confirm == "N":
        configuration()
    
    elif confirm =="x" or confirm == "X":
        exit_program()
    
    else:
        configuration()

 # read credentials


def menu():
    
    cycle()
    
 # initialize

if __name__ == "__main__":
    
    try:
    
        menu()
    
    except Exception as e:
        print(e)
    
