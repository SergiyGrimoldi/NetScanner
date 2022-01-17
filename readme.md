# NetScanner# NetScanner by SergiyGrimldi

This app can halp you monitor your wifi network.


## How it works

1. Scan your IP-Adress
2. Then get a list of: Ip, Mac, Host of all devices connected
3. Check if are connected some devices not trusted
4. Send you an email with unwanted devices connceted

## Some features

1. Scan one your network
2. Scan cycle your network
3. Ceck datas such as Destination email, sender email, pssw of sender email
4. Change datas
5. Show list of trustes devices
6. Add device to trusted list
7. Remove device from trusted list

## 1 - Scan once

Use this to scan once your network, it return a list of devices connceted and alert if are there some unwant devices.
Automatically ends

## 2 - Scan cycle

Use this function to start a cycle of scans that allert you if are there some intrusions

## 3 - Ceck datas

Use this function to read your personal informations.
These informations are setted the first time you start the program and are:
- Destination mail 
- Sender mail (suggested: Gmail)
- Password of sender (not personal but device-password)

## 4 - Settings

Use this function to modify your personal informations.
These informations are:
- Destination mail 
- Sender mail (suggested: Gmail)
- Password of sender (not personal but device-password)

## 5 - List trusted devices
Use this function to read your trusted devices, usually those always connected to your netwok

## 6 - Add to List of trusted devices
Use this function to update your trusted devices with new one.

**_Attention: This add an exception and the program will not send email if this device will connected_**

## 7 - Remove from List of trusted devices
Use this function to update your trusted devices removing one.

**_Attention: This remove an exception and the program will send email if this device will connected_**

# **How to use**

1. Install all packages from requiremets.txt
2. Run python project with:
        
     **sudo python3 _direcotry/of/program/main.py_**

3. Insert system password
4. Enjoy
