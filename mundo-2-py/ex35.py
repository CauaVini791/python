#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total=produtos_mais_1000=mais_barato=menor_valor=0
n=0
while True:
    produto=input("Informe o nome do produto: ")
    preço=float(input("Qual o valor do produto? "))
    total+=preço
    if preço>1000:
        produtos_mais_1000+=1
    if n==0:
        menor_valor=preço
        mais_barato=produto
    if n!=0:
        if preço<menor_valor:
            menor_valor=preço
            mais_barato=produto
    continuar=input("Deseja continuar?(S/N): ").upper()
    if continuar=="S":
        n+=1
        continue
    else: 
        break
print(f"O valor total da compra foi de {total} reais.")
print(f"{produtos_mais_1000} produtos custaram mais de 1000 reais.")
print(f"O produto mais barato foi o {mais_barato}.")