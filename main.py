import yaml
import colorama
import msvcrt
from ping import server_ping        #imports the server_ping function from the ping.py file
import os

print(colorama.Fore.LIGHTCYAN_EX, colorama.Style.BRIGHT, "Welcome to the Uptime Sentinel! Press any Key to continue...", end="", flush=True)
msvcrt.getch()
os.system('cls' if os.name == 'nt' else 'clear')


server_ping()