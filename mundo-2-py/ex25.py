#Faça um programa que leia um número qualquer e mostre o seu fatorial.
numero=float(input("Informe um número:"))
n=1
fatorial=1
while n<numero:
    fatorial=fatorial*n
    valor_fatorial=fatorial*numero
    n=n+1
print(f"O fatorial de {numero} é igual a {valor_fatorial}.")