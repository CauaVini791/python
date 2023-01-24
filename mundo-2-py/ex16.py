#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro_termo=int(input("Informe o primeiro termo da PA:"))
razão=int(input("Informe a razão da PA:"))
último_termo=primeiro_termo+(10*razão)
for c in range(primeiro_termo,último_termo,razão):
    print(c)