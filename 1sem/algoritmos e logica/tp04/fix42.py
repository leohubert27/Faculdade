print("-----------------------------------------------------")
print("Cálculo de Média")
print("-----------------------------------------------------")

nome = str(input("Digite o nome do aluno: "))
RA = int(input("Digite o RA: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

def media_calc (p1,p2):
    media = (p1 + p2)/2
    print("A média do aluno é: ", media)
    if (media >= 7):
        print("Parabéns, você foi aprovado!")
    else:
        print("Você ainda tem uma chance! Estude mais para o exame.")

media_calc (nota1, nota2)