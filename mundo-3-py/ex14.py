#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista_números=[[],[]]
número=0
for c in range(7):
    número=float(input("Digite um número: "))
    if número%2==0:
        lista_números[0].append(número)
    else:
        lista_números[1].append(número)
print(f"Os valores pares digitados foram: {lista_números[0]}")
print(f"Os valores ímpares digitados foram: {lista_números[1]}")