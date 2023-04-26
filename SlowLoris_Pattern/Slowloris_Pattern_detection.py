import pcapy
import re

devices = pcapy.findalldevs()
interface = devices[0]
cap = pcapy.open_live(interface, 65536, 1, 0)

while True:
    (header, payload) = cap.next()

    
    if payload.startswith(b"GET") or payload.startswith(b"POST") or payload.startswith(b"HEAD"):
        
       
        if re.search(b"User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)", payload):
            print("Slowloris detected!")
