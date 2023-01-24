#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
quantidade=maior=menor=soma=0
while True:
    numero=int(input("Informe um número:"))
    quantidade+=1
    soma=soma+numero
    if quantidade==1:
        maior=numero
        menor=numero
    else:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero
    continua_ou_para=input("Quer continuar? (DIGITE S ou N):").upper()
    if continua_ou_para=="S":
        continue
    else:
        break
print(f"A média de todos esses números é igual a {soma/quantidade}.")
print(f"O maior número informado foi {maior} e o menor foi {menor}.")