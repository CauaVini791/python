#Faça um algorítimo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.
preço=float(input("Informe o valor do produto:"))
desconto=preço*0.05
novo_preço=preço-desconto
print(f"O produto ficará por {novo_preço} reais com 5% de desconto.")