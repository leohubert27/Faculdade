salario1 = float(input("Digite o valor do seu salário: "))

if (salario1 <= 1500):
    print("Você recebeu um acréscimo de 20%. Seu novo salário é: ", salario1*1.2)
elif (salario1 <= 2500):
    print("Você recebeu um acréscimo de 10%. Seu novo salário é: ", salario1*1.1)
elif (salario1 > 2500):
    print("Você recebeu um acréscimo de 5%. Seu novo salário é: ", salario1*1.05)