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
elif (media_geral <7):
   print("Será necessário fazer o exame.")
   exame = float(input("Digite a nota do exame: "))
   media_geral = (media_geral + exame)/2
   if (media_geral >=5):
      print("Parabéns, você aproveitou a sua chance e foi aprovado!")
   else:
      print("Você não alcançou o mínimo necessário, estude mais para a próxima!")