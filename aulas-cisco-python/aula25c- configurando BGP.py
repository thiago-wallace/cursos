'''
NAPALM - https://napalm.readthedocs.io/en/latest/
'''

from napalm import get_network_driver
from json import dumps
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

routers = [
    {'host': '192.168.181.101', 'config': 'aula25b-R1-config.cfg'},
    {'host': '192.168.181.102', 'config': 'aula25b-R2-config.cfg'},
]

driver = get_network_driver('ios')

for router in routers:
    device = driver(
        hostname=router['host'],
        username=username,
        password=password,
    )
    device.open()

    print(f'Configurando roteador {router["host"]}...')
    device.load_merge_candidate(router['config'])
    device.commit_config()

    output = device.get_bgp_neighbors()
    print(dumps(output, indent=4))

    device.close()
