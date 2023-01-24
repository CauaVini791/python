#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
lista_do_dict=[]
dict_jogadores={'Jogador 1': randint(1,6), 
'Jogador 2': randint(1,6), 
'Jogador 3': randint(1,6), 
'Jogador 4': randint(1,6)}
for k, v in dict_jogadores.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
dict_jogadores=sorted(dict_jogadores.items(), key=itemgetter(1), reverse=True)
print("-"*25)
for c, posição in enumerate(dict_jogadores):
    print(f"{c+1}º lugar: {posição[0]} com {posição[1]}")