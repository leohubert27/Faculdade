print("-----------------------------------------------------")
print("Cálculo de aumento")
print("-----------------------------------------------------")

salario1 = float(input("Digite o valor do seu salário: "))

def aumento (valor1):
    if (valor1 >= 2500):
        print ("Seu aumento foi de 5%, seu novo salário será R$ ", valor1*1.05)
    elif (valor1 > 1500 < 2500):
        print ("Seu aumento foi de 10%, seu novo salário será R$ ", valor1*1.1)
    elif (valor1 <= 1500):
        print ("Seu aumento foi de 20%, seu novo salário será R$ ", valor1*1.2)
    
aumento (salario1)