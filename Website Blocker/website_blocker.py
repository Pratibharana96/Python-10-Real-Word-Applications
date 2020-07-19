import time
from datetime import datetime as dt
hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc"
redirects= "127.0.0.1"
website_list= ["www.facebook.com","facebook.com","www.youtube.com"]

while True:
    

    if dt(dt.now().year,dt.now().month,dt.now().day,6) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working  Hours...")
        with open(hosts_temp,'r+') as hostsfile:
            hostsdata= hostsfile.read()
            for website in  website_list:
            
                if website in hostsdata:
                    pass
                else:
                    hostsfile.write("\n"+ redirects +" "+ website+"\n")

            
    else:
        print("Fun Hours...")
    time.sleep(5)
   