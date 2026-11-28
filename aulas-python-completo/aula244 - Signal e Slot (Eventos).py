# Signal e Slot (Eventos)
'''
Árvore de camadas e execução:

-> QApplication (app)
  -> QMainWindow (window->setCentralWidget)
      -> CentralWidget (central_widget)
          -> Layout (layout)
              -> Widget 1 (botao1)
              -> Widget 2 (botao2)
              -> Widget 3 (botao3)
  -> show
-> exec
'''

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PySide6.QtCore import Slot

# iniciando cada item de acordo com a árvore acima
app = QApplication()
window = QMainWindow()
central_widget = QWidget()
layout = QGridLayout()
botao1 = QPushButton('Botão 1')
botao2 = QPushButton('Botão 2')

# dentro do QMainWindow, será colocado o QWidget
window.setCentralWidget(central_widget)
# dentro do QWidget, será colocado o QGridLayout
central_widget.setLayout(layout)
# dentro do QGridLayout, será colocado os QPushButton
layout.addWidget(botao1, 1, 1)
layout.addWidget(botao2, 1, 2)

# configurando o visual do botão com QSS
botao1.setStyleSheet('font-size: 40px; color: blue;')
botao2.setStyleSheet('font-size: 40px; color: red;')

# configurando a barra de título da janela
window.setWindowTitle('Aula 243')

# adicionando uma barra de status
status_bar = window.statusBar()
# alterando a mensagem na barra de status
status_bar.showMessage('Barra de status')

# adicionando um menu
menu = window.menuBar()
opcao1 = menu.addMenu('Opção 1')
opcao2 = menu.addMenu('Opção 2')
opcao1_1 = opcao1.addAction('Opção 1.1')
opcao1_2 = opcao1.addAction('Opção 1.2')
opcao2_1 = opcao2.addAction('Opção 2.1')
opcao2_2 = opcao2.addAction('Opção 2.2')
opcaoStatus = opcao1.addAction('Opção Status')


# EVENTOS
''' Menu:
Opção 1.1 e 2.1 - Ao clicar, exibirá uma mensagem na barra de status
Opção 1.2 - Será checkable. Ao mudar o status, exibirá o status na barra de status
Opção 2.2 - Será checkable. Ao mudar o status, exibirá uma mensagem e o status na barra de status
Opção Status - Ao passar o mouse, exibirá um print com o status da Opção 1.2 e 2.2
Botão 1 e 2 - Ao clicar, exibirá uma mensagem na barra de status

Signal - é o sinal enviado do elemento na tela
Slot - a função que será executada quando aquele sinal for recebido

As funções que são chamadas pelos eventos da tela (Slots), é recomendável decorar elas com @Slot (PySide6.QtCore.Slot)
'''


# função para adiar execução das funções
@Slot()
def executar(funcao, *args, **kwargs):
    def inner():
        funcao(*args, **kwargs)
    return inner


# função para alterar mensagem na barra de status, para ser usada como ação
def click(status_bar, mensagem):
    status_bar.showMessage(mensagem)


# função para mostrar na barra de status se a opção está habilitada
@Slot()
def check1(checked):
    status_bar.showMessage(f'Opção ativa: {checked}')


# função para mostrar na barra de status uma mensagem e se a opção está habilitada
def check2(status_bar, mensagem, opcao_checkable):
    status_bar.showMessage(f'{mensagem}: {opcao_checkable.isChecked()}')


@Slot()
def exibir_status():
    mensagem = f'Opção 1.2 {opcao1_2.isChecked()} - '
    mensagem += f'Opção 2.2 {opcao2_2.isChecked()}'
    status_bar.showMessage(mensagem)
    print(mensagem)


# ação ao clicar no menu opcao1_1 e opcao2_1
opcao1_1.triggered.connect(executar(click, status_bar, 'Opção 1.1 clicada'))
opcao2_1.triggered.connect(executar(click, status_bar, 'Opção 2.1 clicada'))

# configurar o menu opcao1_2 e opcao2_2 para ser habilitado/desabilitado (checkable)
opcao1_2.setCheckable(True)
opcao2_2.setCheckable(True)

# ação ao mudar o status do menu opcao1_2 - mostrando o status
# obs: o toggled automaticamente entra com um parâmetro bool, indicando se a opção está ativa ou não
opcao1_2.toggled.connect(check1)
# ação ao mudar o status do menu opcao2_2 - mostrando a mensagem e o status
# obs: o toggled automaticamente entra com um parâmetro bool, porém nesse caso, o parâmetro não está sendo utilizado
opcao2_2.toggled.connect(executar(check2, status_bar, 'Opção 2.2', opcao2_2))

# ação ao passar o mouse no menu opcaoStatus
opcaoStatus.hovered.connect(exibir_status)

# ação ao clicar no botão botao1 e botao2
botao1.clicked.connect(executar(click, status_bar, 'Botão 1 clicado'))
botao2.clicked.connect(executar(click, status_bar, 'Botão 2 clicado'))

# mostrando o QMainWindow e executando o QApplication
window.show()
app.exec()
