from scapy.all import *

dstIP = "10.10.111.1"
srcPort = RandShort()

result = {'Open':[], 'Closed': [], 'Filtered':[]}

for dstPort in range(101):
	scanResponse = sr1(IP(dst=dstIP)/TCP(sport=srcPort,dport=dstPort,flags="S"),timeout=5)

	if(str(type(scanResponse))=="<type 'NoneType'>"):
		scanResponse = sr1(IP(dst=dstIP)/TCP(sport=srcPort,dport=dstPort,flags="S"),timeout=5)
	if(str(type(scanResponse))=="<type 'NoneType'>"):
		result['Filtered'].append(dstPort)
	elif(scanResponse.haslayer(TCP)):
		if(scanResponse.getlayer(TCP).flags == 0x12):
			result['Open'].append(dstPort)
		elif (scanResponse.getlayer(TCP).flags == 0x14):
			result['Closed'].append(dstPort)
	elif(scanResponse.haslayer(ICMP)):
		if(int(scanResponse.getlayer(ICMP).type)==3 and int(scanResponse.getlayer(ICMP).code) in [0,1,2,3,9,10,13]):
			result['Filtered'].append(desPort)

print "Ports Open:"
print result['Open']

print "Ports Closed:"
print result['Closed']

print "Ports Filtered:"
print result['Filtered']


