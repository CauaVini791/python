#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8
elementos=int(input("Informe quantos elementos você quer mostrar:"))
el1=0
el2=1
cont=3
print(el1)
print(el2)
while cont<=elementos:
    el3=el2+el1
    print(el3)
    cont=cont+1
    el1=el2
    el2=el3