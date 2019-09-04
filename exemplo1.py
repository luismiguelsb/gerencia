from easysnmp import Session

session = Session(hostname='localhost',community='public',version=2)

name = session.get('sysName.0')
upTime = session.get('hrSystemUptime.0')
numberProcess = session.get('hrSystemProcesses.0')
ifNumber = session.get('ifNumber.0')
numberInterfaces = int(ifNumber.value)
Bulk = session.get_bulk(['ipAdEntAddr', 'ifPhysAddress'], 0, numberInterfaces)
vector_IP = {}
vector_MAC = {}

print('Nome do host:' + name.value)
print('Uptime:' + upTime.value)
print('Numero de processos:' + numberProcess.value)
print('Numero de interfaces:' + ifNumber.value)

for i in range(numberInterfaces):
	address_IP = Bulk[i]
	address_MAC = Bulk[i+1]
	vector_IP[i] = address_IP.value
	vector_MAC[i] = address_MAC.value
	print "Interface", i
	print "IP:", vector_IP[i]
	print "MAC:", vector_MAC[i]
