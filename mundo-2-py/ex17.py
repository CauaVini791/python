#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont=0
numero=int(input("Informe um número:"))
for c in range(1,numero+1):
    if numero%c==0:
        cont=cont+1
if cont==2:
    print(f"O número {numero} é primo.")
elif cont>=3:
    print(f"O número {numero} não é primo.")