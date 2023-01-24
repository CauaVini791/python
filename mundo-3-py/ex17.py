#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogos=int(input("Quantos jogos você deseja? "))
números_sorteados=[]
lista_jogos=[]
for c in range(jogos):
    while True:
        número=randint(1,60)
        if número not in números_sorteados:
            números_sorteados.append(número)
        if len(números_sorteados)==6:
            break
    lista_jogos.append(números_sorteados[:])
    números_sorteados.clear()
print("           MEGA SENA          ")
print("-"*33)
for c in range(jogos):
    print(f"{c+1}º jogo: {lista_jogos[c]}")
    sleep(1)
print("-"*33)
print("          BOA SORTE!!         ")