'''
NAPALM - https://napalm.readthedocs.io/en/latest/
'''

from napalm import get_network_driver
from json import dumps

driver = get_network_driver('ios')
device = driver(
    hostname='192.168.181.101',
    username='thiago',
    password='cisco',
)
device.open()

print('Configurando roteador...')
device.load_merge_candidate('aula25b-R1-config.cfg')
device.commit_config()

output = device.get_bgp_neighbors()
print(dumps(output, indent=4))

device.close()
