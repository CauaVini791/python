#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas 
#B) A média de idade 
#C) Uma lista com as mulheres 
#D) Uma lista de pessoas com idade acima da média
dict_informações={}
lista_informações=[]
pessoas=0
soma_idades=0
média_idade=0
while True:
    dict_informações['Nome']=input("Nome: ")
    pessoas+=1
    sexo=input("Sexo: ").upper()
    if sexo=="F" or sexo=="M":
        dict_informações['Sexo']=sexo
    else:
        print("ERRO! Por favor, digite apenas M ou F.")
        sexo=input("Sexo: ").upper()
        dict_informações['Sexo']=sexo
    dict_informações['Idade']=int(input('Idade: '))
    soma_idades+=dict_informações['Idade']
    lista_informações.append(dict_informações.copy())
    dict_informações.clear()
    pergunta=input("Quer continuar? [S/N] ").upper()
    if pergunta=="S":
        continue
    elif pergunta=="N":
        break
    else:
        print("ERRO! Responda apenas S ou N.")
        pergunta=input("Quer continuar? [S/N] ").upper()
        if pergunta=="S":
            continue
        else:
            break
média_idade=soma_idades/pessoas
print(f"Ao todo, foram cadastradas {pessoas} pessoas.")
print(f"A média de idade é de {média_idade} anos.")
print("Lista de mulheres cadastradas: ", end="")
for c in lista_informações:
    if c['Sexo']=="F":
        print(c['Nome'], end=" ")
print()
print("Lista de pessoas com idade acima da média: ", end="")
for c in lista_informações:
    if c['Idade']>média_idade:
        print(c, end=" ")