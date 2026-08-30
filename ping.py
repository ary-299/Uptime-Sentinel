import time
import requests
import yaml
import colorama

with open ("config.yml", "r") as file:
    config=yaml.safe_load(file)

while True:
    for server_id, server_data in config["Servers"].items():
        Name = server_data.get("Name")
        url = server_data.get("IP")
        try:
            start_time = time.time()
            ping = requests.get(url, timeout=3)
            end_time = time.time()
            pingms = round((end_time - start_time)*1000, 0)
            print("\r",Name, "(",url,") |", pingms,"ms", end="")
        except requests.exceptions.RequestException:
            print("Server Offline!")