#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
numero=int(input("Informe um número:"))
antecessor=numero-1
sucessor=numero+1
print("O antecessor do número {} é {}, e seu sucessor é {}.".format(numero,antecessor,sucessor))