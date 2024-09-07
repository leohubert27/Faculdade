valor1 = int(input("Digite um valor inteiro (positivo ou negativo): "))

if (valor1 < 0):
    print(valor1*-1)
elif (valor1 > 10):
    valor2 = int(input("Digite um novo valor: "))
    print("A diferença é ", valor1-valor2)
else:
    print(valor1/5)