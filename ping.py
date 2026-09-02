import time
import requests
import yaml
import colorama

colorama.init()

color_map = {

    "BLACK": colorama.Fore.BLACK,
    "RED": colorama.Fore.RED,
    "GREEN": colorama.Fore.GREEN,
    "YELLOW": colorama.Fore.YELLOW,
    "BLUE": colorama.Fore.BLUE,
    "MAGENTA": colorama.Fore.MAGENTA,
    "CYAN": colorama.Fore.CYAN,
    "WHITE": colorama.Fore.WHITE,
    "RESET": colorama.Fore.RESET,
    "LIGHTBLACK": colorama.Fore.LIGHTBLACK_EX,
    "LIGHTRED": colorama.Fore.LIGHTRED_EX,
    "LIGHTGREEN": colorama.Fore.LIGHTGREEN_EX,
    "LIGHTYELLOW": colorama.Fore.LIGHTYELLOW_EX,
    "LIGHTBLUE": colorama.Fore.LIGHTBLUE_EX,
    "LIGHTMAGENTA": colorama.Fore.LIGHTMAGENTA_EX,
    "LIGHTCYAN": colorama.Fore.LIGHTCYAN_EX,
    "LIGHTWHITE": colorama.Fore.LIGHTWHITE_EX,

    "colorama.Fore.BLACK": colorama.Fore.BLACK,
    "colorama.Fore.RED": colorama.Fore.RED,
    "colorama.Fore.GREEN": colorama.Fore.GREEN,
    "colorama.Fore.YELLOW": colorama.Fore.YELLOW,
    "colorama.Fore.BLUE": colorama.Fore.BLUE,
    "colorama.Fore.MAGENTA": colorama.Fore.MAGENTA,
    "colorama.Fore.CYAN": colorama.Fore.CYAN,
    "colorama.Fore.WHITE": colorama.Fore.WHITE,
    "colorama.Fore.RESET": colorama.Fore.RESET,
    "colorama.Fore.LIGHTBLACK_EX": colorama.Fore.LIGHTBLACK_EX,
    "colorama.Fore.LIGHTRED_EX": colorama.Fore.LIGHTRED_EX,
    "colorama.Fore.LIGHTGREEN_EX": colorama.Fore.LIGHTGREEN_EX,
    "colorama.Fore.LIGHTYELLOW_EX": colorama.Fore.LIGHTYELLOW_EX,
    "colorama.Fore.LIGHTBLUE_EX": colorama.Fore.LIGHTBLUE_EX,
    "colorama.Fore.LIGHTMAGENTA_EX": colorama.Fore.LIGHTMAGENTA_EX,
    "colorama.Fore.LIGHTCYAN_EX": colorama.Fore.LIGHTCYAN_EX,
    "colorama.Fore.LIGHTWHITE_EX": colorama.Fore.LIGHTWHITE_EX,
}

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

def server_ping():                                                      #creates the "server ping" command to print servers and URLS entered in the YML aswell as calculating the length of the ping in ms
    timeout_counter = 0

    servers = list(config["Servers"].values())                          #enters all the added servers inside the yaml into a list called "servers"
    num_servers = len(servers)                                          #counts the amount of entries inside the list and sets them as the variable "num_servers"
    total_lines = num_servers * 2
    ping_swiftness = config.get("settings",{}).get("ping_swiftness_in_s",1)

    for server_data in servers:                                         #the for loop loops everything inside it for every single server added inside the yaml
        name = server_data.get("Name")                                  #the name variable changes with every loop, it goes down one server inside the yaml each loop. If the name for server 1 is google and the name of server 2 is youtube, the {name} is google for the fist loop, and in the second loop itll be youtube
        print(f"Initializing {name}...")
        print("\n" * total_lines, end="")

    try:
        while True:
            print(f"\033[{num_servers}A", end="")                       #\033 literally stands for "ESC". \033 here basically says "stop treating the incoming characters like text to read and look for a command to execute"
                                                                        #The "A" means "move up the cursor by one row"
            for server_data in servers:                                 #The for loop flips to each server entered into the yaml
                name = server_data.get("Name")                          #"name" is the name of the server the loop is looking at at the moment. This changes every time the loop is restarting. It flips down the list each time it restarts
                url = server_data.get("IP")                             #same as in line26, just now instead of the name it asks for the IP
                good_threshold = config.get("settings", {}).get("good_ping", 70)
                bad_threshold = config.get("settings", {}).get("bad_ping", 300)
                
                try:

                    start_time = time.time()                            #important for the calculation of the ping in ms, this safes the timestamp this command is ran. This timestamp is saved on the variable "start_time"
                    response = requests.get(url, timeout=3)             #pings set server. The url variable set before is being used here. The variable is needed so each server will pinged with help of the for loop
                    end_time = time.time()                              #same with start_time, just for the end_time
                    pingms = round((end_time - start_time) * 1000, 0)   #This calculates the exact ping in ms by subtracting the timestamp that was set right after the server was pinged from the timestamp that was created right before it. Then multiply it by 1000 to get it in ms
                    if pingms <= good_threshold:
                        ping_color = colorama.Fore.GREEN
                    elif pingms > good_threshold and pingms < bad_threshold:
                        ping_color= colorama.Fore.YELLOW
                    else:
                        ping_color = colorama.Fore.RED
                    status = f"Online ({pingms} ms)"                    #status sets the text "Online ({pingms}ms) to the variable of status."             
                except requests.exceptions.RequestException:            #if the ping command gives out requests.exceptions.RequestException (which basically means that the ping wasnt possible and the server is so offline) the variable status is set to offline
                    ping_color= colorama.Fore.RED
                    status = "Offline"
                raw_color = server_data.get("color", "WHITE")
                color_web = color_map.get(str(raw_color), colorama.Fore.WHITE)

                print(f"{color_web}{name}{colorama.Style.RESET_ALL} | {colorama.Fore.GREEN}{url}{colorama.Style.RESET_ALL} | {ping_color}{status}{colorama.Style.RESET_ALL}                           ")
                print(f"{colorama.Fore.LIGHTBLACK_EX}###################################################################{colorama.Style.RESET_ALL}")

            time.sleep(ping_swiftness)                                  #makes use of the ping swiftness inside the yaml so you can configure at what pace the ping is updated

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")                                  #if a keyboard input is done, the monitoring will be stopped and can only be started again if the programm is restarted