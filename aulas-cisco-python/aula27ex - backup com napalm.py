from napalm import get_network_driver
from getpass import getpass

usuario = input('Usuário: ')
senha = getpass('Senha: ')
with open('aula18b') as arquivo:
    equipamentos = arquivo.read().splitlines()
driver = get_network_driver('ios')
for ip in equipamentos:
    print('Backup', ip)
    with driver(username=usuario, password=senha, hostname=ip) as conexao:
        config = conexao.get_config()
    with open(f'backup-{ip}.cfg', 'w') as arquivo:
        arquivo.write(config['running'])
