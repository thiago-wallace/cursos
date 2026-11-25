# QMainWindow e centralWidget
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
from functools import partial

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
status_bar.showMessage('Teste')

# adicionando um menu
menu = window.menuBar()
opcao1 = menu.addMenu('Opção 1')
opcao2 = menu.addMenu('Opção 2')
opcao1_1 = opcao1.addAction('Opção 1.1')
opcao2_1 = opcao2.addAction('Opção 2.1')


# função para alterar mensagem na barra de status, para ser usada como ação
def escrever_barra_status(status_bar):
    status_bar.showMessage('Opção clicada')


# adicionando uma ação ao menu opção1_1 - Forma 1: utilizando lambda
opcao1_1.triggered.connect(lambda: escrever_barra_status(status_bar))
# adicionando uma ação ao menu opção2_1 - Forma 2: utilizando functools.partial
opcao2_1.triggered.connect(partial(escrever_barra_status, status_bar))

# mostrando o QMainWindow e executando o QApplication
window.show()
app.exec()
