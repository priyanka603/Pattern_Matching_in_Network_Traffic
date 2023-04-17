#! /usr/bin/python
import pcapy

# Gives list of all the connected devices.
devices=pcapy.finalldevs() 

#Used first interface
inf=devices[0]

#Live packet capturing in which 65536 is the size of packet (bytes to capture per packet) and third parameter is 1 which specifies promiscuous mode (This mode allows a network adapter to pass all received traffic,
#no matter to which adapter the traffic is addressed and last parameter is timeout which is 0.
cap=pcapy.open_live(inf, 65536,1,0) 

#Variable count
count=1

#This loop is the one which print the number of packets captured.
while count:
(header, payload) =cap.next() 
print count
count+=1
