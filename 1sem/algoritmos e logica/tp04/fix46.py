valor1 = int(input("Digite um valor: "))

def calculo (numero):
    if (numero < 0):
        print("O valor sem módulo é: ",abs(numero))
    elif (numero > 10):
        numero2 = int(input("Digite outro valor: "))
        subtracao = numero - numero2
        print("A diferença entre os valores é: ",abs(subtracao))
    else:
        print("O valor dividido por 5 é: ", numero/5)
    
calculo (valor1)