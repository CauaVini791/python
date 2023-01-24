#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
numero=float(input("Informe um número:"))
print("O número inteiro digitado foi {} e sua parte inteira é {}.".format(numero,math.trunc(numero)))