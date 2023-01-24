#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma=0
for c in range(6):
    numero=int(input("Informe um número:"))
    if numero%2==0:
        soma=soma+numero
print(soma)