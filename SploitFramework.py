import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random_word import RandomWords
import names
import string
import random
from random import choices
from string import ascii_lowercase
import requests
import pyautogui
import time
import os
from colorama import Fore, Back, Style
os.system('color 04')
wait=time.sleep
RF=Fore.RED
BF=Fore.BLUE
WF=Fore.WHITE
CF=Fore.CYAN
GF=Fore.GREEN
YF=Fore.YELLOW
GB=Back.GREEN
Cmd3="\n"*70
Intro=GF+'''Validate Lots of vulnerabilities to demonstrate exposure
with MetaSploit pro -- Learn more on http://rapid7.com/metasploit\n''' 
Intro0=RF+"  ╔═══════════════════════════════════════════════════════╗\n"
Intro3=RF+Cmd3+"  ╔═══════════════════════════════════════════════════════╗\n"
Intro2="  "+RF+"║"+WF+'''• ▌ ▄ ·. ▄▄▄ .▄▄▄▄▄ ▄▄▄· .▄▄ ·  ▄▄▄·▄▄▌        ▪  ▄▄▄▄▄'''+RF+"║\n"
Intro4="  "+RF+"║"+WF+'''·██ ▐███▪▀▄.▀·•██  ▐█ ▀█ ▐█ ▀. ▐█ ▄███•  ▪     ██ •██  '''+RF+"║\n"
Intro5="  "+RF+"║"+WF+'''▐█ ▌▐▌▐█·▐▀▀▪▄ ▐█.▪▄█▀▀█ ▄▀▀▀█▄ ██▀·██▪   ▄█▀▄ ▐█· ▐█.▪'''+RF+"║\n"
Intro6="  "+RF+"║"+WF+'''██ ██▌▐█▌▐█▄▄▌ ▐█▌·▐█ ▪▐▌▐█▄▪▐█▐█▪·•▐█▌▐▌▐█▌.▐▌▐█▌ ▐█▌·'''+RF+"║\n"
Intro7="  "+RF+"║"+WF+'''▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀  ▀  ▀  ▀▀▀▀ .▀   .▀▀▀  ▀█▄▀▪▀▀▀ ▀▀▀ '''+RF+"║\n"
Intro8=RF+"  ╚═══════════════════════════════════════════════════════╝\n"
Cmd=RF+"root@kali"
Cmd2=WF+":"+CF+"~"+WF+"# "
Info1=GF+"          =[  "+YF+"metasploit v4.14.22-dev                          "+GF+"]"
Info2=GF+'''
+ - -  - -=[  1658 exploits - 947 auxiliary - 293 post         ]
+ - -  - -=[  486 payloads - 40 encoders - 9 nops              ]
+ - -  - -=[  Free MetaSploit Pro trail: http://r-7.co/trymsp  ]\n\n'''
Info3=WF+"Aircrack-ng....."+GF+"OK!"+"\n"+WF+"Aireplay-ng....."+GF+"OK!"+"\n"
Info4=WF+"Airmon-ng......."+GF+"OK!"+"\n"+WF+"Airodump-ng....."+GF+"OK!"+"\n\n\n"
Sel1=WF+"{["+CF+"01"+WF+"]   "+CF+"Email Phishing"+WF+"      }\n"
Sel2=WF+"{["+CF+"02"+WF+"]   "+CF+"Spoofing"+WF+"            }"+YF+" C O M M I N G   S O O N . . .\n"
Sel3=WF+"{["+CF+"03"+WF+"]   "+CF+"Credential harvester"+WF+"}"+YF+" C O M M I N G   S O O N . . .\n"
Sel4=WF+"{["+CF+"04"+WF+"]   "+CF+"KeyLoggers"+WF+"          }"+YF+" C O M M I N G   S O O N . . .\n"
Sel5=WF+"{["+CF+"05"+WF+"]   "+CF+"TabNabbing"+WF+"          }"+YF+" C O M M I N G   S O O N . . .\n"
Sel6=WF+"{["+CF+"06"+WF+"]   "+CF+"WebJacking"+WF+"          }"+YF+" C O M M I N G   S O O N . . .\n"
Info5=GF+'''
To begin Email Phishing you must first download the '''+WF+"["+CF+" Selenium Module "+WF+"]\n"
Info6=GF+"To do that open Command Prompt and type "+CF+"pip install selenium "+GF+"Then download\n"
Info7=GF+"The ChromeWebdriver -> "+WF+"http://chromedriver.chromium.org/downloads\n"
Email1="\n\n"+WF+"Your Email "+CF+"- > "
Email2="\n\n"+WF+"Your Password "+CF+"- > "
Email3="\n\n"+WF+"Victems Email "+CF+"- > "
Email4="\n\n"+WF+"Local Ip "+CF+"- > "
SelFull=Sel1+Sel2+Sel3+Sel4+Sel5+Sel6
FullIntro=Intro0+Intro2+Intro4+Intro5+Intro6+Intro7+Intro8+"\n\n"+Intro+"\n"+Info1+Info2+"\n\n"+Info3+Info4
FullIntro2=SelFull
print(FullIntro+FullIntro2)
A=input(Cmd+Cmd2+GF)
def EmailFun():
	B=input(Email1)
	C=input(Email2)
	D=input(Email3)
	E=input(Email4)
	f=open("MetaSploitData.txt","w+")
	f.write("Gmail -> "+B+" Password -> "+C+"\n")
	f.close()
	wait(1)
	Drive=webdriver.Chrome()
	Drive.get('''https://accounts.google.com/ServiceLogin/identifier?service=mail&'''
		'''passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss='''
		'''1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession''')
	wait(1)
	EmailFind=Drive.find_element_by_name('identifier')
	EmailFind.send_keys(B)
	wait(0.5)
	Next=Drive.find_element_by_xpath("//span[@class='RveJvd snByac']")
	Next.click()
	wait(1)
	PassWordFind=Drive.find_element_by_name('password')
	PassWordFind.send_keys(C)
	wait(0.5)
	Next2=Drive.find_element_by_xpath("//span[@class='RveJvd snByac']")
	Next2.click()
	wait(10)
	EmailFind2=Drive.find_element_by_xpath("//svg[@class='pTh3n ydLZ9 f']")
	EmailFind2.click()
	wait(0.5)
	EmailFind3=Drive.find_element_by_xpath("//input[@class='tF gB Xp kG ea-Ga-ea]")
	EmailFind3.send_keys(Email3)
	wait(0.1)
	EmailFind4=Drive.find_element_by_xpath("//span[@class='Jv]")
	EmailFind4.click()
	wait(1)
	Send=Drive.find_element_by_xpath("//div[@id=':20d.f]")
	Send.send_keys("SomethingHere")
if A=="1" or A=="01":
	print(Info5+Info6+Info7)
	EmailFun();
else:
	exit();
