# NetScanner by SergiyGrimldi

This app can halp you monitor your wifi network.


## How it works

1. Scan your IP-Adress
2. Then get a list of: Ip, Mac, Host of all devices connected
3. Check if are connected some devices not trusted
4. Send you an email with unwanted devices connceted

## 1 - Scan cycle

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
