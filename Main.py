import requests
from os import system, name
from subprocess import run
import threading
from time import sleep
from colorama import init
from termcolor import colored
import random
init()

def asciart():
    print()
    print()
    print(colored("████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗         ██████╗ ██╗     ","cyan"))
    print(colored("╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║         ██╔══██╗██║     ","cyan"))
    print(colored("   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║         ██║  ██║██║     ","cyan"))
    print(colored("   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║         ██║  ██║██║     ","cyan"))
    print(colored("   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗    ██████╔╝███████╗","cyan"))
    print(colored("   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝","cyan"))
    print()
    print()
asciart()

colors = ["red","yellow","blue","cyan","magenta"]

dl = False

if name == "posix":
    sys = True
else:
    sys = False

def clear():
  
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    run(["notify-send",f"[INFO]: File {local_filename}, Downloaded Completely."])
    print(f"[INFO]: File {local_filename}, Downloaded Completely.")
    global dl
    dl = True
    return local_filename

url = input("Enter Link: ")
if sys:
    run(["notify-send","[INFO]: Download Started."])
print("[INFO]: Download Started.")

t = threading.Thread(target=download_file, args=(url,))
t.start()
while dl == False:
    color = random.choice(colors)
    asciart()
    print(colored("Downloading...",color))
    sleep(0.3)
    clear()
    
    color = random.choice(colors)
    asciart()
    print(colored("dOwnloading...",color))
    sleep(0.3)
    clear()
    
    color = random.choice(colors)
    asciart()
    print(colored("doWnloading...",color))
    sleep(0.3)
    clear()
    
    color = random.choice(colors)
    asciart()
    print(colored("dowNloading...",color))
    sleep(0.3)
    clear()
    
    color = random.choice(colors)
    asciart()
    print(colored("downLoading...",color))
    sleep(0.3)
    clear()
    
    color = random.choice(colors)
    asciart()
    print(colored("downlOading...",color))
    sleep(0.3)
    clear()
    
    color = random.choice(colors)
    asciart()
    print(colored("downloAding...",color))
    sleep(0.3)
    clear()
    
    color = random.choice(colors)
    asciart()
    print(colored("downloaDing...",color))
    sleep(0.3)
    clear()
    
    color = random.choice(colors)
    asciart()
    print(colored("downloadIng...",color))
    sleep(0.3)
    clear()
    
    color = random.choice(colors)
    asciart()
    print(colored("downloadiNg...",color))
    sleep(0.3)
    clear()
    
    color = random.choice(colors)
    asciart()
    print(colored("downloadinG...",color))
    sleep(0.3)
    clear()