#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista_geral=[]
lista_pares=[]
lista_ímpares=[]
número=0
while True:
    número=int(input("Digite um número:"))
    lista_geral.append(número)
    if número%2==0:
        lista_pares.append(número)
    else:
        lista_ímpares.append(número)
    pergunta=input("Deseja continuar (S/N)?").upper()
    if pergunta=="S":
        continue
    else:
        break
print(f"A lista completa é: {lista_geral}")
print(f"A lista de pares é: {lista_pares}")
print(f"A lista de ímpares é: {lista_ímpares}")