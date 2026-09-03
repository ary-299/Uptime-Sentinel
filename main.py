import yaml
import colorama
import msvcrt
from ping import server_ping        #imports the server_ping function from the ping.py file
import os
import threading
import time

print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "Welcome to the Uptime Sentinel!" \
+ colorama.Style.RESET_ALL + colorama.Fore.CYAN +"Press any Key to continue." + colorama.Style.RESET_ALL)
msvcrt.getch()
os.system('cls' if os.name == 'nt' else 'clear')

print(colorama.Fore.LIGHTMAGENTA_EX + colorama.Style.BRIGHT +r"""   __  __      __  _                   
  / / / ____  / /_(_____ ___  ___      
 / / / / __ \/ __/ / __ `__ \/ _ \     
/ /_/ / /_/ / /_/ / / / / / /  __/     
\____/ .___/\__/_/_/ /_/ /_/\___/      
   _____            __  _            __
  / ___/___  ____  / /_(_____  ___  / /
  \__ \/ _ \/ __ \/ __/ / __ \/ _ \/ / 
 ___/ /  __/ / / / /_/ / / / /  __/ /  
/____/\___/_/ /_/\__/_/_/ /_/\___/_/   """ + colorama.Style.RESET_ALL)
print("\n\n")

server_ping()
