print("Nome: Leonardo Vinícius Gurtler Hubert | RA: 1051392411025")

NomeAluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
MediaGeral = ((nota1*4) + (nota2*6))/10

#trecho de verificação dos valores das notas
def verificar_nota1 (p1):
    if (p1 < 0):
        print("Valor da primeira nota inválido")
    elif (p1 > 10):
        print("Valor da primeira nota inválido")

def verificar_nota2(p2):
    if (p2 < 0):
        print("Valor da segunda nota inválido")
    elif (p2 > 10):
        print("Valor da segunda nota inválido")

#trecho do cálculo da média
def calculo_media(mg):
    if (mg > 10):
        print("Valores Inválidos")
    elif (mg >= 9 <=10):
        print("Conceito do aluno: A / Situação: APROVADO / Média Geral: ", mg)
    elif (mg <9 >= 7):
        print("Conceito do aluno: B / Situação: APROVADO / Média Geral: ", mg)
    elif (mg < 7 >= 3):
        print("Conceito do aluno: C / Situação: EXAME / Média Geral: ", mg)
    elif (mg <3 >=0):
        print("Conceito do aluno: D / Situação: DP / Média Geral: ", mg)
    elif (mg <0):
        print("Valores Inválidos")

verificar_nota1(nota1)
verificar_nota2(nota2)
calculo_media(MediaGeral)