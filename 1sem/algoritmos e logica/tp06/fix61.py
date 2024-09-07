# Nome: Leonardo Vinicius Gurtler Hubert
# RA: 1051392411025

import os

with open('email.txt', 'a+', encoding='utf-8') as arq:
    arq.write('\n zezinho_python@gmail.com \n')
    arq.write('joaozinho_python@gmail.com \n')
    arq.write('marquinhos_python@gmail.com \n')

arq = open('email.txt', 'r')
leitura = arq.read()
print(leitura)
arq.close()