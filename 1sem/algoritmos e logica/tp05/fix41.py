valor = int(input("Digite o valor inteiro que será fatorado: "))
fatoracao = 1

for c in range(valor,1,-1):
    fatoracao = fatoracao*c

print("O valor do fatorial de ",valor, "é ", fatoracao)