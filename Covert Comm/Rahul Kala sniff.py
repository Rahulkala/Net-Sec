import sys
from scapy.all import*

loop = 15
a = sniff(count=15)
str = ""

for i in range (1,loop):
	if a[i].getlayer(1).id == 0 :
		print("Start of data receive from Server")
	if a[i].getlayer(1).id == 1111 :
		print("End of data from Server")
		break
	str+=chr(a[i].getlayer(1).id)
	
print("Covert Msg from Server: "+str)