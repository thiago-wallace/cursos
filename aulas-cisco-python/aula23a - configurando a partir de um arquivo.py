from netmiko import ConnectHandler

ips = '192.168.181.101', '192.168.181.102', '192.168.181.103'
routers = []
for ip in ips:
    routers.append({
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'thiago',
        'password': 'cisco',
    })

with open('aula23b_config_router_file') as arquivo:
    config = arquivo.read().splitlines()

for router in routers:
    connect = ConnectHandler(**router)
    output = connect.send_config_set(config, read_timeout=40)
    output += connect.save_config()
    print(output)
    connect.disconnect()
