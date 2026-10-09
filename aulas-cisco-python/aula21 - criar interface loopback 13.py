from netmiko import ConnectHandler

R1 = {
    "device_type": "cisco_ios",
    "host": "192.168.181.101",
    "username": "thiago",
    "password": "cisco",
}

connect = ConnectHandler(**R1)
loopback13 = ['interface loopback 13']
configuracao = connect.send_config_set(loopback13)
print(configuracao)
saida = connect.send_command("sh ip int brief")
print(saida)
connect.disconnect()
