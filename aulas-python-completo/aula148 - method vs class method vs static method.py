# method vs class method vs static method

'''
method vs @classmethod vs @staticmethod

method - self, método de instância
@classmethod - cls, método de classe
@staticmethod - método estático (❌self, ❌cls)
'''


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password, host='localhost'):
        connection = cls(host)
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('Log:', msg)


print()
p1 = Connection('192.168.0.0')
p1.set_user('thiago')
p1.set_password('12345')
p2 = Connection.create_with_auth('thiago', '123456', '192.168.0.1')
print(p1.__dict__)
print(p2.__dict__)
Connection.log('Teste')
