nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))

def maioridade (_idade, _nome):
    if (_idade >= 65):
        print("Bem vindo, ", _nome, ", você é maior de 65 anos.")
    elif (_idade >= 18 < 65):
        print("Bem vindo, ", _nome, ", você é maior de idade.")
    elif (_idade < 18):
        print("Bem vindo, ", _nome, ", você é menor de idade.")

maioridade (idade, nome)