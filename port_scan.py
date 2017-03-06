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

starting_time = time.time()
print('+'*40)
print('\tSimple Port Scanner!!')
print('+'*40)

if (flag):
    print('Scanning for most common ports on %s' % (host))
else:
    print('Scanning %s from port %s - %s: ' % (host, start_port, end_port))

print("Scanning started at %s" % (time.strftime("%I:%M:%S %p")))

def check_port(host, port, result = 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((host,port))
        if r == 0:
            result = r
        sock.close()
    except Exception, e:
        pass
    return result

def get_service(port):
    port = str(port)
    if port in common_ports:
        return common_ports[port]
    else:
        return 0

try:
    print("scan in progress")
    print("connecting to port")
    if flag:
        for p in sorted(common_ports):
            sys.stdout.flush()
            p = int(p)
            print(p),
            response = check_port(host,p)
            if (response == 0):
                open_ports.append(p)
                sys.stdout.write('\b'* len(str(p)))
    else:
        for p in range(start_port, end_port+1):
            sys.stdout.flush()
            p = int(p)
            print(p),
            response = check_port(host,p)
            if response == 0:
                open_ports.append(p)
            if not p == end_port:
                sys.stdout.write('\b'* len(str(p)))
    print("\nScanning completed at %s" % (time.strftime("%I:%M:%S:%p")))
    ending_time = time.time()
    total_time = ending_time - starting_time
    print("="*50)
    print("\tScan report: %s" % (host))
    print("="*50)

    if (total_time <= 60):
        total_time = str(round(total_time, 2))
        print("Scan took %s seconds" %(total_time))
    else:
        total_time = total_time/60
        print("Scan took %s minutes" %(total_time))
    if open_ports:
        print("Open ports: ")
        for i in sorted(open_ports):
            service = get_service(i)
            if not service:
                service = "Unknown Service"
            print("\t%s %s: Open" %(i, service))
    else:
        print("Sorry, No open ports found!!")

except KeyboardInterrupt:
    print("You pressed ctrl-c. Exiting.")
    sys.exit(1)

