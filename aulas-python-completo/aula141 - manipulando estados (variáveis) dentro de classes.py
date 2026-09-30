# manipulando estados (variáveis) dentro de classes

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando!')
            return
        self.filmando = True
        print(f'{self.nome} está filmando...')

    def parar_filmagem(self):
        if self.filmando:
            self.filmando = False
            print(f'{self.nome} parou de filmar...')
            return
        print(f'{self.nome} já não está')

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode tirar fotos enquanto está filmando!')
            return
        print(f'{self.nome} está fotografando...')
        print('Feito')


print()

camera_canon = Camera('Canon')
camera_sony = Camera('Sony')

camera_canon.filmar()
camera_canon.filmar()
camera_canon.fotografar()
camera_canon.parar_filmagem()
camera_canon.fotografar()
camera_sony.fotografar()
camera_sony.filmar()

print(f'{camera_canon.filmando=}')
print(f'{camera_sony.filmando=}')
