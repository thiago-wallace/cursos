# realizando backup dos dispositivos
'''
A aula originalmente, seria com o módulo 'telnetlib', porém esse módulo foi descontinuado do python na versão 3.13 conforme nota em 07/10/2024.
https://docs.python.org/3/library/telnetlib.html
https://www.python.org/downloads/release/python-3130/
A comunidade desenvolveu o módulo 'telnetlib3', sucessor mais próximo do módulo descontinuado e podendo ser importado como 'telnetlib'.
O 'telnetlib3' será instalado via pip e utilizado como substituto.
https://docs.python.org/3.12/library/telnetlib.html
'''
import getpass
import telnetlib

user = input("Digite o login: ")
password = getpass.getpass()

lista_ips = open("aula18b")

for ip in lista_ips:
    ip = ip.strip()
    print("Estamos efetuando o backup do " + ip)

    tn = telnetlib.Telnet(ip)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")
    configuracao = tn.read_all().decode("ascii")
    arquivo = open("backup-" + ip, "w", newline="")
    arquivo.write(configuracao)
    arquivo.write("\n")
    arquivo.close()

print("Backup completo")
