#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:                                                                                                    
#A) Quantas pessoas foram cadastradas.                                                                                                                
#B) Uma listagem com as pessoas mais pesadas.                                                                                                    
#C) Uma listagem com as pessoas mais leves.
lista_dados=[]
dados=[]
n=0
maior_peso=menor_peso=nome_maior_peso=nome_menor_peso=0
while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))
    lista_dados.append(dados[:])
    dados.clear()
    pergunta=input("Quer continuar? [S/N] ").upper()
    n+=1
    if pergunta=="S":
        continue
    else:
        break
for c in range(len(lista_dados)):
    if c==0:
        maior_peso=lista_dados[0][1]
        nome_maior_peso=lista_dados[0][0]
    else:
        if lista_dados[c][1]>maior_peso:
            maior_peso=lista_dados[c][1]
            nome_maior_peso=lista_dados[c][0]
for c in range(len(lista_dados)):
    if c==0:
        menor_peso=lista_dados[0][1]
        nome_menor_peso=lista_dados[0][0]
    else:
        if lista_dados[c][1]<menor_peso:
            menor_peso=lista_dados[c][1]
            nome_menor_peso=lista_dados[c][0]
print(f"{n} pessoas foram cadastradas.")
print(f"O maior peso foi de {nome_maior_peso} com {maior_peso} quilos.")
print(f"O menor peso foi de {nome_menor_peso} com {menor_peso} quilos.")