#!/usr/local/bin/python3.8
# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-

#=================================================
#Versão 1.2
#28/05/2021
#Autoria: Lídio Julião
#Contato:lidio.ljl@hotmail.com
#=================================================
"""
Este script, tem como finalidade gerar  senhas obedencendo os padrões de  segurança.
com ele, podemos d efinir uma senha que tenha no mínimo oito caracteres e que esteja 
contido letra minúscula, maiúscula e  caracteres especiais. Ele permite que a senha 
que foi gerada, seja escrita em um arquivo com extensão .json.
"""


import random, string
from datetime import datetime

#Caracteres que serão usados para formar a senha.

upper_lower = string.ascii_letters 
number = string.digits
symbols = '!@#$%&*_+=/?-|\[]''"{};.<>' #permite que desta forma, possamos escolher o tipo de caractere para a senha.

#symbols = string.punctuation #Sequencia caracteres especiais.

#Agrupando todos os caracteres

all = upper_lower + number + symbols

#Definindo finalidade e o tamanho da senha

length = int(input("Informe o Tamanho da Senha: "))
goal =input("Onde esta senha será usada? ")


if length >= 8:
    passwd = "".join(random.sample(all, length))
    date = datetime.now()
    date_dt = date.strftime('%d/%m/%Y')
    text = "Olá!, a senha do(a) " + goal + " é: "
    concat_txt = date_dt, ' || ' ,text, passwd + '\n'
    print(date_dt,'||',text,passwd)
    key = open('senha.json', encoding = 'latin-1', mode='a+')
    key.writelines(concat_txt)
    key.close()
else:
    print("**** OPERAÇÃO CANCELADA !!!****" "\n" "**** A senha deve ter pelo menos oito caracteres ****")
    
    
#======================================================================================================










  
