# introdução ao napalm
'''
NAPALM - https://napalm.readthedocs.io/en/latest/
'''

from napalm import get_network_driver
import json

driver = get_network_driver('ios')
device = driver(
    hostname='192.168.181.101',
    username='thiago',
    password='cisco'
)
device.open()

print('-- facts')
output = device.get_facts()
print(json.dumps(output, indent=4))

print('-- interfaces')
output = device.get_interfaces()
print(json.dumps(output, indent=4))

print('-- interfaces ip')
output = device.get_interfaces_ip()
print(json.dumps(output, indent=4))

print('-- interfaces counters')
output = device.get_interfaces_counters()
print(json.dumps(output, indent=4))

print('-- arp table')
output = device.get_arp_table()
print(json.dumps(output, indent=4))
