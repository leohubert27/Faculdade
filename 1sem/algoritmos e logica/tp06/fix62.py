# Nome: Leonardo Vinicius Gurtler Hubert
# RA: 1051392411025

import os

with open('senha.txt', 'a', encoding='utf-8') as arq:
    arq.write('\n 87654321 \n')
    arq.write('101112 \n')
    arq.write('121110 \n')
    arq.write('senha12345678 \n')
    arq.write('senha101112')

arq = open('senha.txt', 'r')
leitura = arq.read()
print(leitura)
arq.close()