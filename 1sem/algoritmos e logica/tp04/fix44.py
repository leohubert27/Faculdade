import math

valor1 = int(input("Digite um valor de 1 a 9: "))

if (valor1 <= 2):
    print(pow(valor1, 3))
elif ((valor1 % 3) == 0):
    print(math.factorial(valor1))
elif (valor1 <= 9):
    print(valor1/9)
else:
    print("Valor inválido.")