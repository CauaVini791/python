#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere o dólar valendo 3.27.
valor=float(input("Informe o valor que você tem na carteira: R$"))
dolar=valor/3.27
print(f"Com {valor} reais, você pode comprar {dolar:.2f} dólares.")