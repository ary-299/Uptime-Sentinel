import time
import requests
import yaml
import colorama
import msvcrt

colorama.init()

COLOR_MAP = {
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
}

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

def server_ping(): 
    servers = list(config["Servers"].values()) 
    num_servers = len(servers) 
    total_lines = num_servers * 2
    ping_swiftness = config.get("settings", {}).get("ping_swiftness_in_s", 1)
    # Quick initialization message without blocking network requests
    print("Initializing servers..." ,end="\r")
    time.sleep(0.5)
    print("Enjoy!                                      ",end="\r")

    # Print blank lines down so the cursor has room to jump back up
    print("\n" * total_lines, end="")

    try:
        while True:
            # Move cursor back up to the top of our block
            print(f"\033[{total_lines}A", end="") 
            
            for server_data in servers: 
                name = server_data.get("Name") 
                url = server_data.get("IP") 
                good_threshold = config.get("settings", {}).get("good_ping", 700)
                bad_threshold = config.get("settings", {}).get("bad_ping", 1000)
                
                try:
                    start_time = time.time() 
                    # Reduced timeout to 1.5 seconds to prevent freezing on bad venue Wi-Fi
                    response = requests.get(url, timeout=1.5) 
                    end_time = time.time() 
                    pingms = round((end_time - start_time) * 1000, 0) 
                    
                    if pingms <= good_threshold:
                        ping_color = colorama.Fore.GREEN
                    elif good_threshold < pingms < bad_threshold:
                        ping_color = colorama.Fore.YELLOW
                    else:
                        ping_color = colorama.Fore.RED
                    status = f"Online ({pingms} ms)" 
                except requests.exceptions.RequestException: 
                    ping_color = colorama.Fore.RED
                    status = "Offline"
                    
                raw_color = server_data.get("color", "WHITE")
                color_web = COLOR_MAP.get(str(raw_color), colorama.Fore.WHITE)
                print(f"{color_web}{name}{colorama.Style.RESET_ALL} | {colorama.Fore.GREEN}{url}{colorama.Style.RESET_ALL} | {ping_color}{status}{colorama.Style.RESET_ALL}                           ")
                print(f"{colorama.Fore.LIGHTBLACK_EX}###################################################################{colorama.Style.RESET_ALL}")
                print(f"{colorama.Fore.RED}PRESS ANY KEY TO RETURN TO MAIN MENU", {colorama.Style.RESET_ALL})

                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    print("Key detected, returning to main menu...")
            time.sleep(ping_swiftness) 

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    server_ping()