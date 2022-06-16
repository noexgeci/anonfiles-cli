from colorama import *
import requests
import json
import time
import os

url = 'https://api.anonfiles.com/upload'

os.system('cls')

print('''
Drag & Drop the file here and press Enter to upload
''')

filename = input(f"{Fore.GREEN}? {Fore.RESET}File {Fore.GREEN}→ {Fore.LIGHTGREEN_EX}")

if filename == "":
    print(f'{Fore.RED}! {Fore.RESET}No file specified')
    os.system('pause >nul')
    os.system('exit')

files = {'file': (open(filename, 'rb'))}

print(f"{Fore.YELLOW}! {Fore.RESET}Uploading file, this may take some time...")
r = requests.post(url, files=files)
response = json.loads(r.text)

if response['status']:
    url0 = response['data']['file']['url']['short']
    print(f'{Fore.CYAN}! {Fore.RESET}File uploaded successfully {Fore.CYAN}→ {Fore.LIGHTCYAN_EX}{url0}')
    os.system(f'start {url0}')
    os.system('pause >nul')
else:
    message = resp['error']['message']
    errtype = resp['error']['type']
	print(f'{Fore.RED}! {Fore.RESET}Error {Fore.RED}→ {Fore.LIGHTRED_EX}{message} {Fore.RED}| {Fore.LIGHTRED_EX}{errtype}')
	os.system('pause >nul')
