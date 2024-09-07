print("--------------------------------------")
print("Cálculo desconto loja ABC")
print("--------------------------------------")

valor1 = float(input("Digite o valor do produto: "))

def desconto_loja (compra1):
    if (compra1 >= 300):
        print("O valor da sua compra foi R$", compra1, "e o valor com desconto foi R$", (compra1*0.8))
    elif (compra1 >= 200 < 300):
        print("O valor da sua compra foi R$", compra1, "e o valor com desconto foi R$", (compra1*0.9))
    elif (compra1 < 200):
        print("O valor da sua compra foi R$", compra1, "e o valor com desconto foi R$", (compra1*0.95))

desconto_loja (valor1)