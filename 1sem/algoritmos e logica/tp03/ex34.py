compra = float(input("Digite o valor de sua compra: "))

if (compra >= 300):
    print("Você tem o direito a 20% de desconto. O valor total de sua compra foi ", compra, "e o valor com desconto foi ", compra*0.8)
elif (compra >= 200 < 300):
    print("Você tem o direito a 10% de desconto. O valor total de sua compra foi ", compra, "e o valor com desconto foi ", compra*0.9)
elif (compra < 200):
    print("Você tem o direito a 5% de desconto. O valor total de sua compra foi ", compra, "e o valor com desconto foi ", compra*0.95)
