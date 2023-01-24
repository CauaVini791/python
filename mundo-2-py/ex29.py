#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
quantidade=0
soma=0
while True:
    número=int(input("Informe um número [DIGITE 999 PARA PARAR]:"))
    if número!=999:
        quantidade+=1
        soma+=número
        continue
    else:
        print(f"Foram digitados {quantidade} números e a soma deles é igual a {soma}.")
        break