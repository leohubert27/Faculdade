print("Nome: Leonardo Vinícius Gurtler Hubert | RA: 1051392411025")

horas_trab = int(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor das horas: "))

# trecho para verificar os valores
def verificar_valores (ht, vh):
    if (ht <= 0):
        print("Valor de horas trabalhadas inválidas")
    elif (vh <= 0):
        print("Valor hora inválido")

# trecho para realizar o cálculo de horas a serem pagas
def calculo_salario (hora1, valor1):
    if (hora1 <= 40):
        salario = hora1*valor1
        print("A quantidade de horas trabalhadas foi: ", hora1, ", o valor por hora é R$", valor1, " e o total a ser recebido é: R$", salario)
    elif (hora1 > 40):
        salario = 40*valor1
        hora1 = hora1 - 40
        extra = ((hora1*valor1)*1.5)
        total = salario + extra
        print("A quantidade de horas extras trabalhadas foram: ", hora1, " e o valor total a ser recebido é R$", total)

verificar_valores (horas_trab, valor_hora)
calculo_salario (horas_trab, valor_hora)