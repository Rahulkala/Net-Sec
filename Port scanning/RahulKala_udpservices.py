from scapy.all import *

dstIP = "10.10.111.1"

result = {'Filtered':[], 'Open': [], 'Closed':[], 'Open|Filtered':[]}

for dstPort in range(101):
	scanResponse = sr1(IP(dst=dstIP)/UDP(dport=dstPort),timeout=5)

	if(str(type(scanResponse))=="<type 'NoneType'>"):
		scanResponse = sr1(IP(dst=dstIP)/UDP(dport=dstPort),timeout=5)

	if(str(type(scanResponse))=="<type 'NoneType'>"):
		result['Open|Filtered'].append(dstPort)
	elif(scanResponse.haslayer(UDP)):
		result['Open'].append(dstPort)
	elif(scanResponse.haslayer(ICMP)):
		if(int(scanResponse.getlayer(ICMP).type)==3 and int(scanResponse.getlayer(ICMP).code)==3):
			result['Closed'].append(dstPort)
		if(int(scanResponse.getlayer(ICMP).type)==3 and int(scanResponse.getlayer(ICMP).code) in [1,2,9,10,13]):
			result['Filtered'].append(desPort)

print "Ports Open:"
print result['Open']

print "Ports Closed:"
print result['Closed']

print "Ports Filtered"
print result['Filtered']

print "Ports Open|Filtered:"
print result['Open|Filtered']

dnsResp = sr1(IP(dst=dstIP)/UDP(dport=53)/DNS(qd=DNSQR(qname="mock.nyu.edu")), timeout=5)
if(str(type(dnsResp)) != "<type 'NoneType'>"):
	if(dnsResp.haslayer(DNS)):
		result['Filtered|Open'].remove(53)
		result['Open'].append(53)

conf.checkIPaddr = False
fam,hw = get_if_raw_hwaddr(conf.iface)
print "hw addr will be used: " + str(hw)
dhcpDisc = Ether(dst="ff:ff:ff:ff:ff:ff")/\
		IP(src="0.0.0.0",dst="255.255.255.255")/\
		UDP(sport=68,dport=67)/\
		BOOTP(chaddr=hw)/\
		DHCP(options=[("message-type","discover"),"end"])

dhcpDisc.show()
ans, unans = srp(dhcpDisc,timeout=5)
print str(ans)
for p in ans:
	if(p[1][IP].src == dstIP):
		result['Filtered|Open'].remove(67)
		result['Open'].append(67)


print "Ports Open:"
print result['Open']

print "Ports Closed:"
print result['Closed']

print "Ports Filtered"
print result['Filtered']

print "Ports Open|Filtered:"
print result['Open|Filtered']

