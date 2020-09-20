#Coded by:fbitactical on Instagram.
#A-Python-Email-Validation-Check-Tool

import requests

print()
print("▄▄▄█████▓ ▄▄▄       ▄████▄  ▄▄▄█████▓ ██▓ ▄████▄   ▄▄▄       ██▓ ")   
print("▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▒██▀ ▀█  ▒████▄    ▓██▒ ")   
print("▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒▒▓█    ▄ ▒██  ▀█▄  ▒██░ ")   
print("░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░   ") 
print("  ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░██░▒ ▓███▀ ░ ▓█   ▓██▒░██████▒ ")
print("  ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▓  ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░ ")
print("    ░      ▒   ▒▒ ░  ░  ▒       ░     ▒ ░  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░ ")
print("  ░        ░   ▒   ░          ░       ▒ ░░          ░   ▒     ░ ░    ")
print("               ░  ░░ ░                ░  ░ ░            ░  ░    ░  ░ ")
print("                   ░                     ░                           ")
print()

email_address = input("Enter a email-address: ")
response = requests.get("https://api.2ip.me/email.txt?email=" + email_address)

print(response.json())
