NomeAluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
MediaGeral = ((nota1*4) + (nota2*6))/10

if (MediaGeral > 10):
    print("Valores Inválidos")
elif (MediaGeral >= 9 <=10):
    print("Conceito do aluno: A / Situação: APROVADO / Média Geral: ", MediaGeral)
elif (MediaGeral <9 >= 7):
    print("Conceito do aluno: B / Situação: APROVADO / Média Geral: ", MediaGeral)
elif (MediaGeral < 7 >= 3):
    print("Conceito do aluno: C / Situação: EXAME / Média Geral: ", MediaGeral)
elif (MediaGeral <3 >=0):
    print("Conceito do aluno: D / Situação: DP / Média Geral: ", MediaGeral)
elif (MediaGeral <0):
    print("Valores Inválidos")