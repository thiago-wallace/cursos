# enviar email SMTP
# enviar email SMTP com Python - Passo a passo


import os
import smtplib
from dotenv import load_dotenv
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = os.getenv('TO_EMAIL', '')

# Configurações SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Caminho e-mail no HTML
CAMINHO_EMAIL = Path(__file__).parent / 'aula219.html'

# Mensagem de texto
with open(CAMINHO_EMAIL, 'r') as arquivo:
    mensagem = arquivo.read()
email_modelo = Template(mensagem)
nomes = {
    'nome_from': os.getenv('NAME_FROM'),
    'nome_to': os.getenv('NAME_TO'),
}
email_preenchido = email_modelo.substitute(nomes)

# Transformar mensagem em MIMEMultipart
# Configurar remetente, destinarário e assunto do email
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'E-mail de Teste em Python'  # Assunto do email
# Configurar corpo do email (Nesse caso em "html", mas se fosse texto simples, seria "plain")
corpo_email = MIMEText(email_preenchido, 'html', 'utf-8')
# Unir configurações e corpo do email
mime_multipart.attach(corpo_email)

# Conectando ao servidor SMTP
with smtplib.SMTP(smtp_server, smtp_port) as servidor:
    # Extend Hello - Iniciar a conexão com o servidor SMTP
    servidor.ehlo()
    # Estabelecer uma conexão segura
    servidor.starttls()
    # Login e senha
    servidor.login(smtp_username, smtp_password)
    # Enviar email configurado
    servidor.send_message(mime_multipart)
    print('E-mail enviado com sucesso')
