from easysnmp import Session

session = Session(hostname='localhost',community='public',version=2, use_sprint_value = True)

name = session.get('sysName.0')
upTime = session.get('hrSystemUptime.0')
numberProcess = session.get('hrSystemProcesses.0')
ifNumber = session.get('ifNumber.0')
numberInterfaces = int(ifNumber.value)
vector_IP = {}
vector_MAC = {}

print('Nome do host:' + name.value)
print('Uptime:' + upTime.value)
print('Numero de processos:' + numberProcess.value)
print('Numero de interfaces:' + ifNumber.value)

Bulk1 = session.get_bulk('ipAdEntAddr', 0, numberInterfaces)
Bulk2 = session.get_bulk('ifPhysAddress', 0, numberInterfaces)

for i in range(numberInterfaces):
	address_IP = Bulk1[i]
	vector_IP[i] = address_IP.value
	address_MAC = Bulk2[i]
	vector_MAC[i] = address_MAC.value
	print "Interface", i
	print "IP:", vector_IP[i]
	print "MAC:", vector_MAC[i]

