#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def área(l,c):
    print(f"A área do terreno com {l} de largura e {c} de comprimento é igual a {l*c} metros.")

while True:
    l=float(input("Digite a largura do terreno: "))
    c=float(input("Digite o comprimento do terreno: "))
    área(l,c)