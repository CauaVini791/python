#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
menor_peso=0
maior_peso=0
peso_inicial=0
for c in range(0,5):
    peso=float(input("Informe seu peso:"))
    if c==0:
        maior_peso=peso
        menor_peso=peso
    else: 
        if peso>maior_peso:
            maior_peso=peso
        if peso<menor_peso:
            menor_peso=peso
print(f"O maior peso lido foi {maior_peso}.")
print(f"O menor peso lido foi {menor_peso}.")