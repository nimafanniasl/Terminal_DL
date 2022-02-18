import requests
from os import system, name
import os
import threading
from time import sleep
from colorama import init
from subprocess import run
from colorama import Fore
from termcolor import colored
import random
import re


class FileDownloader:
    total_size = None
    current_size = None
    filename = None

    init()

    def __init__(self):
        self.asciart()

        self.colors = ["red", "yellow", "blue", "cyan", "magenta"]

        self.dl = False

        if name == "posix":
            self.sys = True
        else:
            self.sys = False
        url = input("Enter Link: ")
        if self.sys:
            self.notify_send("[INFO]: Download Started.")
        print("[INFO]: Download Started.")

        t = threading.Thread(target=self.download_file, args=(url,))
        t.start()
        while self.dl is False:
            if self.total_size is not None and self.current_size is not None:
                color = random.choice(self.colors)
                self.asciart()
                print(f"Size: {self.getstandardsize(self.total_size)}")
                print(
                    colored(
                        f"Downloading... {self.persent(self.current_size/self.total_size)}% \
                         {self.getstandardsize(self.current_size)}",
                        color))
                sleep(0.2)
                self.clear()
            elif self.total_size is None and self.current_size is not None:
                color = random.choice(self.colors)
                self.asciart()
                print(colored(f"Size: Unknown :)", "magenta"))
                print(
                    colored(f"Downloading... {self.getstandardsize(self.current_size)}", color))
                sleep(0.2)
                self.clear()

        print(Fore.GREEN + "[INFO]:", Fore.YELLOW +
              f"File {self.filename},", Fore.CYAN + "Downloaded Completely.")

    @staticmethod
    def persent(num):
        num2 = num * 100
        num2 = round(num2)
        return num2

    @staticmethod
    def getstandardsize(size):
        itme = ['bytes', 'KB', 'MB', 'GB', 'TB']
        for x in itme:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0
        return size

    @staticmethod
    def notify_send(msg):
        run(["notify-send", str(msg)])

    @staticmethod
    def asciart():
        print()
        print()
        print(colored("████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗         ██████╗ ██╗     ", "cyan"))
        print(colored("╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║         ██╔══██╗██║     ", "cyan"))
        print(colored("   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║         ██║  ██║██║     ", "cyan"))
        print(colored("   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║         ██║  ██║██║     ", "cyan"))
        print(colored("   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗    ██████╔╝███████╗", "cyan"))
        print(colored("   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝", "cyan"))
        print()
        print()

    @staticmethod
    def clear():

        if name == 'nt':
            _ = system('cls')

        else:
            _ = system('clear')

    def download_file(self, url):
        with requests.get(url, stream=True) as r:
            if "Content-Disposition" in r.headers.keys():
                local_filename = re.findall(
                    "filename=(.+)", r.headers["Content-Disposition"])[0]
            else:
                local_filename = url.split("/")[-1]
            if "Content-Length" in r.headers:
                self.total_size = r.headers['Content-Length']
                self.total_size = int(self.total_size)
            else:
                self.total_size = None
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    self.current_size = os.path.getsize(local_filename)
                    f.write(chunk)
        self.notify_send(f"[INFO]: File {local_filename}, Downloaded Completely.")
        global dl
        self.dl = True
        self.filename = local_filename


if __name__ == "__main__":
    Terminal_DL = FileDownloader()
