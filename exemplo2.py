from easysnmp import Session
import time

session = Session(hostname='localhost', community='public', version=2)

ifNumber = session.get('ifNumber.0')
numberInterfaces = int(ifNumber.value)

valueIN1 = {}
valueIN2 = {}
valueOUT1 = {}
valueOUT2 = {}
IN_BytesPerSec = {}
OUT_BytesPerSec = {}
MAX_BytesPerSec = 1024*1024*5

print('Numero de interfaces:' + ifNumber.value)

while 1>0:
	Bulk = session.get_bulk(['ifInOctets', 'ifOutOctets'], 0, numberInterfaces)
	time.sleep(4)
	Bulk2 = session.get_bulk(['ifInOctets', 'ifOutOctets'], 0, numberInterfaces)

	for i in range(numberInterfaces):
		ifInOctets1 = Bulk[i]
		ifOutOctets1 = Bulk[i+1]

		ifInOctets2 = Bulk2[i]
		ifOutOctets2 = Bulk2[i+1]

		valueIN1[i] = int(ifInOctets1.value)
		valueOUT1[i] = int(ifOutOctets1.value)
		valueIN2[i] = int(ifInOctets2.value)
		valueOUT2[i] = int(ifOutOctets2.value)

		IN_BytesPerSec[i] = (valueIN2[i] - valueIN1[i]) / 5
		OUT_BytesPerSec[i] = (valueOUT2[i] - valueOUT1[i]) / 5

		print "Interface:", i
		print "IN ", valueIN1[i], "bytes"
		print "OUT ", valueOUT1[i], "bytes"
		print "Taxa de entrada ", IN_BytesPerSec[i], "bytes"
		print "Taxa de saida ", OUT_BytesPerSec[i], "bytes"
		print "Maxima: ", MAX_BytesPerSec

		if((IN_BytesPerSec[i] or  OUT_BytesPerSec[i]) >= MAX_BytesPerSec):
			print "Ultrapassou a taxa maxima!" 
