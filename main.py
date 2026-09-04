import yaml
import colorama
import msvcrt
from ping import server_ping        #imports the server_ping function from the ping.py file
import os
import threading
import time
from rich.console import Console
import readchar

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')
print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "Welcome to the Uptime Sentinel!" \
+ colorama.Style.RESET_ALL + colorama.Fore.CYAN +"\n Press any Key to continue to the main menu!" + colorama.Style.RESET_ALL)
msvcrt.getch()
os.system('cls' if os.name == 'nt' else 'clear')

while True:
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

  console.print("=-=-=-=- MAIN MENU -=-=-=-=", style="#32384D")
  console.print("\n>>     1.Start Programm     <<", style="#FF0055")
  console.print("\n>>    2.Edit Server Data    <<", style="#FF00AA")
  console.print("\n>>    3.Edit Discord Bot    <<", style="#9000FF")
  console.print("\n>> 4.Edit Advanced Settings <<", style="#4C00FF")
  console.print("\n>>5.Minecraft Server Support<<", style="#0004FF")
  console.print("\n>>        6.Credits         <<\n", style="#0059FF")
  console.print("=-=-=-=-=-=-=-=-=-=-=-=-=-=", style="#32384D")
  console.print("\n-> Press ESC to always get back to the main menu", style="#333148")
  REA = readchar.readkey()

  if REA == "1":
    os.system('cls' if os.name == 'nt' else 'clear')
    server_ping()
