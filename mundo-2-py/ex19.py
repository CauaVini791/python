#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
cont=0
for c in range(0,7):
    ano=int(input("Informe seu ano de nascimento:"))
    if ano>=2004:
        cont=cont+1
print(f"{cont} pessoas ainda não atingiram a maioridade.")