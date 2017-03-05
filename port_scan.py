#!/usr/bin/python3

import socket, sys, time, datetime, argparse, os
flag = 0
os.system('clear')
line = '#' * 50
desc = line + '''\nA simple port scanner that works!\nExample Usage:
python port_scan.py abcd.com 1 100
The above example will scan the host \'abcd.com\' from 1 to 100.
To scan most common ports, use: python port_scan.py abcd.com\n''' + line

#Argparse is used to parse arguments
parser = argparse.ArgumentParser(description = desc, formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('host', metavar='H', help='Host name to be scanned')
parser.add_argument('startport', metavar='P1', nargs='?', help="Start scanning from this port")
parser.add_argument('endport', metavar='P2', nargs='?', help="Scan until this port")

args = parser.parse_args()

host = args.host #The hostname to scan for open ports

ip = socket.gethostbyname(host) #Converts the hostname into IP address
