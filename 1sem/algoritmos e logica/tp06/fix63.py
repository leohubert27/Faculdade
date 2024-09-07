# Nome: Leonardo Vinicius Gurtler Hubert
# RA: 1051392411025

import os

arq = open('mensagem.txt', 'r', encoding='utf-8')
print(arq.readlines())
print(arq.tell())
arq.close()

with open('mensagem.txt', 'r', encoding='utf-8') as lista_palavras:
    palavras = lista_palavras.read().split(' ')
    print(palavras)