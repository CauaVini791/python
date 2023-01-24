#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta pinta uma área de 2m**2.
largura=float(input("Informe a largura em metros:"))
altura=float(input("Informe a altura em metros:"))
area=largura*altura
tinta=area/2
print(f"Com uma área de {area} metros, você vai gastar {tinta} litros de tinta.")