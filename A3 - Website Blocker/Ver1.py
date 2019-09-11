import time
from datetime import datetime as dt

hosts = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.google.com","google.com","www.microsoft.com","microsoft.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(hosts,'r+') as file:
            content = file.read()
            for website in website_list:
                s = redirect + "    " + website + "\n"
                if s in content:
                    pass
                else:
                    file.write(s)

    else:
        with open(hosts,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            print("Loop")

    time.sleep(5)
