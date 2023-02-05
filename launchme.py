import importings
import time
import os
import sys
import requests
import json
import random
import string
import time
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
print("Skipping update search")
print("Manual update may be required.")
print("----------------------------------------")
print("made by yazide uwu uwu uwu uwu uwu uwu uwu uwu uwu uwu uwu uwu uwu")
print("----------------------------------------")
print("launching in 2 secs")
if os.path.exists("config.owo"):
    os.remove("config.owo")
print("Configuration needed to launch.")
print("Please wait")
time.sleep(2)
clear()
print("Proceeding to configuratinon.")
print("Please input correctly.")
print("----------------------------------------")
website = input("Website to connect ->")
print("----------------------------------------")
name = input("Your name ->")
print("----------------------------------------")
ti = input("Time to connect (in secs) ->")
print("----------------------------------------")
print("Generating your configuration file.")
print("Connecting to Y-S Network to generate UUID.")
net = requests.get("https://y-s.es/")
if net.status_code == 200:
    print("Connection succeeded.")
else:
    print("Connection failed.")
    sys.exit(1)
print("----------------------------------------")
uwu = open("config.owo", "x")
uwu.write("SAJDHQ!9")
uwu.close()
print("------- Configuration completed -------")
print("----------------------------------------")
input("Press any key to continue...")
print("----------------------------------------")
print("Launching")
print("Connecting to "+ website)
print(name+" we are downloading the entire website so we know when it changes.")
response = requests.get(website).text
def check():
    return(requests.get(website).text)

if os.path.exists("web.owo"):
    os.remove("web.owo")
uwu = open("web.owo", "x")
uwu.write(response)
uwu.close()
print("----------------------------------------")
print("We have succesfully downloaded the website.")
print("----------------------------------------")
print("Waiting "+ ti + " secs")

clear()
uwu = True
rsn = "error"
cntn = ""
print(ti)
ti = int(ti)
times = "0"
while uwu:
    times = int(times)
    times = times + 1
    times = str(times)
    clear()
    print("Status: Getting files")
    print("Checked "+ times +" times.")
    xd = open("web.owo", "r")
    cntn = xd.read()
    clear()
    print("Status: Reading files")
    print("Checked "+ times +" times.")
    print("Content of the file has been compiled.")
    xd.close()
    clear()
    print("Status: Downloading website")
    print("Checked "+ times +" times.")
    print("Content of the website has been downloaded.")
    xd = check()

    clear()
    print("Status: Comparing websites")
    print("Checked "+ times +" times.")
    print("Content of the website is being compared with the file one")

    if xd != cntn:
        uwu = False
        rsn = "AE!"
        clear()
        print("!!!!!!!!!!!!!!")
        break
    clear()
    print("Status: Waiting time.")
    print("Checked "+ times +" times.")
    time.sleep(ti)
    clear()
    print("Status: Starting again.")

print("WEBSITE CODE HAS CHANGED!")
    
    