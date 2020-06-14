# -*- coding: utf-8 -*-


print """  /$$$$$$$  /$$$$$$ /$$$$$$$  /$$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$$     /$$$$$$$  /$$     /$$
| $$__  $$|_  $$_/| $$__  $$| $$__  $$| $$__  $$| $$  | $$|__  $$__/| $$_____/    | $$__  $$|  $$   /$$/
| $$  \ $$  | $$  | $$  \ $$| $$  \ $$| $$  \ $$| $$  | $$   | $$   | $$          | $$  \ $$ \  $$ /$$/ 
| $$  | $$  | $$  | $$$$$$$/| $$$$$$$ | $$$$$$$/| $$  | $$   | $$   | $$$$$       | $$$$$$$/  \  $$$$/  
| $$  | $$  | $$  | $$__  $$| $$__  $$| $$__  $$| $$  | $$   | $$   | $$__/       | $$____/    \  $$/   
| $$  | $$  | $$  | $$  \ $$| $$  \ $$| $$  \ $$| $$  | $$   | $$   | $$          | $$          | $$    
| $$$$$$$/ /$$$$$$| $$  | $$| $$$$$$$/| $$  | $$|  $$$$$$/   | $$   | $$$$$$$$ /$$| $$          | $$    
|_______/ |______/|__/  |__/|_______/ |__/  |__/ \______/    |__/   |________/|__/|__/          |__/ 
"""               

import requests
import sys

try:
    site = sys.argv[1]
    wordlist = sys.argv[2]

except:
    print "Invalid arguments"
    print "Usage: dnsbrute.py http://site.com/ <wordlist>"
    sys.exit(1)



try:
    arquivo = open(wordlist)
    linhas = arquivo.read().splitlines()

except:
    print "File Not Found"
    sys.exit(1)



try:
    for linha in linhas:
        resposta = requests.get(site+linha)
        codigo = resposta.status_code
        if codigo != 404 and codigo != 403:
            print str("Found -->") + " " + site+linha, codigo

except Exception as erro:
    print str("Error") + erro



