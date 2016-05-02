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
