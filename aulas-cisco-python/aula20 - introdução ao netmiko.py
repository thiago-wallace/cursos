# introdução ao netmiko
'''
netmiko - https://pynet.twb-tech.com/blog/netmiko-python-library.html
'''

from netmiko import ConnectHandler, SSHDetect

R1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.181.101',
    'username': 'thiago',
    'password': 'cisco',
}

connect = ConnectHandler(**R1)
output = connect.send_command('sh ip int brief')
print(output)
connect.disconnect()
