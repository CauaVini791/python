#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont=soma=0
while True:
    numero=int(input("Informe um número:"))
    if numero!=999:
        cont+=1
        soma+=numero
    else:
        break
print(f"Foram digitados {cont} números e a soma de todos eles é igual a {soma}.")