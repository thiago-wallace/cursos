# QWidget e QLayout 1
'''
QWidget e QLayout de PySide6.QtWidgets
QWidget -> genérico
QLayout -> Um widget de layout que recebe outros widgets

QWidget (Não confundir com QtWidget) - Um Widget genérico que serve para receber um QLayout
QLayout - Um Widget que recebe outros Widgets
'''

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

# criando a aplicação que vai monitorar os elementos e ficar em looping
app = QApplication()

# criando os botões
button1 = QPushButton('Botão 1')
button1.setStyleSheet('font-size: 40px; color: blue')
button2 = QPushButton('Botão 2')
button2.setStyleSheet('font-size: 40px; color: red')
button3 = QPushButton('Botão 3')
button3.setStyleSheet('font-size: 40px; color: green')

# criando o widget central - widget genérico para receber o layout
central_widget = QWidget()

# criando o layout VBox - layout vertical
layout = QVBoxLayout()

# adicionando o layout no widget central
central_widget.setLayout(layout)

# adicionando os botões no layout
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)

# adicionar o widget centrar na hierarquia para exibir na janela
central_widget.show()

# executar aplicação para monitorar os elementos e gerenciar o looping
app.exec()
