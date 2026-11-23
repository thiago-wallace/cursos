# QApplication e QPushButton
'''
QApplication e QPushButton de PySide6.QtWidgets
QApplication -> O Widget principal da aplicação
QPushButton -> Um botão
PySide6.QtWidgets -> Onde estão os widgets do PySide6

QApplication - é uma das poucas aplicaçãoes do Qt que não mostra nada na tela, utilizado para monitorar e gerenciar o looping de eventos da janela,
    como por exemplo, ele monitora todas as ações possíveis na janela, como um clique em um botão, um minimizar ou maximizar a janela, etc.
QtWidgets - são os elementos que estão na tela/janela, ou seja, cada botão, link, label, box, menu, são coisas que estão no QtWidgets.
'''

from PySide6.QtWidgets import QApplication, QPushButton

# criando a aplicação (Que vai monitorar e gerenciar a janela e todos os elementos)
app = QApplication()

# criando um botão
button1 = QPushButton('Botão 1')

# alterar o estilo do botão, como tamanho e a cor do texto, em Qt Style Sheets (QSS: Mesma sintaxe do CSS para HTML)
button1.setStyleSheet('font-size: 40px; color: blue;')

# adiciona o widget na hierarquia para exibir na janela
button1.show()

# criando outro botão
button2 = QPushButton('Botão 2')

# alterar o estilo do botão, como tamanho e a cor do texto, em Qt Style Sheets (QSS: Mesma sintaxe do CSS para HTML)
button2.setStyleSheet('font-size: 40px; color: red;')

# adiciona o widget na hierarquia para exibir outra janela
button2.show()

# executa a aplicação QApplication
app.exec()

'''
Neste código de exemplo, é exibido uma janela para cada botão, porque o botão normalmente é um Widget final, e para cada botão, foi executado um show(),
    sendo assim, para cada show(), é exibido uma nova janela separada.
Nas futuras aulas, será verificado para inserir um Widget de layout, que permite adicionar outros Widgets dentro dele, como por exemplo, o QMainWindow,
    dessa forma, será possível adicionar o botão no QMainWindow, e executar o show() apenas para o QMainWindow, exibindo uma janela só, com o botão dentro.

Widget de layout - são Widgets utilizados para adicionar outros Widgets dentro dele. Exemplo: uma janela, um painel, etc.
Widget final - são Widgets utilizados para exibir aquele elemento final, em que não deverá ser adicionar nada dentro dele. Exemplo: um botão, uma caixa de
    texto, etc.
'''
