#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitórias=0
while True:
    escolha=input("Você quer par ou ímpar?(DIGITE PAR OU ÍMPAR)").upper()
    jogador=int(input("Escolha um número entre 0 e 10:"))
    computador=randint(0,10)
    soma=computador+jogador
    if escolha=="ÍMPAR":
        if soma%2==0:
            print("Você perdeu. TENTE NOVAMENTE.")
            print(f"Deu par!!! Você escolheu {jogador} e o computador escolheu {computador}, resultando em {soma}.")
            break
        elif soma%2==1:
            vitórias+=1
            print("PARABÉNS!!! Você ganhou.")
            print(f"Deu ímpar!!! Você escolheu {jogador} e o computador escolheu {computador}, resultando em {soma}.")
            continue
    elif escolha=="PAR":
        if soma%2==0:
            vitórias+=1
            print("PARABÉNS!!! Você ganhou.")
            print(f"Deu par!!! Você escolheu {jogador} e o computador escolheu {computador}, resultando em {soma}.")
            continue
        elif soma%2==1:
            print("Você perdeu. TENTE NOVAMENTE.")
            print(f"Deu ímpar!!! Você escolheu {jogador} e o computador escolheu {computador}, resultando em {soma}.")
            break
print(f"Você conseguiu {vitórias} vitória(s) consecutiva(s).")