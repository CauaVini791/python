for c in range(10,-1,1):
    print(c)

#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print("""[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador=int(input("Qual a sua jogada?"))
computador=randint(0,2)
if computador==0:
    if jogador==0:
        print("""EMPATOU!!!
        VOCÊ ESCOLHEU PEDRA.
        O COMPUTADOR ESCOLHEU PEDRA.""")
    elif jogador==1:
        print("""VOCÊ GANHOU!!!
        VOCÊ ESCOLHEU PAPEL.
        O COMPUTADOR ESCOLHEU PEDRA.""")
    elif jogador==2:
        print("""EU GANHEI!!!
        VOCÊ ESCOLHEU TESOURA.
        O COMPUTADOR ESCOLHEU PEDRA.""")
    else:
        print("JOGADA INVÁLIDA.")
elif computador==1:
    if jogador==0:
        print("""EU GANHEI!!!
        VOCÊ ESCOLHEU PEDRA.
        O COMPUTADOR ESCOLHEU PAPEL.""")
    elif jogador==1:
        print("""EMPATOU!!!
        VOCÊ ESCOLHEU PAPEL.
        O COMPUTADOR ESCOLHEU PAPEL.""")
    elif jogador==2:
        print("""VOCÊ GANHOU!!!
        VOCÊ ESCOLHEU TESOURA.
        O COMPUTADOR ESCOLHEU PAPEL.""")
    else:
        print("JOGADA INVÁLIDA.")
elif computador==2:
    if jogador==0:
        print("""VOCÊ GANHOU!!!
        VOCÊ ESCOLHEU PEDRA.
        O COMPUTADOR ESCOLHEU TESPURA.""")
    elif jogador==1:
        print("""EU GANHEI!!!
        VOCÊ ESCOLHEU PAPEL.
        O COMPUTADOR ESCOLHEU TESOURA.""")
    elif jogador==2:
        print("""EMPATOU!!!
        VOCÊ ESCOLHEU TESOURA.
        O COMPUTADOR ESCOLHEU TESOURA.""")
    else:
        print("JOGADA INVÁLIDA.")