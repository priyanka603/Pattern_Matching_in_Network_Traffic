#!/usr/bin/python

import pcapy

from struct import *

devs=pcapy.findalldevs()

inf=devs[0]

cap=pcapy.open_live(inf,65536,1,0)




while 1:
        (header,payload)=cap.next()
        
        #layer header .
        l2hdr=payload[:14]
        
        #layer data
        l2data=unpack("!6s6sH",l2hdr)
        
        #source mac address
        
        srcmac="%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" %((l2hdr[0]),(l2hdr[1])
        ,(l2hdr[2]),(l2hdr[3]),(l2hdr[4]),(l2hdr[5]))
        
        #destination mac address 48 bit.
        
        dstmac="%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" %((l2hdr[6]),(l2hdr[7])
        ,(l2hdr[8]),(l2hdr[9]),(l2hdr[10]),(l2hdr[11]))
        
        print("Source MAC: ",srcmac, "Destination MAC: ",dstmac)
        
        iphdr=unpack("!BBHHHBBH4s4s",payload[14:34])
        
        ttl=iphdr[5]
        prot=iphdr[6]
        
        print("Protocol",str(prot),"Time to live: ",str(ttl))
        
        
