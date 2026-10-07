# configurando OSPF no roteador R2 192.168.181.102
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

HOST = "192.168.181.102"
user = input("Digite o login: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"interface g0/1\n")
tn.write(b"ip address 10.100.102.2 255.255.255.252\n")
tn.write(b"no shutdown\n")
tn.write(b"end\n")

tn.write(b"conf t\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 10.100.102.0 0.0.0.3 area 0\n")
tn.write(b"end\n")

tn.write(b"conf t\n")
tn.write(b"interface g0/2\n")
tn.write(b"ip address 10.100.203.1 255.255.255.252\n")
tn.write(b"no shutdown\n")
tn.write(b"end\n")

tn.write(b"conf t\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 10.100.203.0 0.0.0.3 area 0\n")
tn.write(b"end\n")

tn.write(b"wr\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))
