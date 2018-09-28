#Author: Andre Ortega, brainwork.com.br

import getpass
import netmiko
import csv
import logging
from netmiko import ConnectHandler

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

print('\n''Script initiated')
#Get credentials
UN = raw_input('Username: ')
PW = getpass.getpass('Password: ')
EN = getpass.getpass('Enable: ')

#Template Default with credentials
device_template = {
'device_type': 'cisco',
'ip': '1.1.1.1',
'username': UN,
'password': PW,
'port':1111,
'secret': EN
}

#Open file with devices informations (IP and Port)
input_file = csv.DictReader(open('devices_to_configure.csv'))

#Prepar device_template with information from CSV
for row in input_file:
	if (row['port']) == '23':
		device_template['device_type'] = 'cisco_ios_telnet'
		device_template['port'] = '23'
	else:
		device_template['device_type'] = 'cisco_ios'
		device_template['port'] = '22'
	device_template['ip'] = row['ip']
	#Connect to device and send config
	print ('===== Initiating config on device ',device_template['ip'],' =====')
	net_connect = ConnectHandler(**device_template)
	net_connect.enable()
	output = net_connect.send_config_from_file('commands_to_send.txt')
	print(output)
	#Save logs ond file
	log = open('log_file.txt', 'a')
	log.write(output)
	log.write('\n')
	net_connect.disconnect()
	print ('===== Config on device', device_template['ip'],' done! =====')
print('\n' 'Script finished')
