print("-------------------------------------------------")
print("Cálculo de Média do Aluno")
print("-------------------------------------------------")

nome = str(input("Digite o nome do Aluno: "))
RA = str(input("Digite o RA: "))
nota1 = float(input("Digite a Primeira nota: "))
nota2 = float(input("Digite a Segunda nota: "))
media_geral = (nota1+nota2)/2

if (media_geral >= 7):
   print("Parabéns! Você foi aprovadx!")
else:
   print("Você ainda tem uma chance, estude mais para o próximo exame")