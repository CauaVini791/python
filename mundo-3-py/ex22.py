#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dict_informações={}
lista_gols=[]
dict_informações['Nome']=input("Digite o nome do jogador: ")
partidas=int(input("Quantas partidas ele jogou? "))
for c in range(partidas):
    lista_gols.append(int(input("Quantos gols ele fez na partida " + str(c+1) + "? ")))
dict_informações['Gols']=lista_gols
dict_informações['Total_Gols']=sum(lista_gols)
print(dict_informações)
print('-'*60)
print(f"""O campo 'Nome' tem o valor {dict_informações['Nome']}
O campo 'Gols' tem o valor {dict_informações['Gols']}
O campo 'Total_Gols' tem o valor {dict_informações['Total_Gols']}""")
print('-'*60)
print(f"O jogador {dict_informações['Nome']} jogou {partidas} partidas.")
for c in range(partidas):
    print(f"Na partida {c+1}, fez {lista_gols[c]} gols.")
print(f"Totalizando {dict_informações['Total_Gols']} gols.")