divisao1 = int(input("Digite um número: "))

if (divisao1 % 10 == 0):
    print("O número é divisível por 10!")
elif (divisao1 % 5 == 0):
    print("O número é divisível por 5!")
elif (divisao1 % 2 == 0):
    print("O número é divisível por 2!")
else:
    print("O valor não é divisível por 10, 5 ou 2.")