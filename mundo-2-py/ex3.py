#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: o primeiro valor é maior, o segundo valor é maior, não existe valor maior, os dois são iguais.
numero1=int(input("Digite um número:"))
numero2=int(input("Digite outro número:"))
if numero1>numero2:
    print("O primeiro valor é maior.")
elif numero1<numero2:
    print("O segunda valor é maior.")
else:
    print("Os dois valores são iguais.")