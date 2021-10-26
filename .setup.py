#!/bin/env python3
# Botol Baba Fuck Your Tut Tut Tut

"""

you can re run setup.py 
if you have added some wrong value

"""
import os, sys,time
import configparser

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)
		
		
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
bl="\033[1;94m"
ya="\033[1;93m"

logo='''
\033[1;92m   ______     ______) _____) 
\033[1;93m  (, /    )  (, /   /        
\033[1;91m    /---(      /   /   ___   
\033[1;94m ) / ____)  ) /   /     / )  
\033[1;96m(_/ (      (_/   (____ /     
\033[3;90m \n      TELEGRAM AUTO MEMBER ADDER\033[0;37;40m
\033[1;94m──────────────────────────────────────────────────
\033[1;92m▸ \033[1;95mAUTHOR     : MEHEDI HASAN ARIYAN
\033[1;92m▸ \033[1;95mFACEBOOK   : FACEBOOK.COM/THEMEHTAN
\033[1;92m▸ \033[1;95mYOUTUBE    : YOUTUBE.COM/MASTERTRICK1
\033[1;92m▸ \033[1;95mGITLAB     : GITLAB.COM/BOTOLBABA
\033[1;94m──────────────────────────────────────────────────'''
def banner():
	os.system('clear')
	print(logo)
	
banner()
print(gr+"\n\n\n[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch .config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"\n\n[+] YOUR API ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"\n[+] YOUR HASH ID : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"\n[+] YOUR NUMBER : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('.config.data', 'w')
cpass.write(setup)
setup.close()
jalan(ya+"\n\n[+] Setup Complete By BotolBaba!")
print(bl+"\n[+] Now You Can Run This Tool !")
jalan(gr+"\n[+] If You Dont Know How To Run This Tool Then Watch This Video. Video Tutorial : https://bit.do/BabaBTG\n\n\n")
input('\n\033[1;96mPRESS ENTER TO GO BACK')
os.system("python2 .btg.py")
