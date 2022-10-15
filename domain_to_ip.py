#!/usr/bin/python3
import socket
import re
import turtle
import pyfiglet
from termcolor import colored
import turtle 
import urllib.request as u
print(colored('    *******************************Domain To IP******************************************','green'))
print(colored('*******************************CREATE BY AHSAN AHMED******************************************','red'))
banner = colored(pyfiglet.figlet_format('Domain To IP'),'green')
print(banner)
domain = turtle.textinput("Domain Name","your domain name") #domain



re_http = re.sub(r'https?://www.',' ',domain)
r = re_http.strip()

ip = socket.gethostbyname(r) # ip converted
print(colored(domain,'magenta',attrs=['reverse', 'blink']),':',colored(ip,'red'))



httpp = ''

if 'www.' in domain and 'http' not in domain:
   
    ht = re.sub(r'^www.',' ',domain)
   
    doi = ht.strip()
   
    httpp = re.sub(r'^[^https?://www.]','https://www.','a'+doi)

elif "https://www." not in domain and "http://www." not in domain:
      print(domain,'dd')
      httpp = re.sub(r'^[^https?://www.]','https://www.','a'+domain)
      
else:
    httpp = domain      



url_source = u.urlopen(httpp)
url_read = url_source.read()
print(url_read)


