from netmiko import ConnectHandler
from getpass import getpass

usuario = input('Usuário: ')
senha = getpass('Senha: ')
with open('aula18b') as arquivo:
    equipamentos = arquivo.read().splitlines()

for ip in equipamentos:
    print('Backup', ip)
    with ConnectHandler(device_type='cisco_ios', username=usuario, password=senha, host=ip) as conexao:
        saida = conexao.send_command('sh run')
    with open(f'backup-{ip}.txt', 'w') as arquivo:
        arquivo.write(saida)
