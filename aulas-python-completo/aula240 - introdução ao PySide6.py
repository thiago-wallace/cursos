# introdução ao PySide6
'''
PySide6 para GUI (interface gráfica) com Qt em Python - Instalação
- A seção original desse curso usou PyQt5 (estamos atualizando para PySide6)
- Essas bibliotecas (PySide e PyQt) usam a biblioteca Qt
- Qt é uma biblioteca usada para a criação de GUI (interface gráfica
  do usuário) escrita em C++.
  - PySide e PyQt conseguem fazer a ponte (binding) entre o Python e a
  biblioteca para a criação de interfaces gráficas sem ter que usar outra
  linguagem de programação.
- PySide6 é uma referencia à versão 6 da Qt (Qt 6)
- Qt é multiplataforma, ou seja, deve funcionar em Windows, Linux e Mac.

Por que mudei de PyQt para PySide na atualização?
- PySide foi desenvolvido pela The Qt Company (da Nokia), como parte do
  projeto Qt for Python project - https://doc.qt.io/qtforpython/
- Por usarem a mesma biblioteca (Qt), PySide e PyQt são extremamente
  similares, muitas vezes os códigos são idênticos. Portanto, mesmo que você
  ainda queira usar PyQt, será muito simples portar os códigos. Muitas vezes
  basta trocar o nome de PySide para PyQt e vice-versa.
- A maior diferença entre PyQt e PySide está na licença:
  PyQt usa GPL ou commercial e PySide usa LGPL.
  Em resumo: com PySide, você tem a permissão uso da biblioteca para fins
  comerciais, sem ter que compartilhar o código escrito por você para o
  público.
  Licenças são tópicos complexos, portanto, se oriente sobre elas
  antes de usar qualquer software de terceiros.
  https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3)

Aulas do antigo PyQt5 (Caso necessário):
https://drive.google.com/drive/folders/18sAhJGlgNOlX5Cz1C2lVXt5ZedZ4i1v4?usp=share_link

Links sobre o PySide6:
https://doc.qt.io/qtforpython/
https://pypi.org/project/PySide6/
'''

import PySide6.QtCore

# exibir a versão do PySide6
print(PySide6.__version__)

# exibir a versão do Qt compilado para o PySide6
print(PySide6.QtCore.__version__)  # type: ignore
