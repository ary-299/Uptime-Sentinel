import time
import requests
import yaml
with open ("config.yml", "r") as file:
    config=yaml.safe_load(file)

URL1= config ["Servers"]["server1"]["IP"]
URL2= config ["Servers"]["server2"]["IP"]
URL3= config ["Servers"]["server3"]["IP"]


start_time = time.time()
try: response=requests.get()