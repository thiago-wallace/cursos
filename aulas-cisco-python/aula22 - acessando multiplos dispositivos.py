# acessando multiplos dispositivos e exibindo o seu hostname

from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.181.101',
    'username': 'thiago',
    'password': 'cisco',
}
R2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.181.102',
    'username': 'thiago',
    'password': 'cisco',
}
R3 = {
    'device_type': 'cisco_ios',
    'host': '192.168.181.103',
    'username': 'thiago',
    'password': 'cisco',
}

for router in (R1, R2, R3):
    connect = ConnectHandler(**router)
    print(connect.find_prompt())
    connect.disconnect()

print('Finalizado')
