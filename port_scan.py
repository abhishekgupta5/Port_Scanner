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

if (args.startport) and args.endport:
    start_port = int(args.startport)
    end_port = int(args.endport)
else:
    flag = 1

open_ports = []

common_ports = {
    '21': 'FTP',
    '22': 'SSH',
    '23': 'TELNET',
    '25': 'SMTP',
    '53': 'DNS',
    '69': 'TFTP',
    '80': 'HTTP',
    '109': 'POP2',
    '110': 'POP3',
    '123': 'NTP',
    '143': 'IMAP',
    '156': 'SQL-SERVER',
    '389': 'LDAP',
    '443': 'HTTPS',
    '546': 'DHCP-CLIENT',
    '547': 'DHCP-SERVER',
    '995': 'POP3-SSL',
    '993': 'IMAP-SSL',
    '3306': 'MYSQL',
    }

