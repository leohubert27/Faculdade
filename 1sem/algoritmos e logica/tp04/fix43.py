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
    elif (media <7):
        print("Será necessário fazer o exame...")
        exame = float(input("Digite a nota do exame: "))
        media_exame = (media + exame)/2
        print("A sua nova média é: ", media_exame)
        if (media_exame >= 5):
            print("Parabéns, você aproveitou sua chance e foi aprovado!")
        else:
            print("Você não alcançou o resultado desejado, estude mais para a próxima!")

media_calc (nota1, nota2)