# Ambientes virtuais em Python (venv)
'''
Um ambiente virtual carrega toda a sua instalação do Python para uma pasta no caminho escolhido.
Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.
venv é o módulo que vamos usar para criar ambientes virtuais.
Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são: venv env .venv .env

Verificar versão do python:
    python -V
    python --version

Verificar qual ambiente do Python está sendo utilizado (global ou virtual) no Windows:
    gcm python
    gcm python --Syntax
Verificar qual ambiente do Python está sendo utilizado (global ou virtual) no Linux / MAC:
    which python

Criar ambiente virtual:
    python -m venv "nome do ambiente virtual"
Exemplo:
    python -m venv venv
    python -m venv .venv
    python -m venv ambiente_virtual
'''

