import sys
from scapy import*

d="10.10.111.106"
s="10.10.111.199"

port=1025

a_string="rahul"

ip_start = IP(src=s,dst=d, id=0)
send(ip_start/TCP(sport=5000,dport=port))

for letter in a_string:
    ip=IP(src=s,dst=d, id=ord(letter))
	t=TCP(sport=5000,dport=port)
	send(ip/t)
	port=port+1
	ip.show()
	
ip_end=IP(src=s,dst=d, id=1111)
send(ip_end/TCP(sport=5000,dport=port))