nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))

lista_notas = [nota1,nota2,nota3,nota4,nota5]

x = 0
maior_nota = lista_notas[x]

while x < len(lista_notas):
    if lista_notas[x] > maior_nota:
        maior_nota = lista_notas[x]
    x = x+1

print("A maior nota é: ", maior_nota)