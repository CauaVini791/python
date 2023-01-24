#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista_ordenada=[]
for c in range(5):
    lista_ordenada.append(float(input("Digite um nùmero:")))
lista_ordenada.sort()
print(f"Os valores digitados em ordem foram {lista_ordenada}.")