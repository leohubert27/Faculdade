print("------------------------------------------------------------------------------")
print("CÁLCULO DE ÍNDICE DE MASSA CORPORAL")
print("------------------------------------------------------------------------------")

genero = input("A pessoa é do gênero MASCULINO ou FEMININO? ")
peso = float(input("Digite o peso da pessoa: "))
altura = float(input("Digite a altura da pessoa: "))

#Definindo as funções do cálculo de IMC de pessoas do sexo masculino e feminino
def imc_masc (peso1, altura1):
    imc = peso1 / (altura1 ** 2)
    
    if (imc >=25):
        print("Seu IMC é: ", imc, " e você está ACIMA do peso ideal.")
    elif (imc >=20 <25):
        print("Seu IMC é: ", imc, " e você está no peso IDEAL.")
    elif (imc < 20):
        print("Seu IMC é: ", imc, " e você está ABAIXO do peso ideal.")
    elif (imc <=0):
        print("Os valores inseridos são inválidos")

def imc_fem (peso2, altura2):
    imc = peso2 / (altura2 ** 2)
    
    if (imc >=24):
        print("Seu IMC é: ", imc, " e você está ACIMA do peso ideal.")
    elif (imc >=19 <24):
        print("Seu IMC é: ", imc, " e você está no peso IDEAL.")
    elif (imc < 19):
        print("Seu IMC é: ", imc, " e você está ABAIXO do peso ideal.")
    elif (imc <=0):
        print("Os valores inseridos são inválidos")
    

#Convertendo os valores da variável gênero para caps lock e verificando qual função será chamada   
if (genero.upper() == "MASCULINO"):
    imc_masc(peso,altura)
elif (genero.upper() == "FEMININO"):
    imc_fem(peso,altura)