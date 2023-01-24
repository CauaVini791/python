#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
tentativas=0
computador=randint(0,10)
while True:
    jogador=int(input("Escolha um número entre 0 e 10:"))
    tentativas=tentativas+1
    if computador==jogador:
        print(f"PARABÉNS. Você pensou o mesmo número que a máquina, após tentar {tentativas} vez(es).")
        break
    else:
        if jogador>computador:
            print("Menos... Tente novamente.")
        elif jogador<computador:
            print("Mais... Tente novamente.")
        continue